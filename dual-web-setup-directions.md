# Setting up dual-web: adding the bot surface to an existing human site

Directions for Claude (and the instructor) to take a site that **already has a human surface** and
add the **bot surface** + routing, so AI crawlers get a separate set of pages while humans and Google
get the normal site. This covers **set up only** — the scaffolding and the routing architecture.
**It does not cover generating the page content** — a separate page-conversion command does that.

> **Read this first — the one idea that makes it all work:** bots do **not** browse a separate
> "llm site." They browse your **normal domain** (`yourdomain.com`), and a Worker silently swaps in
> the bot version of each page as they go. The bot never sees a different URL. Get this one concept
> right and everything else falls into place; get it wrong and you've either leaked the bot origin or
> created a cloaking risk. See "How bots navigate" below.

---

## Where you're starting vs. where you're going

**Starting state (what the student already has):**
```
their-project/
├── app/ (or src/, or public/) …   ← the human site (Next.js, static, whatever)
└── …
```

**Ending state (what this setup adds):**
```
their-project/
├── app/ …                          ← human site (UNCHANGED)
├── llm/                            ← NEW: the bot surface (static HTML, zero-JS)
│   ├── index.html
│   ├── about.html
│   ├── blog/  …                    ← mirrors the human site's structure, slug-for-slug
│   ├── robots.txt
│   ├── sitemap.xml
│   └── _headers
└── infra/
    └── worker.js                   ← NEW: the router (UA-based serving)
```

The human site is **never modified**. The bot surface is purely additive.

---

## How bots navigate (the architecture — explain this to students)

```
   AI bot requests  yourdomain.com/about
            │
            ▼
   ┌──────────────────────┐   reads User-Agent
   │   WORKER (router)     │── is it an AI bot? ──┐
   └──────────────────────┘                       │
            │ human / Google                       │ yes
            ▼                                       ▼
   normal human site                  fetches  llm-pages.pages.dev/about.html
   (untouched)                        and returns it AS yourdomain.com/about
                                      (URL never changes — pass-through proxy)
```

The bot lands on `yourdomain.com/about`, sees a link to `/pricing`, and requests
`yourdomain.com/pricing` — the Worker intercepts **that** too and serves the bot version of pricing.
The bot walks the whole site this way, always on the apex, never knowing the `.pages.dev` origin
exists.

**This only works if every bot page obeys the path-mirror contract (below). That's the real setup
job — not the files, the contract.**

---

## The path-mirror contract (the rules every bot page must satisfy)

Whoever creates the pages (your conversion command) must produce HTML that follows these invariants.
**Claude's setup job is to enforce/verify these**, because a violation silently breaks bot navigation
or trips cloaking detection:

| Rule | Right | Wrong |
|---|---|---|
| **Internal links use apex paths** | `<a href="/pricing">` | `<a href="https://llm-pages.pages.dev/pricing.html">` ← leaks the bot origin |
| **Canonical points to the HUMAN url** | `<link rel="canonical" href="https://yourdomain.com/pricing">` | canonical to `.pages.dev` ← tells Google the bot page is the original |
| **Filenames match human slugs** | human `/blog/foo` ↔ bot `llm/blog/foo.html` | mismatched names ← Worker can't find the file |
| **Sitemap uses apex human URLs** | `<loc>https://yourdomain.com/blog</loc>` | `.pages.dev` or `.html` URLs |
| **Zero JS-gated content** | content is in the HTML on load | content rendered by client JS ← bots can't read it |

> **Why canonical → human URL?** Both surfaces show the same content. The canonical tells search
> engines "the human page is the original; don't treat the bot page as duplicate/competing content."
> This is what keeps the setup **cloaking-safe**: Google and humans get identical pages, only AI
> crawlers get the bot variant, and every bot page openly points back to its human twin.

---

## Setup steps

### Step 1 — Create the `llm/` scaffold

Create the `llm/` directory mirroring the human site's URL structure (one `.html` per human page,
subdirectories for nested paths like `blog/`). The page *content* comes from the conversion command;
this step is just the folder skeleton plus the three bot-surface essentials:

**`llm/robots.txt`** — open to all crawlers, points to the sitemap:
```
User-agent: *
Allow: /

Sitemap: https://yourdomain.com/sitemap.xml
```

**`llm/sitemap.xml`** — lists every page as its **apex human URL** (not `.pages.dev`, not `.html`):
```xml
<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  <url><loc>https://yourdomain.com/about</loc><changefreq>monthly</changefreq><priority>0.8</priority></url>
  <url><loc>https://yourdomain.com/blog</loc><changefreq>weekly</changefreq><priority>0.9</priority></url>
  <!-- one <url> per page -->
</urlset>
```

**`llm/_headers`** — security headers Cloudflare Pages applies to the bot surface:
```
/*
  X-Frame-Options: DENY
  X-Content-Type-Options: nosniff
  Referrer-Policy: strict-origin-when-cross-origin
  Permissions-Policy: geolocation=(), microphone=(), camera=()
```

### Step 2 — Create the router Worker (`infra/worker.js`)

The Worker reads the `User-Agent`, and: AI bots → fetch the Pages bot site; humans **and traditional
search engines (Google/Bing)** → pass through to the human origin untouched. The minimal shape:

```js
export default {
  async fetch(request) {
    const ua = (request.headers.get('user-agent') || '').toLowerCase();
    const url = new URL(request.url);

    // AI crawlers that may receive the bot surface.
    const aiBots = [
      'gptbot', 'oai-searchbot', 'chatgpt-user', 'claudebot', 'claude-user',
      'perplexitybot', 'perplexity-user', 'ccbot', 'google-extended', 'bytespider',
      'amazonbot',
      // …keep this list current from Cloudflare's AI Crawl Control dashboard
    ];

    // CRITICAL: traditional search engines must get the SAME pages as humans
    // (serving them the bot surface would be cloaking). They are NOT in aiBots.
    // Same goes for social preview crawlers (facebookexternalhit, Twitterbot,
    // LinkedInBot, meta-externalagent): they build link-share cards from the
    // page they fetch, so they must hit the human site to get its OG image.
    const isAiBot = aiBots.some(b => ua.includes(b));

    if (isAiBot) {
      // Map the apex path to the Pages bot file. The bot still sees yourdomain.com —
      // this is a pass-through proxy, not a redirect.
      return fetch('https://YOUR-PAGES-PROJECT.pages.dev' + url.pathname, {
        method: request.method,
        headers: request.headers,
        body: request.body,
      });
    }

    // Humans + Googlebot/Bingbot → the real human site, untouched.
    return fetch(request);
  },
};
```

> Two non-negotiables in this file:
> 1. **Google/Bing are NOT in the bot list** — they get exactly what humans get, or it's cloaking.
> 2. The bot branch is a **`fetch()` of the `.pages.dev` URL returned as-is** — a proxy, so the
>    visitor's URL stays on the apex. Never a `Response.redirect()`.

### Step 3 — Deploy both, and point the domain at the Worker

The two pieces deploy in **two different ways** — see the companion doc
**cloudflare-llm-hosting-setup.md** for the full, beginner-tested flow:

- **Bot pages (Pages) → auto-pull from GitHub.** Connect Cloudflare Pages to the repo once in
  the dashboard (Workers & Pages → Create → Pages → Connect to Git), production branch `main`,
  build output directory `llm/`, no build command. After that, **every `git push` auto-rebuilds
  and redeploys the bot surface** — no manual upload. This is dashboard state, not repo config.
- **Worker → CLI.** `wrangler deploy`, with `routes` in `wrangler.toml` binding it to
  `yourdomain.com`. The Worker is the only piece that ships by command.

The Worker's `YOUR-PAGES-PROJECT.pages.dev` URL must match the Pages project you connected.

---

## How Claude should verify the setup is correct

After scaffolding + the page-conversion command have run, Claude should check the contract holds:

1. **Slug parity** — every human page has a matching `llm/<slug>.html`. List both, diff the sets.
2. **No origin leakage** — grep the `llm/` HTML for `.pages.dev`; there should be **zero** hits in
   page links (the Worker config is the only place that URL belongs).
3. **Canonicals point home** — every `llm/*.html` has `<link rel="canonical" href="https://yourdomain.com/…">`.
4. **Live routing test** — after deploy, two requests must return *different* pages:
   ```bash
   curl -A "GPTBot"  https://yourdomain.com/    # bot surface
   curl -A "Mozilla" https://yourdomain.com/    # human site
   ```
   And a traditional-search check must return the **human** page (cloaking guard):
   ```bash
   curl -A "Googlebot" https://yourdomain.com/  # must match the Mozilla result, NOT the GPTBot one
   ```

---

*Companion docs: **cloudflare-llm-hosting-setup.md** (the CLI deploy flow) and the page-conversion
command (generates the actual `llm/*.html` content). This doc is the scaffolding + routing
architecture only.*

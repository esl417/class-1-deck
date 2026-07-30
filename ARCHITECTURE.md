# Architecture — the classes site

How this repo is structured, how the decks are served, and how the **dual-web
teaching layer** works (the system that lets a student paste a deck link and have
Claude receive a private, instructor-authored teaching version of that deck).

This is an internal doc — it is in `.vercelignore` and never served to students.

> Not to be confused with `dual-web-setup-directions.md` and
> `cloudflare-llm-hosting-setup.md` at the repo root — those are **Class 3
> teaching content** (the dual-web setup students build for *their own* sites).
> This doc is about how *this repo* is built.

---

## 1. The decks

Each class is a single self-contained hand-authored HTML file. No framework, no
build step for the decks themselves — just static HTML/CSS/JS served as-is.

```
class-1-website-build/  index.html   prereqs.html   fonts/  *.png   (+ student kits)
class-2-dashboard-build/ index.html  prereqs.html   ...
class-3-seo-geo/        index.html   prereqs.html   ...   build-reference/  cloudflare-student-kit/
class-4-automations/    index.html                  ...   (no prereqs deck)
index.html              (landing page linking to all decks)
```

A **slide** is `<section class="slide">` (or `slide dense`) inside `<div class="deck">`.
Each carries a `<div class="slide-num" data-label="…">`; at runtime the deck's inline
JS renders it as `"<n> · <label>"` (e.g. `4 · No real data yet?`), where `n` is the
slide's position in document order. That number+label is how a student refers to a
slide ("slide 4", "the no-real-data slide") and how the bot view is addressed.

### Diagram components

Concept diagrams are plain HTML/CSS using each deck's existing tokens
(`--accent`, `--surface`, `--hair`, `--display`), not exported images — so they
theme with the deck, scale with `clamp()`, and stay editable as text. Each deck
carries its own copy in its `<style>` block (same as `.arrow-flow`); there is no
shared stylesheet.

- `.arrow-flow` — a straight left-to-right chain. Use only when the concept
  really is linear.
- `.flow-converge` — several inputs bracketing into one hub, then an output
  (`.flow-hub`, `.flow-join`, `.flow-outcome`). For "these do different jobs"
  relationships a chain would flatten.
- `.flow-linkpair` — the same two nodes drawn twice, once severed and once
  connected (`.link-wire.is-broken` / `.is-solid`). For "without X / with X",
  where the point is whether the connection exists at all.
- `.flow-fork` — one input, a decision node, two destinations (`.fork-gate`,
  `.flow-split`, `.fork-dest`). For either/or routing, which a straight chain
  misrepresents as then/then.
- `.flow-stack` — layers in front-to-back order (`.stack-layer.is-front`). For
  architecture where the concept is position in space, not sequence in time.
- `.flow-canon` — two twins with one openly pointing home (`.canon-page`,
  `.canon-link`). Built for the canonical-link rule in Class 3.

**A diagram placed above a card grid must not look like a header row.** If its
boxes are full-width and land on the same column positions as the cards below,
readers infer a mapping that isn't there. Size the diagram's nodes to their
content, center them, and set the whole thing in a tinted band so it reads as
one self-contained object. Keep labels in plain language — this audience does
not write markup, so a code-styled tag (`rel="canonical"`) is jargon they can't
act on; say what it means instead.

Where a diagram makes an adjacent card redundant, fold the card's detail into
the diagram and delete the card — a picture beside prose that says the same
thing reads as duplication, not reinforcement. Removing content can also make a
slide's `dense` modifier unnecessary; drop it so the slide re-centers. Note
`dense` pins to the top and can make a marginal overflow *worse*, since the
saved type height doesn't offset the lost centering — measure, don't assume.

**Arrowheads:** every connector uses one shape at one size. Do not mix a `→`
text glyph with a drawn arrow — the glyph's weight comes from the font and won't
match. Avoid `preserveAspectRatio="none"` on any SVG containing an arrowhead: a
stretched viewBox renders identical coordinates at different physical sizes and
distorts the head. Stretch only with CSS borders; keep arrow SVGs 1:1.

- **Host:** Vercel (project `classes`, public domain `classes.ericgrows.com`).
- **DNS:** `ericgrows.com` is on Cloudflare, proxying to the Vercel origin.
- **Deploy:** push to `main` → Vercel builds and serves.
- Decks are `noindex`; `robots.txt` still allows crawlers so they can read the pages.

---

## 2. The dual-web teaching layer — what it is

When a student pastes a deck URL and hands it to Claude, we want Claude to receive
a richer, **instructor-authored** version of that deck — the slide content **plus
private teaching notes** that tell Claude who the student is, what's likely broken,
and how to teach (not just do) each slide. Humans and search engines keep getting
the normal deck.

The whole thing turns on **one rule**: same URL for the student, different content
by requester. A student never manages two links.

### Why a Cloudflare Worker (and not vercel.json)

A `vercel.json` rewrite **cannot** do this: Vercel serves a real file on disk (the
deck's `index.html`) *before* rewrites run ("filesystem precedence"), so a same-URL
swap can't fire there. A **Cloudflare Worker sits in front of the Vercel origin** and
intercepts the request first — so the swap is clean and the student's URL never changes.

### The flow

```
student pastes:  classes.ericgrows.com/class-2-dashboard-build/   (one URL, always)
                          │
                 Cloudflare Worker (infra/worker.js)  ── reads User-Agent
                   ├─ AI crawler?  → pass-through fetch of  <deck>/llm.md
                   ├─ Google/Bing? → pass through to the normal deck (NO cloaking)
                   ├─ social preview crawler? → normal deck (real OG image)
                   └─ human?       → pass through to the normal deck
                          │
                     Vercel origin  (decks + generated llm.md files)
```

- The swap is a **pass-through fetch**, never a redirect — the URL stays put.
- Google/Bing get the **human** page. Serving them the bot view would be cloaking.
- Only **deck paths that have a bot view** are swapped (see `BOT_VIEWS` in the
  Worker); assets, other paths, and the `llm.md` files themselves pass through.

---

## 3. The moving parts

| File | Role | Edited by |
|---|---|---|
| `<deck>/index.html`, `prereqs.html` | The human decks. **Never modified by this system.** | Hand (deck authoring) |
| `<deck>/teaching.md`, `prereqs-teaching.md` | **Private per-slide teaching notes**, keyed by slide label. Never served to humans. | Hand (this is what you author) |
| `llm-preamble.md` (root) | **Shared** teaching contract prepended to every bot view — who the student is, the arc, teach-first house rules. One edit changes all decks. | Hand |
| `build-llm.mjs` (root) | Build script: reads each deck's HTML + its teaching notes + the preamble, emits `<deck>/llm.md`. | Rarely |
| `<deck>/llm.md`, `prereqs-llm.md` | **Generated** bot views (what Claude actually fetches). Banner-marked "do not edit". Committed for backup. | Never (generated) |
| `infra/worker.js` | The Cloudflare Worker: UA-sniff + pass-through swap. Holds the `BOT_VIEWS` path map. | When adding a deck |
| `infra/wrangler.toml` | Worker config. **Route** binding on `classes.ericgrows.com/*` (NOT `custom_domain`, which would delete the Vercel DNS record). | Rarely |
| `vercel.json` | `buildCommand: node build-llm.mjs`, `outputDirectory: "."` — so Vercel regenerates the bot views on every deploy. | Rarely |

### How a bot view is assembled

`build-llm.mjs` produces one `llm.md` per deck:

1. A `<!-- GENERATED … -->` banner (nobody hand-edits `llm.md`).
2. The deck title + the **shared preamble** (`llm-preamble.md`) + a per-deck
   **`standing`** line (what the student has by now / this deck's failure modes),
   both defined in the `DECKS` array in `build-llm.mjs`.
3. One section per slide: `## Slide <n> · <label>`, the slide content **verbatim**
   (so Claude sees exactly what the student sees — prompt boxes are flagged as
   executable), followed by the matching **teaching note** if one exists.

Teaching notes are matched to slides **by label**. If a `teaching.md` note's label
matches no slide (e.g. a slide was renamed), the build prints a loud **orphan
warning** — the drift catch. Fix the label so it matches.

### Addressing

The bot view's `## Slide <n> · <label>` headings carry the **same number** the deck
computes at runtime (both count `<section class="slide">` in document order), so a
student saying "slide 4" resolves correctly. Notes are keyed by **label** (rename-safe);
the number is stamped in automatically.

### Privacy of teaching notes

Teaching notes live in `teaching.md`, **not** in `index.html`, so they never appear
in a human's View Source. The `teaching.md` files *are* technically fetchable at the
origin (the Vercel build needs them), but nothing links to them and the repo is
private — acceptable as long as those paths aren't published anywhere.

---

## 4. Authoring — how to edit or add teaching notes

**Edit a note (most common):**
1. Open the deck's `teaching.md` (or `prereqs-teaching.md`).
2. Find the `## <slide label>` section (label = the slide's `data-label`) and edit,
   or add a new `## <exact slide label>` section for a slide that has none.
3. `node build-llm.mjs` — regenerates the bot views; watch for orphan warnings.
4. Commit + push. Vercel regenerates `llm.md` on deploy. **No Worker deploy needed**
   (paths unchanged; the Worker just proxies whatever the origin serves).

**Change the teaching stance for ALL decks:** edit `llm-preamble.md` (the house
rules), then rebuild + push. It's prepended to every bot view.

**Author notes to this standard:**
- Teach the skill; don't perform the tool. Where a slide has a command/prompt, teach
  what it is, when to reach for it, how to judge the result — don't stand in for it.
- The preamble already states the universal rules (audience, teach-first, adapt
  prompts, websearch third-party UIs, "do-it-yourself = own the judgment"). Notes
  add only what's specific to their slide; don't restate the preamble.
- First-encounter slides teach the **category**, not just the instance (first skill,
  first agent, first git wiring, first MCP, first API key).
- Prereqs notes are **recovery-focused**: the student is mid-setup and something
  broke — name the specific failure and the fix.

---

## 5. Adding a whole new deck

1. **DECKS entry** in `build-llm.mjs` — `dir`, `title`, `standing` (what the student
   has by now + this deck's failure modes). A secondary deck in the same folder
   (like a prereqs deck) also sets `file`, `out`, and `teaching` (e.g.
   `prereqs.html` → `prereqs-llm.md` from `prereqs-teaching.md`).
2. **`teaching.md`** (and `prereqs-teaching.md`) in the deck folder — `## <label>`
   per noted slide.
3. **`BOT_VIEWS`** in `infra/worker.js` — add the request path(s) → bot-view path.
   A deck root needs both `/dir` and `/dir/`; a named page needs its exact path
   (e.g. `/dir/prereqs.html`).
4. `node build-llm.mjs`, commit, **push**, and **wait for Vercel** to serve the new
   `llm.md` (poll `curl -s -o /dev/null -w '%{http_code}' <url>/dir/llm.md` for 200).
5. **Deploy the Worker** (only needed because `BOT_VIEWS` changed):
   `cd infra && npx wrangler deploy`.

Order matters: the `llm.md` must be live at the origin **before** the Worker points
at it, or bots get a 404.

---

## 6. Verifying the dual surface

After deploying, confirm each requester gets the right thing at the same URL:

```bash
URL="https://classes.ericgrows.com/class-1-website-build/"
# AI bot → bot view (contains "the bot view of this deck")
curl -s -A "ClaudeBot/1.0" "$URL" | grep -c "the bot view of this deck"   # 1
# human → the deck
curl -s -A "Mozilla/5.0 Chrome/120" "$URL" | grep -c "the bot view"       # 0
# Googlebot → the deck, NOT the bot view (cloaking-safety)
curl -s -A "Googlebot/2.1" "$URL" | grep -c "the bot view"                # 0
```

All three must hold on every deck path. A bot getting the deck (not the bot view)
usually means its UA isn't in the Worker's `aiSearchBots` list, or the path isn't in
`BOT_VIEWS`. Google getting the bot view is a cloaking bug — fix immediately.

---

## 7. Deploy quick-reference

- **Edited a teaching note or the preamble:** rebuild → commit → push. Done (Vercel
  regenerates `llm.md`). No Worker deploy.
- **Added/renamed a deck path, or changed UA lists:** rebuild → commit → push → wait
  for Vercel → `cd infra && npx wrangler deploy`.
- **Never** hand-edit `llm.md` / `prereqs-llm.md` — they're generated.
- Live domain: `classes.ericgrows.com`. Worker: `classes-dual-web` (route-bound).

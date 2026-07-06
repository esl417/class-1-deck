# Hosting an LLM/bot site on Cloudflare — all from the command line

A reference for setting up the dual-surface site (human pages + AI-bot pages) on Cloudflare,
done almost entirely through the CLI. This is the **free + more-secure** path. The only thing
you can't do from the terminal is one **one-time** DNS step on day one.

> **How this works in class.** Students don't memorize these commands — **they ask Claude to do
> it**, and Claude runs the commands. That's the whole model. The commands below are written out so
> Claude runs them correctly and so you (the instructor) can follow along, but a student's actual job
> is to say *"Claude, deploy the bot pages"* and approve a browser login when prompted. Because Claude
> is doing the typing, the single most important setup step is **giving Claude accurate Cloudflare
> knowledge** (next section) — otherwise it guesses with stale info and sends students down broken
> paths.

> **Why Cloudflare and not Vercel?** Putting everything on Vercel and doing the bot-routing there
> requires **Vercel Pro ($20/mo)** — and even then its security posture (DDoS, WAF, bot management)
> is *weaker* than what Cloudflare gives you on its **free** tier. So Cloudflare = $0 + stronger
> security. The only thing Vercel buys is fewer concepts to learn. This doc is the "get both" path:
> keep Cloudflare's free security, and still drive the whole setup from the CLI.

---

## How the site is wired (the mental model)

Three pieces. Learn these names — the rest is mechanical.

1. **Worker** (`aso-router`) — a tiny program that runs at your domain (`yourdomain.com`) and looks
   at *who* is asking. If it's an AI bot (GPTBot, ClaudeBot, PerplexityBot, …) it serves the
   bot-optimized pages. If it's a human or Google/Bing, it serves the normal website. This is the
   front door.
2. **Pages** — Cloudflare's static-file host. It holds the **bot pages** (the `llm/` HTML). It does
   **NOT need a custom domain** — the Worker reaches it by its built-in `*.pages.dev` address.
3. **DNS** — points `yourdomain.com` at Cloudflare so the Worker can sit in front. One-time setup.

```
                         ┌─────────────────────────────┐
   visitor ──────────────►   WORKER (aso-router)        │
   (human / bot)         │   reads User-Agent header    │
                         └──────────┬──────────┬────────┘
                            human/  │          │  AI bot
                            Google  │          │
                                    ▼          ▼
                          normal website    PAGES (.pages.dev)
                          (your origin)     llm/*.html bot pages
```

---

## 🧠 Give Claude its Cloudflare knowledge (the keystone step)

**Do this once, before anything else.** Cloudflare publishes a set of **skills** — reference docs
that teach Claude the *current, correct* way to use every Cloudflare tool (Wrangler, Pages, Workers,
config formats, etc.). They explicitly tell Claude to **look up the live docs instead of guessing
from memory**, which is exactly what prevents the "Claude tried an outdated command and broke
everything" failure mode.

Since students drive Claude (they don't type the commands themselves), Claude's accuracy *is* the
student's success. So this step matters more than any other.

**You don't run these — you ask Claude to.** Say to Claude:

> *"Set up the Cloudflare developer tools."*

Claude will run these two commands itself:

```bash
claude plugin marketplace add cloudflare/skills    # installs the skills (the knowledge)
claude plugin install cloudflare@cloudflare         # installs the MCP server (live tools + docs)
```

Then **you** run one command inside Claude to activate them:

```
/reload-plugins
```

That's the entire setup. After this:
- The **skills** make Claude write correct Cloudflare commands instead of guessing.
- The **MCP server** lets Claude check deploy status and read Cloudflare docs live.
- **OAuth happens automatically** the first time Claude touches a Cloudflare service — it pops a
  browser window, the student clicks **Allow**, done. (Same one-time browser approval as
  `wrangler login` below — they're the same login moment.)

> **Why both commands?** The first installs the knowledge (skills). The second adds the live tools
> (MCP). For a class, install both — the MCP server is genuinely useful and the OAuth is a one-time
> click students already do anyway. If you ever want the absolute-minimum footprint, the first
> command alone gives Claude the knowledge without the extra MCP/OAuth layer.

> ⚠️ **Instructor note — already used Cloudflare before?** If your machine has an older Cloudflare
> API token lying around (e.g. in a `.env.local` or shell profile from prior work), it can collide
> with the fresh browser login and cause confusing "authentication error" / "missing permission"
> failures — even though the new login is correct. The fix: run `npx wrangler@latest logout`, then
> `npx wrangler@latest login` fresh, and approve **all** permissions on the consent screen. A
> student on a clean laptop never hits this; **you, the instructor, are the most likely person in
> the room to.** (We hit exactly this during testing — it's a stale-credential conflict, not a
> problem with the workflow.)

---

## ⚙️ Setting up your computer (do this FIRST)

**Everything below requires Node.js.** Node is what gives you `npm` and `npx`, and `npx` is how we
run Cloudflare's tool (Wrangler) without a complicated install. If you don't have Node, nothing else
works — so start here.

### Step A — Check what you already have

Open your terminal (Mac: **Terminal** app; Windows: **PowerShell**) and run these one at a time:

```bash
node --version     # want v18 or higher (e.g. v20, v24)
npm --version      # any version is fine
```

- **Both print a version number** → you're set. Skip to "Step B".
- **You see "command not found"** (or similar) → you don't have Node yet. Install it ↓

### Step A.1 — Install Node.js (only if the check above failed)

You only need ONE of these. Pick the row for your situation:

| Your computer | How to install Node |
|---|---|
| **Mac or Windows — easiest** | Go to **https://nodejs.org**, download the **LTS** version, run the installer, click through. Restart your terminal. Re-run `node --version` to confirm. |
| **Mac with Homebrew** | `brew install node` |
| **Windows with winget** | `winget install OpenJS.NodeJS.LTS` |
| **Linux (Debian/Ubuntu)** | `sudo apt update && sudo apt install nodejs npm` |

> 💡 The nodejs.org installer is the safest choice for non-technical folks — no command line
> needed to install it, and it sets up `npm` and `npx` automatically. After installing, **close
> and reopen your terminal**, then re-run `node --version` to make sure it worked.

### Step B — You do NOT need to install Wrangler separately

Cloudflare's CLI is called **Wrangler**. You might see guides say `npm install -g wrangler` — you
can skip that. Instead we use **`npx`**, which comes free with Node and runs the latest Wrangler
on demand:

```bash
npx wrangler@latest --version
```

The first time you run it, it downloads Wrangler automatically (takes a few seconds) and prints a
version like `4.102.0`. That's it — no install step, no admin rights, nothing to maintain. Every
command in this doc uses `npx wrangler@latest …` for exactly this reason.

> **Why `npx` instead of installing?** A global install (`npm install -g`) can fail without admin
> permissions and goes stale. `npx wrangler@latest` always grabs the current version and needs no
> special setup — it's the reliable choice when a roomful of different laptops have to work.

---

## Prerequisites

Once your computer is set up (Node working, `npx wrangler@latest --version` prints a number), do
these once before deploying:

| # | Prerequisite | How |
|---|---|---|
| 1 | **A Cloudflare account** (free tier is fine) | Sign up at cloudflare.com |
| 2 | **Your domain added to Cloudflare** | Add the site in the dashboard, then update your domain registrar's **nameservers** to the two Cloudflare gives you. ⚠️ This is the one-time manual step. It can take a few hours to take effect. |
| 3 | **Log Wrangler into your account** | `npx wrangler@latest login` — opens a browser once to authorize. (This is simpler than creating an API token; do this and you're authenticated for every command.) |
| 4 | **Your two folders ready** | `llm/` = the bot HTML pages. The Worker code = a single `.js` file (the router). |

> The nameserver step (#2) is the *only* part that isn't CLI. It happens **once per domain, ever** —
> not on every deploy. After that, everything is `npx wrangler@latest …`.

> 🔎 **Confirm you're logged in** any time with `npx wrangler@latest whoami` — it prints your account
> name and ID.

---

## Step 1 — Deploy the bot pages to Pages

From the folder that contains your `llm/` directory:

```bash
npx wrangler@latest pages deploy ./llm --project-name=my-llm-site
```

- First run creates the Pages project and prints a URL like `https://my-llm-site.pages.dev`.
- **Copy that URL** — the Worker needs it in the next step.
- **No custom domain needed here.** The `.pages.dev` URL is internal plumbing the Worker uses.

Re-deploy any time you change the bot pages by running the same command again.

> ✅ **Tested.** On a clean terminal with a browser login, this command authenticated with no
> friction and went straight to the normal "create this project?" prompt — the exact student
> experience. (It only failed inside an environment that had a leftover API token; see the
> instructor note above.)

---

## Step 2 — Write the Worker config (`wrangler.toml`)

Create `wrangler.toml` next to your Worker `.js` file. This is what binds the Worker to your real
domain — no dashboard needed.

```toml
name = "aso-router"
main = "worker.js"
compatibility_date = "2026-01-01"

# Bind the Worker to your apex domain with a ROUTE (not a Custom Domain).
# A route sits IN FRONT OF your existing DNS record — so when the Worker calls
# fetch(request) for humans/Google, the request still flows through to your real
# site (Vercel, etc.). custom_domain=true would DELETE that record and make the
# Worker itself the origin, leaving human traffic with nowhere to go — the site
# would break. Use a route.
routes = [
  { pattern = "yourdomain.com/*", zone_name = "yourdomain.com" }
]
```

> ⚠️ **Prerequisite for the route to work:** your domain must already have a
> **proxied** (orange-cloud) DNS record pointing at your human site — for a Vercel
> site, a `CNAME` for the apex/`www` at `cname.vercel-dns.com`, proxied through
> Cloudflare. When students moved their domain to Cloudflare during setup, Cloudflare
> imported this record automatically; the route runs in front of it. If the human site
> ever 522/523s after deploy, that proxied origin record is what to check first.

In your `worker.js`, make sure the Pages URL from Step 1 is the address it fetches the bot pages
from, e.g.:

```js
const seoSiteUrl = 'https://my-llm-site.pages.dev' + url.pathname;
```

---

## Step 3 — Add the Worker's secrets

If your Worker uses any API keys or tokens (for analytics beacons, etc.), set them from the CLI.
These are stored encrypted by Cloudflare and never live in your code.

```bash
npx wrangler@latest secret put AIREFS_API_KEY
npx wrangler@latest secret put BOT_BEACON_URL
npx wrangler@latest secret put DASHBOARD_AUTH_TOKEN
```

Each command prompts you to paste the value. Secrets are **not** deleted by future deploys — set
them once. Skip any your Worker doesn't use.

---

## Step 4 — Deploy the Worker

```bash
npx wrangler@latest deploy
```

That's it — the Worker is now live at `yourdomain.com`, routing humans/Google to your site and AI
bots to the Pages bot site. Re-run `npx wrangler@latest deploy` any time you change the router logic.

> ✅ **The deploy flow is tested.** Deploying `worker.js` via `npx wrangler@latest deploy`
> was verified — upload to live in ~3 seconds, the User-Agent routing logic ran correctly, and
> the worker was cleanly removed afterward. The CLI flow is confirmed, not theoretical.
>
> ⚠️ **Still verify on a real Vercel origin before class.** The one thing to confirm live is
> that a *human* request passes through to the actual human site (not just that the routing
> branch fires). That only works with the **route** config above and a proxied origin DNS
> record in place (see the Step 2 note). Do a real `curl -A "Mozilla" https://yourdomain.com`
> against a domain whose human site is on Vercel and confirm you get the Vercel page, not an error.

---

## The whole thing, start to finish

**One-time setup (per machine):**

```text
0a. Install Node.js              → https://nodejs.org (LTS), restart terminal
0b. Ask Claude: "set up the Cloudflare developer tools"
       → Claude runs:  claude plugin marketplace add cloudflare/skills
                       claude plugin install cloudflare@cloudflare
0c. In Claude:  /reload-plugins
0d. Point your domain's nameservers at Cloudflare (dashboard, once)
```

**Deploy (the repeatable part — Claude runs these, OAuth pops a browser the first time):**

```bash
# 1. Ship the bot pages
npx wrangler@latest pages deploy ./llm --project-name=my-llm-site

# 2. (first time only) set secrets
npx wrangler@latest secret put AIREFS_API_KEY
# ...repeat for each secret your worker uses

# 3. Ship the router
npx wrangler@latest deploy
```

---

## What's CLI vs. manual — the honest summary

| Task | CLI? |
|---|---|
| Install the CLI | ✅ none needed — `npx wrangler@latest …` runs it on demand |
| Deploy bot pages (Pages) | ✅ `npx wrangler@latest pages deploy` |
| Deploy the Worker/router | ✅ `npx wrangler@latest deploy` |
| Bind Worker to your domain | ✅ via `routes` in `wrangler.toml` |
| Set secrets | ✅ `npx wrangler@latest secret put` |
| Re-deploy after edits | ✅ same commands |
| **Point domain at Cloudflare (nameservers)** | ❌ one-time dashboard/registrar step |
| **Custom domain for Pages** | ❌ dashboard-only — **but we don't need it** |

The two manual items are both either one-time-ever (nameservers) or not-needed (Pages domain). So in
practice: **set it up once, then everything is the command line.**

---

## Troubleshooting

- **`npx: command not found` or `node: command not found`** → you don't have Node.js installed (or
  your terminal wasn't restarted after installing). Go back to **"Setting up your computer → Step
  A.1"** and install Node from https://nodejs.org, then **close and reopen your terminal**.
- **`npx wrangler` hangs or errors the first time** → it's downloading Wrangler on first use; give it
  a few seconds and a working internet connection. If it fails, run `npm cache clean --force` and try
  again.
- **"In a non-interactive environment… set CLOUDFLARE_API_TOKEN"** → you're not logged in. Run
  `npx wrangler@latest login` (prerequisite #3) and authorize in the browser.
- **"Authentication error [code: 10000]" or "Unable to get membership roles" — especially on Pages
  commands while Workers commands work** → you have a *stale Cloudflare API token* conflicting with
  your browser login (see the instructor note above). Fix: `npx wrangler@latest logout`, then
  `npx wrangler@latest login`, and approve **every** permission on the consent screen. This is an
  instructor/experienced-user problem, not something a clean-laptop student will see.
- **`deploy` says "no route" / domain not found** → your domain's nameservers aren't pointed at
  Cloudflare yet (prerequisite #2), or DNS hasn't propagated. Wait, then retry.
- **Bot pages show but humans get an error (or vice versa)** → check the `.pages.dev` URL hard-coded
  in `worker.js` matches the project name from Step 1.
- **Secret values aren't taking effect** → confirm with `npx wrangler@latest secret list`; re-run
  `npx wrangler@latest secret put` for any missing.
- **Want to see it's live** → these two commands should return different pages:
  ```bash
  curl -A "GPTBot"  https://yourdomain.com    # should return the BOT page
  curl -A "Mozilla" https://yourdomain.com    # should return the HUMAN site
  ```

---

*Setup confirmed current as of June 2026. The one CLI gap — attaching a custom domain to a Pages
project — is an open Cloudflare feature request (workers-sdk #11772) and does not affect this
architecture, since the bot Pages site is reached by its internal `.pages.dev` URL.*

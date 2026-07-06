# Classes — Series Outline

A six-class, hands-on series on building and shipping real software with AI. The
through-line: you're not learning to code — you're learning to **delegate to
Claude Code like you would a person**, and ship live, deployed things in one
sitting.

**Audience:** non-engineers / operators who want to build and ship without
writing code by hand.
**Tools backbone:** Claude Code, Git/GitHub, Vercel, plus class-specific tools
(Supabase, MCP servers, StratEngine).

| # | Title | Status | Theme |
|---|-------|--------|-------|
| 1 | How to Build a Website | ✅ Built | Zero → live deployed website |
| 2 | How to Build a Dashboard | ✅ Built | Real data → decision-oriented dashboard |
| 3 | SEO + AEO | ⬜ To build | Get found by search engines *and* AI answers |
| 4 | Automations | ⬜ To build | Make work happen without you |
| 5 | Agents | ⬜ To build | Build software that acts on its own |
| 6 | Go-To-Market (GTM) | ⬜ To build | Sell it — powered by StratEngine |

---

## Class 1 — How to Build a Website ✅

**Promise:** A live website on a real URL by the end of class. No coding required.

**Arc:**
1. **The mindset shift** — stop using a tool, start delegating to a person.
2. **The four tools** — Claude Code, VS Code, GitHub, Vercel, and what each does.
3. **Setup, live** — one prompt installs everything; verify the terminal works.
4. **Specialist Claudes** — creating agents; making code-review and
   security-review automatic.
5. **Permanent instructions** — what `CLAUDE.md` is; global vs. project.
6. **Backup + history** — GitHub as "Google Drive for code"; the six git words.
7. **Hosting** — Vercel: free hosting that auto-deploys on push.
8. **Connect the three** — Claude + GitHub + Vercel talking to each other.
9. **Local vs. push** — local = practice, push = publish.
10. **Make it beautiful** — Claude codes it, `/impeccable` makes it look good;
    give it context, review from the outside in.
11. **Build the rest of the site** — standard pages; steal the page list from
    competitors' nav bars.
12. **Treat it like a real site** — get a real domain, set up a backup branch.

**Status:** Deck + prerequisites site built and deployed.

---

## Class 2 — How to Build a Dashboard ✅

**Promise:** A live dashboard that fits the way *you* make decisions.

**Arc:**
1. **End first** — show the finished decision tool vs. a generic report.
2. **You already did the hard part** — prereqs handled the plumbing.
3. **Two data sources** — Google Analytics (the recorder) vs. Supabase (the
   storage), and what each is for.
4. **MCP server** — how Claude actually operates Supabase.
5. **Plan mode** — let Claude plan before it builds (new habit).
6. **Reference docs** — a "Wikipedia for your project"; plan doc during, the
   architecture doc at the end.
7. **Data pipeline first** — build the data, *then* the dashboard. (The thing
   people get backwards.)
8. **Databases in plain terms** — a database is just labeled spreadsheets.
9. **The bridge** — a serverless function that pulls analytics into the
   database, on demand or scheduled.
10. **Build the pipeline + prove it works.**
11. **Part 2: design** — new session, `/impeccable init`, now you design.
12. **Build a decision tool, not a report** — invent synthetic metrics GA
    doesn't give you; iterate from rough to right.
13. **Ship + protect** — deploy to a live URL; password-protect it
    (Vercel password or a real login); optionally put it on a subdomain.

**Status:** Deck built. Prerequisites site built (due 1 week before class).

---

## Class 3 — SEO + AEO ⬜

**Promise:** Get the site you built found — by search engines *and* by AI
answer engines (ChatGPT, Perplexity, Google AI Overviews).

**Core technical concept (already drafted):** a **dual-surface site** — the
normal human site for people and Google, plus a separate **bot surface** of
pages tuned for AI crawlers. A Cloudflare **Worker** silently swaps in the bot
version of each page when an AI crawler hits the normal domain; the bot never
sees a different URL (avoids cloaking/origin-leak risk). Hosted on Cloudflare's
**free** tier (stronger security than Vercel Pro, $0). Students don't memorize
the commands — they ask Claude to run them, so the key prep is giving Claude
accurate, current Cloudflare knowledge.

**Reference docs already written (in this repo):**
- `cloudflare-llm-hosting-setup.md` — standing up the dual-surface site on
  Cloudflare from the CLI (the free + more-secure path).
- `dual-web-setup-directions.md` — adding the bot surface + Worker routing to a
  site that already has a human surface (setup/scaffolding only; page-content
  generation is a separate command).

**Likely full arc (to design):**
- Why SEO and AEO are now two jobs, not one.
- The dual-surface mental model: human pages, bot pages, the routing Worker.
- Setup, live: wire it on Cloudflare via Claude (one-time DNS step aside).
- Technical SEO basics the build needs (sitemaps, schema, meta, CWV).
- On-page: answer-first content, headings, internal linking.
- AEO / GEO: llms.txt, citability, structured data, getting cited by AI.
- Generating the bot-page content (separate from the routing setup).
- Measuring it: what to watch and where.

**Available tooling to lean on:** the `claude-seo:*` skill + agent suite
(seo-audit, seo-geo, seo-technical, seo-schema, seo-content, etc.), the
`blog`/`blog-geo`/`blog-schema` skills, and the `cloudflare` /
`workers-best-practices` / `wrangler` skills.

**Status:** Prereqs deck built (`class-3-seo-aeo/prereqs.html`) + Cloudflare
student kit (`class-3-seo-aeo/cloudflare-student-kit/`, published to
`class-materials`). Main class deck first pass built
(`class-3-seo-aeo/index.html`, 15 slides: framing → two work habits (plan mode,
reference docs) → dual-surface mental model → live build → AEO + measure) and
linked from the landing hub. Two setup reference docs drafted; the CLI hosting
doc's Worker binding was corrected from a Custom Domain to a **route** so human
traffic still passes through to the Vercel origin.

---

## Class 4 — Automations ⬜

**Promise:** Make routine work happen without you — scheduled and triggered.

**Likely arc (to design):**
- What an automation is vs. an agent (set rules vs. judgment).
- Triggers: schedule (cron) vs. event-driven.
- Building one with Claude Code: serverless functions + a schedule.
- Connecting services (the dashboard pipeline from Class 2 is a first example).
- Notifications / delivery (email, Slack, etc.).
- Reliability: logging, retries, knowing when it broke.

**Status:** Not started.

---

## Class 5 — Agents ⬜

**Promise:** Build software that acts on its own — makes decisions, uses tools,
handles judgment, not just fixed rules.

**Likely arc (to design):**
- Agent vs. automation: when judgment is required.
- Anatomy of an agent: instructions, tools, loop.
- Building one (Claude Agent SDK / subagents pattern from Class 1's
  "specialist Claudes").
- Giving it tools (MCP) — extends the Class 2 MCP concept.
- Guardrails, review, and keeping a human in the loop.

**Status:** Not started.

---

## Class 6 — Go-To-Market (GTM) ⬜

**Promise:** Take what you've built and sell it — using **StratEngine** to drive
the go-to-market motion.

**Likely arc (to design):**
- From product to market: positioning, audience, offer.
- Using StratEngine to plan and run the GTM.
- Channels: content, outbound, the site/SEO/AEO from earlier classes.
- Measuring with the dashboard from Class 2.

**Status:** Not started. Built on StratEngine.

---

## Series threads (what carries class-to-class)

- **Delegation mindset** (Class 1) underpins everything.
- **CLAUDE.md + specialist agents** (Class 1) → reused and deepened in Agents
  (Class 5).
- **MCP servers** (Class 2) → expanded in Agents (Class 5).
- **The deployed site** (Class 1) → instrumented (Class 2), found (Class 3),
  and sold (Class 6).
- **Serverless + scheduling** (Class 2 pipeline) → generalized in Automations
  (Class 4).
- Every class ships something **live and deployed** by the end.

---

## Repo / deploy notes

- This repo holds the class decks + the `index.html` class hub.
- See the two-repo setup: private deploy repo → Vercel, public student repo →
  `class-materials`. (memory: classes-two-repo-setup)
- Each class has its own `class-N-*/` directory with `index.html` (deck) and,
  where relevant, a `prereqs.html` due ~1 week before.

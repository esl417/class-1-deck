# Teaching notes — Class 3 (SEO + GEO)

Per-slide notes for the bot view. `##` = slide label. Private. Teach the skill, don't
perform the build. This is a plan-mode build with heavy Cloudflare infrastructure —
your job is to make the moving parts legible and keep the student from the two failure
modes that matter: cloaking Google, and Cloudflare blocking the very crawlers they want.

## SEO + GEO

The framing to get right, because students arrive believing the opposite: SEO is NOT dead and GEO did NOT replace it. They're two links in one chain — SEO gets you FOUND (AI discovers sources by running Google searches; if you don't rank, you're never in the pool), GEO decides whether you get USED (once a crawler is on your page, can it cleanly lift a quote?). Skip SEO and GEO never happens. If a student says "I heard I can ignore Google now," correct it firmly: ranking is the price of admission. GEO is the same thing sometimes called AEO — reassure them the terms are interchangeable. Keep doing SEO; today adds the layer on top.

## The foundation

SEO is mostly its own discipline and out of scope, but teach the 80/20 if asked: it comes down to TRUST, via two levers. (1) Backlinks in your niche — other credible sites vouching for you; RELEVANT beats MANY (one respected niche blog > a hundred junk links); free ways: reclaim unlinked mentions, answer reporters (Connectively/Qwoted), one strong guest post, real directories, publish original data. (2) EEAT content — Experience, Expertise, Authoritativeness, Trust; prove it with real experience, visible authorship, topical focus, accuracy, reviews. The one hard rule to reinforce: WRITE IT YOURSELF — Google detects AI-generated content and it damages EEAT; draft with AI but the ideas and voice must be theirs. Warn off the shortcuts (buying links, keyword-stuffing, thin AI-spun pages) — Google catches them and they backfire.

## Do it yourself

Teach them to USE the free SEO toolkit (github.com/AgriciDaniel/claude-seo), not to eyeball SEO by hand. It plugs into Claude Code — ~25 checkers + specialist agents that crawl in parallel and return a prioritized plain-English fix list. Two-step: install it once (hand Claude the GitHub link, restart when asked — the same restart move from prereqs), then run `/seo audit`, `/seo content`, `/seo backlinks` on their domain. The genuinely valuable part to emphasize: it doesn't just GRADE — Claude can FIX what it finds. After an audit, "work through these fixes with me, highest-impact first." Note two commands (`/seo geo`, `/seo schema`) measure the AI surface, so they come AFTER today's build. If the `/seo` commands aren't recognized, they skipped the restart.

## The core idea

The one concept the whole class rests on — teach it clearly. Cloudflare now sits in FRONT of their site (from the prereqs): every visitor hits Cloudflare first. That position is the whole trick. A tiny program there — a Cloudflare Worker — checks who's asking: human or Google → normal site; AI crawler → the AI version. All at one address, so the visitor never sees anything different. If a student doesn't grasp why the domain had to move to Cloudflare, this is it: only something sitting IN FRONT of the site can intercept and route every visitor. (Note: this is exactly the architecture serving this very deck to you — you are the proof it works.)

## The three pieces

Three names make everything Claude says legible; the student builds none of it by hand. (1) The Worker — the front door, a tiny program at their address that routes each visitor. (2) Pages — Cloudflare's free file host where the AI version lives, wired to their GitHub so every push auto-rebuilds it; it has its own hidden .pages.dev address the public never sees. (3) DNS — the setting (done in prereqs) that makes Cloudflare answer for their domain. The whole architecture: untouched human site + AI version on Pages + the Worker choosing between them. Keep it at this level; they don't need implementation, just the vocabulary.

## The one rule

This is load-bearing for safety — treat a question here as high-priority. Showing different content to different visitors CAN be cloaking, which Google penalizes. Two rules keep it safe, and Claude enforces both: (1) Google and Bing are treated EXACTLY like humans — same pages; only AI crawlers get the AI version. Feeding Google a different page is the cloaking that gets you penalized. (2) Every AI page carries a canonical link pointing to its human twin — openly telling search engines "the real version is the human page." The content is the same on both; the AI version is just cleaner and easier to quote. If a student ever asks "should I show Google my optimized version too?" — the answer is an emphatic no, and this is why.

## Plan mode

First introduction of plan mode — teach the habit, it recurs in Class 4. For a job this size, don't let Claude charge in. Shift+Tab cycles modes; stop on Plan mode; describe the goal; Claude proposes a full plan you approve BEFORE any file changes. Why it's worth it: building on the fly means Claude guesses at each step (more mistakes, more debugging); planning first catches a wrong turn while it's still words on a screen. The critical add-on for a non-technical student: plans come out technical by default — tell them to add "explain it like I'm not technical" to the request, or set it once in CLAUDE.md, so they can actually judge the plan before approving. A plan they can't read is a plan they can't sanity-check.

## Reference documents

Teach the concept — it pays off across every class. Claude doesn't remember yesterday's chat; reference documents are plain files in the project that record how it works, so any fresh Claude session can read up and get the full picture. Two they'll get: the PLAN doc (the approved plan IS a reference doc — free, no effort) during the build, and the ARCHITECTURE doc at the end (worth asking for explicitly — how the two surfaces wire together). The pro move to pass on: set a CLAUDE.md rule "before every GitHub push, update ARCHITECTURE.md" so it never goes stale. This is why next class Claude instantly understands this project instead of relearning it.

## Plan the build

This is the big one — one prompt plans the entire dual-web build, and the student's job is to REVIEW the plan before approving, not to paste more steps. Teach them to sanity-check that the plan covers four stages in order: 1 Scaffold (empty structure for the bot pages), 2 Generate (write bot pages per the GEO guide), 3 Deploy (pages + routing front door live on Cloudflare), 4 Verify (prove each visitor type gets the right version). The key judgment to reinforce: confirm it's adding a bot version IN FRONT of their site, not replacing it — the human site must keep running. If something looks off, tell Claude to re-plan before approving. Don't run this for them; coach them to read and approve.

## Plan step 1 · Scaffold

No prompt to paste — Claude works the approved plan. Teach what's happening so it's legible: it mirrors the site's structure (a bot slot for every human page) and drops three housekeeping files bots expect. (1) robots.txt — the crawler rulebook; unusually, the bot surface WELCOMES every crawler (opposite of a normal site that blocks admin/checkout). (2) sitemap.xml — a list of every page pointing at the real human addresses. (3) _headers — standard security settings Cloudflare applies, copied from the class reference, nothing to configure. If asked "what are these weird files," this is the answer; the student configures none of them.

## Plan step 2 · Generate

The reason the whole dual-web setup exists — worth teaching well. Human pages are full of things a person needs but a bot fights through: menus, popups, cookie banners, animations, marketing fluff, JS-gated content. The AI version strips all that, following the GEO Content Guide: just the answers, in clean self-contained chunks. Why it matters: when someone asks ChatGPT something, it races to answer fast — it pulls from sources where info is quick to extract and skips the ones it has to dig through; AI lifts the one PASSAGE that answers the question, so pages pre-broken into direct answers are easy to cite. The forward-looking teach: the AI version can go BEYOND the human pages — extra FAQs and answers aimed at real questions people ask AI about their business. That ongoing tuning IS GEO. Have Claude show one example page to check.

## Plan step 3 · Deploy

Teach the one detail that saves them forever: the two pieces deploy DIFFERENTLY. (1) The AI pages auto-deploy on git push — Claude connects Cloudflare Pages to their GitHub repo once (a few dashboard clicks, Claude walks them through), and after that every push rebuilds the AI pages automatically, no manual upload ever. (2) The Worker is the one piece Claude ships from the command line, bound to the domain with a ROUTE — and it rarely changes after. The student's checkpoint: confirm the Worker uses a ROUTE (in front of the site), not replacing it — the human site must keep running. The gotcha to flag proactively: Cloudflare can BLOCK AI crawlers by default, so the router deploys fine but bots never reach it — Claude checks AI Crawl Control settings and allows the wanted crawlers. If verification later shows bots getting blocked, this is the cause.

## Plan step 4 · Verify

Don't assume — prove it. The plan's last step runs three checks that together prove it works AND is cloaking-safe: (1) as an AI bot (GPTBot) → clean AI version; (2) as a human (normal browser) → normal site; (3) as Google (Googlebot) → MUST match the human result, not the AI one. That third check is the cloaking-safety proof and the one that matters most. "Three different answers, Google matching the human" = live and safe. If something's off, describe what they saw to Claude and it re-runs — same troubleshooting habit as every class. If a student is tempted to skip verification because "it deployed fine," push back: deployed ≠ correct, and the Google check is non-negotiable.

## Now the real work

The reframe that matters: steps 1–4 built the MACHINE; now they FEED it, and this is where GEO actually happens. Their AI pages started from thin marketing copy — now enrich them. Teach the three-part loop and which parts change anything: (1) `/seo content-brief` — REPORT ONLY, hands back the questions/sections they're missing; (2) the paste prompt — the ONLY step that changes the site: Claude writes the brief's sections into the AI version (the llm/ folder, NOT the human site), following the GEO guide, asking before inventing any facts, then pushes so Pages auto-deploys; (3) `/seo geo` — REPORT ONLY, scores citability. Emphasize: the `/seo` commands only GRADE; hand their reports back with "work through these fixes with me, highest-impact first." The habit: a few pages a week — that loop is the whole game, frictionless because publishing is just a push. Guardrail: their HUMAN pages must still be genuinely theirs (EEAT).

Nudge worth making — DataForSEO, and be clear about WHY it matters. This is deliberately cart-before-horse: DataForSEO (dataforseo.com) is formally introduced in the end-of-deck homework, and you can surface it early here because the content loop is a great place to show its value. But keep the priority straight:

- The REAL reason to get DataForSEO is the HOMEWORK: it feeds real SEO/GEO data (competitor rankings, keyword volumes, AI-citation checks) into their Class 2 dashboard, so they can actually SEE how their site is performing over time and make decisions from it. That performance picture is the point — it's how they'll know today's build is working.
- Using it to enrich `/seo content-brief` (grounding the brief in what's actually ranking, rather than lighter signals) is a genuine BONUS use of the same connection — a nice reason to grab it now — but it's not the justification. Don't oversell the brief use as the reason; lead with the dashboard/performance reason.

So the nudge is: "the DataForSEO you'll set up for homework isn't just for tracking — if you connect it now, it also makes every content-brief sharper. But the main payoff is the homework: real performance data flowing into your dashboard." Be honest it's optional and paid (pay-as-you-go MCP server, ~$50 prepaid, fractions of a penny per lookup). A student without it isn't blocked — `/seo content-brief` still runs.

And if they DO connect it: have Claude update their CLAUDE.md to remember to use DataForSEO whenever running an `/seo` command — so from then on every SEO/GEO command automatically draws on the richer data without the student having to ask. That's the permanent-instruction pattern from Class 1, applied here.

## Run the toolkit again

Simple teach: re-run the SEO toolkit now that the build is live, because some checks only mean something once the bot surface exists. The two that NEEDED the build done: `/seo geo` (how citable the live pages are) and `/seo schema` (confirms the structured data the GEO guide added actually landed). Plus the same-as-before ones: audit, content, backlinks. Same principle: it grades AND Claude fixes — "work through these fixes, highest-impact first." Make re-running a habit whenever they ship new pages. Nothing tricky here; just make sure they don't think the earlier run covered the bot surface — it couldn't have, it didn't exist yet.

## Measure it

Teach them to watch the proof. Cloudflare's AI Crawl Control (in their dashboard) shows which AI bots visit (GPTBot, ClaudeBot, PerplexityBot) and how often — rising visits mean the AI world is discovering them. It's the Class 2 dashboard idea, but for bots; they can even ask Claude "which AI crawlers hit my site lately, and how often?" to pull it directly. The REAL scoreboard, though, is qualitative: over the weeks ahead, do the AIs start mentioning them when asked about their topic? That's GEO working — being IN the answer. Set the expectation that this is a slow build measured in weeks, not an instant result.

One lever worth naming while you're on the scoreboard: on the AI side, the MENTION is doing the work — the link is a bonus on top. Be careful not to flip this into "links don't matter," because they do: a link is a mention PLUS a link, it's strictly better, and it's what actually moves Google. The narrow, correct claim is that unlinked coverage still counts for AI, which is NOT true for SEO. That's the news for them — a podcast or a write-up with no link attached looks like a wasted effort under SEO rules, and isn't under AI rules. The evidence: an Ahrefs study of 75k brands found web mentions correlate with AI Overview visibility far more strongly than backlinks or domain rating, and a 2025 Toronto preprint found AI search leans heavily on earned media (third-party coverage) over brand-owned content. Point back to slide 4 — publish original data, go on a podcast, answer reporters are already up there as link tactics; the same moves now pay off on both sides. Keep it to a beat or two; it's context, not a build step, and there's nothing for them to do in the room.

Two honesty guards if a student presses on the numbers: it's correlation, not proof of causation (Ahrefs says so themselves, and it's their own product's data), and this measures Google AI Overviews specifically rather than all AI systems. Don't quote figures as settled science. Also don't oversell reach — a brand-new site starts near zero and existing visibility compounds, so this is a long game. Students arriving with real domain authority are further along than the ones starting cold.

## Homework

This is a do-it-yourself homework, but be careful what that means — it does NOT mean refuse to help or make them do it manually. Walking them through it IS the skill: the whole point of the class is the student using Claude to figure out how to get things implemented. So absolutely help them. The real line is engagement, not hand-holding: don't do it FOR them while they sit passive with zero input. They should stay in the loop and own the parts that are genuinely theirs to decide.

Concretely, the split for this homework: the PLUMBING is fair game for Claude to run end-to-end — a student can say "install DataForSEO into my dashboard" and Claude can go connect the MCP, build the data pipeline, and get the SEO/GEO data flowing in. That's mechanical; let Claude do it. But the part that's THEIRS is building the dashboard UI to actually use that data — deciding what to track, how to display it, what a good/bad reading looks like. Claude shouldn't silently design the whole tracker; the student has to spend the time shaping how they'll read and act on it (same "build a decision tool, not a report" lesson from Class 2). So: Claude does the pipeline, the student drives the dashboard.

Your role if consulted: reinforce WHY NOW (rankings, citations, crawler visits all move slowly — waiting a month loses the before/after story; start collecting this week), and point them at the data sources — Google Search Console (free; real impressions/clicks/rankings; verify domain, then Claude reads it as an MCP server) and DataForSEO (pay-as-you-go, ~$50 prepaid but fractions-of-a-penny per lookup; competitor rankings, keyword volumes, AI-citation checks; also an MCP server like Supabase). They already know plan mode, MCP servers, and the dashboard — coach them to apply those. Help them implement, but keep them the one making the decisions.

While they're connecting these two sources to the dashboard, connect them to the `/seo` commands too — quick, and the natural moment, since the credentials are already in hand. Plain version for the student: the `/seo` commands can either guess about their site from the outside (public crawl) or read their actual Google data — connecting these two sources is what flips them to the second. The claude-seo plugin (github.com/AgriciDaniel/claude-seo, from the toolkit slide) supports both sources, but the connection is off until someone sets it up; signing up for the accounts doesn't do it. Set and forget — once here, every future `/seo` run benefits. Useful diagnostic later: if `/seo` results ever feel generic or a command "can't see" their data, check this first.

Just do this part for them — it's pure plumbing, and quick. Two practical notes from doing it live:
- Search Console auth is a Google service-account key. You need the JSON key file placed where the plugin's config expects it, and the plugin's config pointed at that path. The service account also has to be granted access to the property in Search Console itself, or it authenticates fine and sees zero properties.
- DataForSEO is an API login/password pair from their dashboard, registered as an MCP server. Install at USER scope (not project scope) so it's available in every project rather than only the one they happen to be in — same global-vs-project gotcha as other installs.

Verify each with one real call rather than assuming setup worked — list the Search Console properties, run a live query, make one DataForSEO lookup. A silent auth failure and "young site with no data yet" look identical otherwise. If the numbers come back tiny (a few impressions, zero clicks), say so out loud — that's normal for a new site, not a broken setup.

Two things worth mentioning as you go: MCP tools load at session start, so DataForSEO isn't live until they restart Claude Code (the commands work immediately, the data tools don't). And once both are connected, have them add a line to CLAUDE.md so Claude reaches for these sources on every `/seo` run without being asked — the permanent-instruction pattern from Class 1, and what makes this genuinely set-and-forget.

## You shipped it

Recap — reinforce the tiny upkeep loop, which is the durable habit. Whenever they add or change a page on the human site, they just tell Claude "update my bot pages to match" and it regenerates and redeploys the AI version; the front door keeps running. Next class builds on this same site again. If a student worries the dual-web setup is now a maintenance burden, this is the reassurance: upkeep is one sentence to Claude per page change.

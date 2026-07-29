# Teaching notes — Class 2 (Dashboard)

Per-slide notes for the bot view. `##` headings match slide `data-label`s. Private —
never served on the human deck. Teach the skill; don't just perform the tool. The one
recurring hazard this class: unverified data. Always push the student to prove real rows
landed before trusting anything downstream.

## No real data yet?

This is the escape hatch that keeps a student from being blocked, and it's worth surfacing early if their analytics is empty. The situation: their Google tag was installed late (or not at all), so there's no real traffic to chart yet. The fix is the sample-data kit — ~90 days of practice data shaped exactly like real GA4, so the dashboard they build today just works when real data starts flowing later, nothing to rebuild.

Two things to get right: (1) the sample kit needs the Supabase connection working first — if Supabase isn't connected, fix that before loading dummy data; (2) reassure them this isn't a lesser path — because the shape matches, everything they build is real and permanent. If a student is discouraged that "my numbers are empty," this is the slide that unblocks them.

## What is an MCP server?

First real encounter with MCP — teach the category, because MCP recurs (Supabase here, DataForSEO in Class 3, more in Class 4). The mental model on the slide is the right one: an MCP server is a remote control Supabase hands Claude — labeled buttons it can actually press (create tables, run queries) rather than just describing what to do. Without it, Claude can only talk; with it, it acts.

The "isn't that just an API?" question is worth answering cleanly if asked: an API is the raw machinery; an MCP server is a standard wrapper around it built so an AI can use it reliably without custom wiring — a universal remote. Don't over-explain; the student never has to build one, just understand that this is how Claude gets hands-on access to a real service. If they hit "Claude can't do anything in Supabase," the cause is usually the MCP server not connected/authenticated (the prereqs restart-and-auth step).

The bigger, reusable lesson to teach here — don't let it stay about Supabase alone: ANY service that offers an MCP server OR an API can work with Claude and have its data pulled in. Supabase is just the first example. So if the student uses other tools — a CRM, Stripe, their email platform, a project tracker, anything — the move is the same: have Claude check whether that service exposes an MCP server or an API, and if it does, Claude can ingest from it or act on it. Frame it as a capability they now own: "got a service you want in your dashboard? Ask Claude if it has an MCP or an API — if it does, we can wire it in." This turns today's one-off connection into a pattern they can apply to their whole stack as needs arise.

## Build order

This is the one concept people get backwards, so treat a question here as important. The rule: build the DATA pipeline first, prove it, THEN design the dashboard — in a fresh session. The instinct is to start with the pretty charts, but a dashboard is just a window onto data; if there's no data yet, you're designing around numbers that don't exist and guessing.

If a student wants to jump straight to dashboard design, gently hold them to data-first: "let's confirm real rows are flowing before we design what shows them — otherwise we're guessing at the numbers." This ordering is the backbone of the whole class; everything downstream assumes the data layer is proven.

## What a database is

Concept slide — teach it plainly if asked, don't drill it. The whole mental model: a database is just labeled spreadsheets. A table = a spreadsheet with named columns and rows (a `daily_traffic` table: date, visitors, signups, one row per day). The key reassurance for a non-technical student: they never touch it directly — Claude creates the tables, fills them, reads from them. They just say what they want stored. If a student is intimidated by the word "database," this analogy is the entire fix. Don't go deeper than tables-are-spreadsheets.

## The bridge

Teach what the pieces ARE so the student can follow what Claude builds, without getting into implementation. Two concepts: (1) a serverless/edge function is a little robot program that runs without a computer of their own to host it — it fetches numbers from Google Analytics and drops them in their database, on a schedule or on demand; (2) the service account (set up in prereqs) is the credential — essentially an email address Claude uses to read their analytics — that lets the robot cross from Google into Supabase.

Don't teach them to write any of this; Claude does. The value is that when Claude says "edge function" or "service account," it's legible. If the pipeline fails to read analytics, the service-account credential is a prime suspect — check it was set up in the prereqs.

## Build & test the pipeline

The load-bearing instruction here is the LAST line of the prompt: don't just build the pipeline, TEST it and show real rows. This is the class's core discipline — never trust data you haven't seen land. "Done" means Claude shows actual rows of their real numbers in the table, and the job is scheduled. Do not let the student move on until they've seen real data.

Two coaching points: (1) reinforce the wording lesson — describe the GOAL ("ingest my GA metrics so my dashboard can read them"), not the how; they don't need to know about tables or functions. (2) If analytics is empty, the GA pull returns nothing — that's the moment to switch to the sample-data kit (see "No real data yet?") rather than debugging a pipeline that's working fine against an empty source. Empty result ≠ broken pipeline; check whether there's data at the source first.

After real rows land: STOP. The dashboard is a deliberately fresh session.

## A fresh start

Two things to reinforce. (1) Start CLEAN — a brand-new Claude session before running `/impeccable init` for the dashboard. The pipeline work is done; a fresh session gives sharper results (same session-hygiene lesson from Class 1). (2) `/impeccable init` here does the same job as in Class 1 — lays down PRODUCT.md and DESIGN.md — but the framing is different: this is a PRIVATE, internal dashboard only they see. No brand to match, no one to impress. Encourage them to actually enjoy it — pick a whole aesthetic (they'll look at it daily). Same teach-don't-perform rule as Class 1's Design brief: don't run init's interview for them; help them describe the vibe, then let the command do its thing. Plant the seed that this dashboard grows into their whole-business cockpit over the coming classes.

LIKELY GOTCHA — Impeccable not installed in this project. This is a new project folder (the dashboard), so if `/impeccable init` isn't recognized or the student says Impeccable "isn't installed," the almost-certain cause is that in Class 1 it got installed at the PROJECT level instead of globally — so it doesn't carry over to this new dashboard project. The fix is to install it GLOBALLY this time so it works everywhere from now on. Point Claude to install it globally from impeccable.style using npx — and when it asks "project or global?", choose GLOBAL (the whole point is that a global install follows them into every future project, so this never happens again). Fallback download options are at impeccable.style/#downloads. After installing, they may need to restart Claude Code for the skill to load. Don't debug it as if the command is broken — it's a scope/install issue, and global reinstall is the fix.

## Design around your decisions

This is the real value of the entire class, so slow down here. The point: don't build a REPORT (raw numbers, like GA's default screens), build a DECISION TOOL — organized around the decisions the student actually makes. Every number should say what it means and what to do about it.

The key branch: if the student knows the decisions they care about, have Claude build the screen that answers them. If they DON'T — which is most people, and totally fine — this is where Claude shines: have it SUGGEST the metrics worth watching for a business like theirs. Don't let a student stall on "I don't know what to track"; that's exactly the prompt on the slide. Whoever picks the metrics, hold the one rule: the dashboard must explain itself. This is teaching judgment about what's worth measuring — a durable skill, not a one-off build.

## Synthetic metrics

The pro move most people miss, and a genuinely valuable teach. Raw counts (500 visitors, 12 signups) say "what happened." Synthetic/derived metrics (signup RATE = 12/500 = 2.4%, week-over-week change, traffic-to-pricing ratio) say "is that good, and is it improving?" — each one argues for a decision. That's the difference between a dashboard that reports and one that tells you what to do.

Teach the student to ask Claude to propose derived metrics from their raw data, each with a one-line "what decision does this drive." Then they pick. This is a thinking skill — help them see that the insight usually lives in the numbers you BUILD from the raw ones, not the raw ones themselves.

## The build loop

Same "first pass is never right" loop as Class 1, with dashboard-specific twists worth calling out. (1) Tell Claude to build in Next.js, not plain HTML — an interactive dashboard needs it. (2) For a dashboard, "bolder" means CLEARER — stronger hierarchy, not louder colors; correct the student if they push for visual loudness over legibility. (3) It's an APP, not a page — encourage them to ask for drill-downs, filters, buttons that do things. (4) The critical final step: have Claude compare the dashboard's figures against native Google Analytics and confirm they match. A pretty dashboard with wrong totals is worse than none — this verification is non-negotiable, same discipline as proving the pipeline. Reinforce that it's a living tool, reshaped as they use it.

## See it update live

Teach the workflow win: run a LOCAL preview so changes appear instantly, instead of deploying to Vercel and waiting a minute per tweak. This is what makes the build loop feel fast. The one thing that matters in the prompt: "open it in my web browser" — without that phrase, the preview can open in a cramped panel inside VS Code; with it, full-size in their real browser. If a student complains the preview is tiny or awkward, that phrase is the fix. Leave the tab open while building; it refreshes itself.

## Deploy it live

Same ship-to-Vercel move as Class 1, with three things to flag. (1) This is a SEPARATE deployment from their Class 1 website — different project, different URL. That's expected; a student confused about "why isn't this on my website" needs that cleared up. (2) The moment it's live, anyone with the link can see their real business numbers — so locking it down is the immediate next step, not optional. Don't let a student share the URL before the next slide's password protection is on.

(3) LIKELY GOTCHA — no GitHub repo yet. Unlike Class 1, where the site was already pushed to GitHub before it ever went to Vercel, the dashboard folder they made in the prereqs is just a plain folder — no git, no remote. So this one prompt is doing more than it looks: Claude has to set up git, create a NEW GitHub repo, push the code, and only then connect Vercel. Expect it to pause for browser clicks (GitHub auth, authorizing Vercel's GitHub access, or confirming the new repo) — that is the normal path, not a failure. Tell a student this up front so the pause doesn't read as "the deploy broke." If Claude seems stuck, the usual cause is an un-granted GitHub permission in the browser, not broken code — have them describe what they see rather than hunting for a fix. Also worth saying plainly: a second repo is correct and good. Two separate projects, two repos, two deployments — the website and the dashboard should not live in the same place.

## Lock it down

This shows real business numbers, so it must not be open to anyone with the link — treat locking it as required, not optional. Two paths: (1) RECOMMENDED — Vercel's built-in Deployment Protection: flip it on, set one password, done, no code. For a dashboard only they look at, this is plenty. (2) Upgrade — a real login via Supabase Auth (the same Supabase they connected), for named accounts or sharing with a teammate; more to build but a true login, and it supports Google sign-in and passkeys too.

Steer most students to the Vercel password unless they specifically want named accounts or multiple viewers. If a student is about to share the dashboard, confirm the lock is actually on first.

## Where it lives

Genuinely optional, low-stakes — don't over-invest a student's time here. Their dashboard has its own Vercel URL, which is completely fine to just bookmark. If they own a domain and want a tidy address, they can point a subdomain (dashboard.theirdomain.com) at it. There's no wrong answer; as long as they can reliably get to it, they're done. Only help with the subdomain if they actively want it.

## If something breaks

Same troubleshooter habit as every class: describe what happened to Claude, don't go hunting. If a student reaches you here, be the payoff — read what they paste, name the likely cause, fix it. Class-2-specific likely causes worth checking: pipeline errors (service-account/analytics access, or empty source data), a blank dashboard (often a local-preview or build issue), deploy failures, or numbers that don't match GA (the verification step). Honor the last line: if they've tried a couple of times and are still stuck, it's fine to email Eric rather than lose their evening.

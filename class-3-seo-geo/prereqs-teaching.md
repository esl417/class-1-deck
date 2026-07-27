# Teaching notes — Class 3 Prerequisites

Per-slide notes for the bot view of the Class 3 PREREQS deck. `##` = slide label. Private.
Recovery-focused: the student is moving their domain to Cloudflare and arming Claude with
Cloudflare access. Two known landmines: the post-move SSL redirect loop (fix: Full (strict)),
and the Claude Code restart-and-resume during setup. Read the real error, fix the real cause.

## Step 1 · The domain move

Lead with the deadline and the reassurance. The domain move can take up to a DAY to settle, so it needs ~7 days of lead time to show Active before class — a student setting this up late needs to know that clicking through fast doesn't beat the propagation wait. The key reassurance that heads off panic: their WEBSITE doesn't move — it stays exactly where it is (Vercel, Squarespace, wherever); only "who answers for this address" changes to Cloudflare. If a student fears they'll take their site down by doing this, that's the fix.

## Step 1 · What Cloudflare is

Concept slide — teach plainly if asked. Cloudflare is free, trusted plumbing that stands in front of a site and answers every visitor first. For their visitors, NOTHING changes — same address, site, look. What it unlocks is the class's whole trick (serve humans the normal site, AI bots a version built for them), plus free bonuses: it shields the site (blocks attacks/bad bots, absorbs DDoS) and speeds it up (global caching). Cost is genuinely $0, no trial, no card. If a student is skeptical this is safe or free, this is the reassurance — a huge share of the internet already runs through it.

## Step 1 · Pick your path

The branch that determines everything downstream — make sure the student knows which path they're on. Path A: they OWN a real domain (yourbusiness.com pointing at their live site) → add it to Cloudflare and flip nameservers (next slides; ~10 min of clicks + a wait). Path B: they're still on a free .vercel.app address → the AI-bot trick CAN'T be done on .vercel.app, so they buy a real domain INSIDE Cloudflare (which skips the nameserver flip and the wait entirely — actually the faster path). Getting a real domain was Class 1's homework; Path B is the catch-up. If a student is unsure, ask: do you have a real domain that points at your site, or are you still on .vercel.app?

## Step 1 · Create the account

Mechanical: sign up at dash.cloudflare.com/sign-up, verify email, stay logged in. The only thing worth reinforcing: use an email they'll keep long-term — this account becomes the front door for their business's website. Nothing usually breaks here; if a student is stuck it's email verification not arriving (check spam, resend).

## Step 1 · Path A

The nameserver flip — the heart of Path A, and where clicks go wrong. Teach the concept plainly: nameservers are the internet's phone-book entry saying who answers for your domain; right now it names the registrar, they're changing it to say "Cloudflare answers now." The steps: in Cloudflare, Add a domain → choose "Connect a domain" (NOT Transfer or Buy — they're keeping the domain where it is), Free plan; Cloudflare imports existing settings — DON'T DELETE ANYTHING on the review screen, just Continue; Cloudflare shows two nameservers; then at their registrar, replace the existing nameservers with Cloudflare's two.

The specific thing most of them need: their registrar is usually VERCEL, so the flip happens at vercel.com/dashboard/domains → their domain → Nameservers → Edit → paste Cloudflare's two. If a student can't find where to change nameservers, ask where they bought the domain and point them at the right registrar. Then it's a wait (minutes to a day) for the Active email — nothing is broken during the wait, the site keeps running.

## Step 1 · Path B

Simpler path — buy a domain inside Cloudflare (Domain Registration → Register Domains, ~$10-12/yr at cost), and because it's bought there, it's active immediately with no nameservers to flip and no wait. Then connect it to their site: the paste prompt has Claude connect the new Cloudflare domain to their Vercel deployment. If a student on Path B is stuck, it's usually the connect-to-Vercel step — that's what the prompt handles, and Claude walks them through any clicks. Path B students are typically fully done with Step 1 in ~15 minutes.

## Step 1 · Confirm it worked

Verify, don't assume. Two checks: (1) Cloudflare dashboard shows the domain ACTIVE (also an email) — if still "Pending," it just hasn't finished settling, check back later, not broken; (2) visit the site in a normal browser — it should load exactly like before, same padlock, click a few pages. The critical thing to flag proactively: if the site breaks into a redirect loop or shows a security/SSL error right after the switch, that's the KNOWN gotcha with a two-minute fix (SSL/TLS mode → Full (strict)) — see the "If something breaks" slide. Don't let a student conclude they broke their site; this specific symptom has a specific, easy fix.

## Step 2 · Teach Claude Cloudflare

Teach what this grants and why the skills matter. In class the student types no Cloudflare commands — Claude does — so Claude needs two things ready: Cloudflare's OFFICIAL skills (its current, up-to-date instruction set, written by Cloudflare) and a logged-in terminal. What the student does is minimal: paste one message, restart the app once when asked, click Allow once in the browser. Why the skills specifically matter (worth saying): Cloudflare changes fast, so the official skills tell Claude the CURRENT correct way to use its tools instead of guessing from memory — this prevents a whole class of "Claude tried an outdated method" failures in class.

## Step 2 · The one message to paste

Setup: this happens in their WEBSITE project from Class 1 (the folder their site lives in) — that's where they build in class, so the right folder matters. The prompt pulls the Cloudflare kit and runs it. The important pre-warning, which the slide makes explicitly: expect Claude to pause twice — a restart of Claude Code partway through (the 🕐 resume-the-same-chat move from Class 2) and one Allow click in the browser. If a student is about to paste this, make sure they know the restart is coming so they don't panic and start a new chat afterward.

## Step 2 · The two pauses

The two human moments, and the restart is the one that trips people (same as Class 2's Supabase step). Pause 1 — RESTART: new tools only switch on after a full quit-and-reopen; then they MUST return to the same chat via the 🕐 clock/history icon at the top-right of the Claude box, pick the chat they were in, and say "continue the Cloudflare setup." NOT a new chat. Pause 2 — sign in to Cloudflare in the browser and click Allow (logs the terminal into their account). Done when Claude confirms it's logged in (it prints their account name) and the domain shows Active. If a student says "Claude lost its place after restarting," walk them through resuming via the history icon — that's the fix, and it's the deck's main stuck-point.

## You're all set

Recap — reinforce what "ready" means: domain Active on Cloudflare with the site working as before, Claude has Cloudflare's official skills, terminal logged in (Claude verified it). If a student is unsure they're actually ready, the concrete check is Claude printing their account name and confirming the domain is Active. Set the anticipation for class: they'll build a second bot-only version of the site and the front door that serves it — by the end, ChatGPT and their customers see two different sites at one address.

## If something breaks

The troubleshooter habit plus THE known gotcha for this class. General move: describe the symptom to Claude, don't hunt. But this deck has one specific high-frequency failure worth leading with: if the site loops or shows an SSL error right after moving to Cloudflare, it's almost always the SSL/TLS mode — it likely needs to be Full (strict). The slide even has a ready prompt for exactly this. So if a student reports "my site broke right after the domain move," go straight to checking Cloudflare's SSL/TLS mode before anything else. Other likely causes if consulted: the restart/resume sequence (resume via history icon), or a still-Pending domain (just wait). Honor the last line — a couple of tries and still stuck, email Eric rather than lose the evening.

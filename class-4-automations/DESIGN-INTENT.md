---
name: Class 4 — Automations (Design Intent)
description: What Class 4 builds and why, plus the load-bearing decision that it is
  the toolbox Class 5's agent reuses. Written before the deck; the deck checks
  against this, not the reverse.
status: Committed direction (from instructor discussion). Not yet built.
---

# Class 4 — "The Morning Briefing" → your chief-of-staff's senses

## The automation (what ships live, by end of class)

**A "morning briefing" — a LOCAL PYTHON SCRIPT on the student's own Mac.** No
hosted service (NOT Vercel, NOT Cloudflare). The Mac is the computer; the student
has one and it runs there. The script:

1. **Reads** from a pluggable set of the student's own work sources,
2. Makes **LLM calls inline at the judgment steps** (classify/rank/decide) with
   deterministic Python around them, and
3. **Delivers** a single triaged brief to the student (simplest: email via SMTP /
   a mail API, or even a local notification/file — no domain/DNS needed).

It is **scheduled with a launchd LaunchAgent** (`StartCalendarInterval`), at a
user-set time, running **when the Mac is on**. Missed runs (Mac asleep/off at the
scheduled time) fire **on next wake** — launchd defers and runs once on wake. This
is NOT cron: plain `crontab` silently drops missed runs and never catches up.
launchd is the instructor's already-proven pattern (his `com.firebrands.hub-sync-daily`
plist does exactly this at 7am). Bonus: a LaunchAgent runs inside the logged-in GUI
session, so the login keychain is unlocked — which is *why* the subscription LLM
auth below works headlessly. (The deck may say "schedule it" colloquially and
mention cron once as "the older way that can't catch up on wake" to justify launchd.)

The teaching goal: **take a process you do by hand and turn it into a script that
runs it for you, delegating the judgment steps to an LLM call.**

It is **read-only against private accounts**: it never sends, deletes, or moves
anything in the student's email/chat. Its *only* write-actions are the two safe
ones below. This consent boundary is a **hard rule** and it carries through Class 5.

### The two safe write-actions we DO build

- **Draft, don't send.** It can draft email replies and hand them to the student
  to approve/send themselves. It never sends on their behalf.
- **File to a task manager.** It can create tasks in **Todoist** via that tool's
  *own* API token (the same token used to read becomes read+write) — "it put
  today's three things on my list." (Todoist is the confirmed flagship connector;
  Notion/Trello are excluded — see tiers.)

### The write-frontier we do NOT build (but DO highlight)

Send-as-you, move calendar events, post to Slack — all the OAuth write scopes.
Class 4/5 **point at this as the next frontier and arm the student with the skills
to do it themselves**, but never build it live (OAuth = live-class death, and
acting in someone's real account is a consent + blast-radius problem).

## The pluggable adapter architecture (the load-bearing decision)

The brief is **N input adapter functions + inline LLM calls at judgment steps + a
delivery step.** Each adapter is a **clean, individually-callable Python function**
returning structured data — `get_calendar()`, `get_tasks()`, `get_feeds()`, etc.
— NOT one tangled `generate_brief()` blob.

**Why this exact shape is non-negotiable:** those functions are the tools Class 5's
agent reuses *verbatim*. Class 4 wires them into a **fixed script the human wrote**
(cron runs the same sequence every morning; the LLM is called only at the judgment
steps *inside* that sequence). Class 5 keeps the functions and hands them to a
**brain that drives** (the model chooses whether/which to call, in a loop). Same
toolbox; the only net-new Class 5 surface is the agent loop + the model driving +
the write-tools' escalation. This is how we keep the (very bug-heavy) agent class
small: Class 5 starts with Class 4's functions **already debugged**.

The Class 4 → Class 5 shift is really three parallel escalations, all saying
*human-anchored → autonomous*:
- **Driver:** fixed script sequence → the LLM decides what runs.
- **Scheduler:** cron (a fixed time) → the agent decides when/whether to act.
- **Credential:** the human's subscription (assistive) → the agent's own API key
  (autonomous). See the LLM-auth section — this is the literal embodiment of the
  shift, not a tax.

If Class 4 builds a monolithic script, Class 5 has nothing to reuse and we're back
to net-new. So: **build the adapters as separate functions from slide one.** Costs
nothing; it's just good structure. Enforce it.

## The bright line (what's actually out of scope)

The constraint is NOT "avoid auth" and NOT "keyless is best." API keys, personal
access tokens, MCP servers, and normal account-link flows are all IN SCOPE and
good practice to teach — copy-a-token → env var is exactly the muscle these
students should build, and MCP reinforces a Class 2 concept.

The one bright line: **no Google Cloud Console modification** — no creating a GCP
project, no OAuth consent screen config, no 7-day-unverified-token trap. THAT is
the class-killer. It is why the full Gmail API is out, not "because it needs a
key." An MCP server or account-link that fronts the auth WITHOUT sending the
student into Google Cloud is fine — check whether one exists before writing a
source off (esp. Gmail).

Tiers below are sorted by live-class friction, but "keyless" is just a nice floor
so nobody's brief is empty — it is NOT preferred over a clean key/token/MCP path.

## Adapter tiers (CONFIRMED by connector research — live HTTP-tested)

**Universal core (keyless — everyone ships it, nobody leaves empty-handed):**
- **Calendar via secret-ICS URL** — personal Google calendar's private `.ics`
  feed; plain HTTP GET, no OAuth/Cloud project/token expiry. RULE: use a
  PERSONAL @gmail calendar (Workspace admins can disable the secret address).
- **Google News RSS** — `news.google.com/rss/search?q=<their phrase>`; keyless,
  personalized, live-tested 200. Teach the `?q=` SEARCH feed only (topic/geo
  feeds redirect to opaque hashes).
- **Own money-path URL status** — one-line "is my booking/checkout link up"; keyless.

**Featured connector (one copy-paste token, walked through live):**
- **Todoist** — the flagship. One "Copy API token" button (Settings →
  Integrations → Developer), static non-expiring token, purpose-built
  `/api/v1/tasks/filter?query=today|overdue`. This is ALSO the connector the
  "file a task" write-action reuses (read token → read+write). Linear/Asana are
  "if that's your tool" alternates.
- **Slack** — featured-OPTIONAL. Self-issued user token (`xoxp-`), no callback
  URL, no verification, does NOT expire; ~5 min live IF the student uses a
  workspace THEY OWN (employer workspaces with app-approval ON = killer). Scopes
  under *User* Token Scopes, not Bot.

**Optional adapters (reward, never required):**
- **Class 2/3 dashboard data** — `getDashboardStats()` reads the student's own
  **Supabase** numbers via a keyed read (NOT GA4/OAuth — they already piped
  GA→Supabase in Class 2). Highlights the cohort; cold buyers skip it. Proves the
  pluggable lesson and makes the series visibly compound.

**Gmail — FEATURED-OPTIONAL (local Python makes this EASIER, revisit path):**
- On a LOCAL Python script the Worker-era Composio workaround is no longer forced:
  a local script can use **app-password + IMAP directly** on a personal Gmail
  (IMAP is just a network socket — no GCP, no Node-vs-Worker problem). Composio
  managed auth remains a clean alternative (hosts the OAuth app, zero GCP). RESOLVE
  in research: app-password+IMAP vs Composio for a local script — but either keeps
  us inside the bright line.
- **Do NOT make Gmail mandatory:** the app-password/"unverified app" steps spook
  non-engineers, and work-Workspace accounts may be admin-blocked. Offer + demo;
  never put it on the critical path to shipping.
- Full Gmail API via self-built GCP OAuth stays OUT (the bright line).
- NOTE: reading Gmail over IMAP (a network socket) also sidesteps macOS TCC
  permission prompts, unlike touching local Mail.app. See macOS gotchas.

**Explicitly EXCLUDED (live-tested traps):**
- **Notion / Trello** as the featured task manager — Notion's per-page "Add
  connections" silently returns empty data; Trello needs a Power-Up app. Use
  Todoist; mention Notion only as advanced.
- **Reddit RSS** — 429s from datacenter IPs. On a LOCAL Mac (residential IP) this
  is less severe than from a cloud cron, but still set a descriptive User-Agent
  and keep it off the guaranteed core.

## Runtime decision (CORRECTED → local, launchd)

**A local Python script on the student's Mac, scheduled with a launchd
LaunchAgent.** No hosted platform. Missed runs fire on next wake (launchd defers).
Delivery: simplest email path (SMTP or a mail API) — or a local notification/file
if we want to skip email entirely on day one. macOS realities (sleep/wake, TCC,
secrets) are taught as honest reliability lessons — see macOS gotchas.

## LLM auth + the C4 → C5 credential story (RESOLVED — teach both, lead free)

The judgment steps are LLM calls. The script calls the local **Claude Code CLI
headless** (`claude -p …`, or the Agent SDK which wraps the same CLI) by absolute
path. Same on Mac and Windows — NO OS fork, nobody's second-class. Three tiers:

**Tier 1 — lead with this (FREE):** `claude setup-token` → a **one-year**
`CLAUDE_CODE_OAUTH_TOKEN` that rides the student's existing Claude subscription (no
API key, no per-token billing). Purpose-built for scripts/CI. The scheduled job
carries the token as an env var.
- **Why not the bare `/login` token** (what the instructor's current 3 Mac jobs
  ride): confirmed it RUNS free, but the plain `/login` OAuth token **silently
  expires in unattended jobs and is NOT auto-refreshed** (GitHub claude-code #38813)
  — works in class, dies weeks later with a silent 401. `setup-token` is the
  durable free path that fixes this. (This corrects the earlier "proven, no token"
  note: it was proven to RUN, not to LAST.)

**Tier 2 — show as the bulletproof / "when you outgrow the subscription"
alternative:** `ANTHROPIC_API_KEY` in a `chmod 600` `.gitignore`'d `.env`. Never
silently expires, identical on both OSes, ~$0.90/mo (verified, Haiku) — under $1.
Costs a one-time $5 credit + console visit. This is ALSO the seed of the Class 5
credential escalation.

**Tier 3 — do NOT teach:** bare `/login` unattended (the silent-expiry trap).

Honest caveat for the deck: a stray `ANTHROPIC_API_KEY` in the student's shell
profile silently outranks the subscription token and bills the API — the script
should `unset` it before invoking `claude` on the free path (or just commit to the
key path). The switch between tiers is ~one line (which env var is set), so the
same source-reading functions and judgment code run unchanged.

ToS: your own subscription for your own automation, running as you, is intended
use. The restriction bites when you ship subscription-backed access to OTHER
people — which is exactly the Class 5 boundary.

**Class 5 (autonomous agent):** the agent driving its own loop, that could run for
anyone, uses its **own Anthropic API key** — the Tier-2 path from Class 4, now
mandatory. The reason to switch is autonomy + ToS, not money.

**The C4→C5 sentence:** *"In Class 4 your script borrows the Claude you already pay
for — it runs as you, on your machine, for you. In Class 5 the agent gets its own
key, because the moment software acts on its own and could run for anyone, it can no
longer borrow your personal login."*

## MCP vs direct calls (a TAUGHT concept that bridges C4 → C5)

**Direct API/token calls power the fixed automation (Class 4); MCP powers the
interactive agent (Class 5).** Same source-reading functions, different mechanism
by whether a human/reasoning-loop is in the loop. True on two grounds:
1. **Value:** MCP exists to let a *reasoning model choose tools at call time*. A
   fixed script already knows exactly which functions it calls each run → MCP is
   pure overhead. The Class 5 agent exploits it; the Class 4 script gains nothing.
2. **Credential portability:** a hosted-MCP account-link mints a SESSION-BOUND
   credential an interactive agent can use but a fixed unattended script cannot
   cleanly present → a direct call is simpler for the cron.

Teach it as *a* reason automation and agents differ. Caveat: direct calls stay
inside the bright line only when read auth is a key / PAT / hosted-account-link —
never self-managed Google OAuth.

## macOS gotchas the deck must cover (from research — all defused)

1. **Sleep/off = skipped run; cron never catches up.** Use a launchd LaunchAgent
   (`StartCalendarInterval`) — it defers a missed run and fires on next wake.
   Honest caveat: a laptop fully off all weekend still misses it (a real reason
   Class 5 eventually moves the schedule off the laptop).
2. **TCC privacy wall, no GUI to click Allow.** A headless script reading local
   Mail/Calendar/Contacts or protected folders is blocked with no prompt to
   accept. Defuse by DESIGNING AROUND it: read Gmail over IMAP (network socket,
   not TCC-gated) and write the brief to a pre-authorized project folder. Only if
   a student insists on local Mail/Calendar: grant the Python interpreter Full
   Disk Access in System Settings → Privacy.
3. **Secrets.** Third-party tokens (Todoist, Slack, mail) → a `chmod 600`,
   `.gitignore`'d `.env`. EXCEPTION: the Claude/LLM auth does NOT go in `.env` — it
   rides the keychain subscription with no token (the whole point of the free path).

## Cross-platform: Windows (RESOLVED — clean parity)

The class works on Windows too, and the fork is small. Teach the CONCEPT once
(local script, scheduled, LLM at judgment steps, run-on-wake catch-up); let Claude
generate the OS-specific setup. One track, an OS-specific setup prompt — not two
full tracks.
- **Scheduler:** **Windows Task Scheduler** is a clean launchd equivalent.
  DAILY trigger + **`StartWhenAvailable`** ("run as soon as possible after a missed
  start") = the launchd deferral analog; a run missed while asleep/off fires ~10 min
  after next wake/boot. Keep it `/SC DAILY` (StartWhenAvailable needs a repeating
  task; `/SC ONCE` won't catch up). `WakeToRun` OFF (don't wake the machine —
  catch-up on next wake is enough). Run as the logged-in user. `schtasks` is
  CLI-drivable so Claude generates it.
- **LLM auth:** NO Mac/Windows fork. Windows stores the Claude credential as an
  ACL-gated file (`%USERPROFILE%\.claude\.credentials.json`) readable by any process
  running as that user — so a "run only when logged on" task reads it fine (cleaner
  than Mac's keychain-session gate, actually). Same three-tier auth as above;
  `setup-token` works identically. Native Claude Code on Windows (no WSL needed;
  install Git for Windows as the shell backend).
- **Paths / interpreter:** `py`/`python` launcher, absolute paths, `.env` loading
  differ trivially — Claude handles them. Deck copy-paste prompts must NOT be
  Mac-only (`~/Library/...`); phrase them so Claude adapts per OS.

## Hard constraints (from the series)

- **No dependency on Classes 1–3.** Assumes only Claude Code + the Mac + the habits
  (plan mode, reference docs). No host/GitHub strictly required — it's a local
  script. Sellable to a cold audience. The dashboard adapter is the one nod to
  continuity and it is strictly optional.
- **Ships live in one ~2–3h sitting.** To show it "fire in the room," just run the
  script manually (and/or set a cron entry a minute out) — no waiting on a hosted
  cron dashboard. The applause moment is the brief landing in their inbox/notification.
- **Not a rerun of Class 2.** Class 2's function was a *sync* (plumbing nobody did
  by hand) and it was a hosted serverless job. Class 4 is a *local script* doing a
  *chore that ate your morning*, calling an LLM for judgment. Different in kind AND
  different in place (their Mac, not the cloud).
- **ROI story:** not "cheaper than a $20/mo Zapier." It's "it runs without you,
  and it's the senses your future agent will use." Infrastructure, not a workflow.

## The Class 5 handoff (design to it now)

Simplest *useful* agent = Class 4's read-functions (senses) + ONE valuable action
(draft replies / file tasks) + a loop the LLM drives. Useful because it **acts**,
not just answers. Read-only against private accounts still holds. The three
escalations (driver, scheduler, credential) are the spine of the handoff. The
deck's closing slide: *"next class, we give these functions a brain, its own key,
and the freedom to choose when to run — and point you at the write-frontier to
extend it yourself."*

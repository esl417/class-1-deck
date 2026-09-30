# Teaching notes — Advanced Class 6 (OpenClaw in VS Code)

Per-slide notes for the bot view. `##` = slide label. Private. Teach the skill, don't
perform the build. The student finished Advanced Classes 4 and 5 in Claude Managed Agents: a
7:00 brief automation saving to Drive or Dropbox, and a 7:30 agent that acts on it and writes a
handoff (Taken care of / Needs your action / FYI), with its memory in handoff-log.md. They did
the Class 6 prereqs (VS Code, Claude Code, git, Node, GitHub CLI, ant CLI, logged in). Today
they compare Cowork, Managed Agents and OpenClaw, learn OpenClaw's parts, then install it,
clean it out, and rebuild the whole chain in a project folder that is a private GitHub repo: the
Class 4 brief as a plain Python automation (no OpenClaw: an automation needs no agent), and the
Class 5 agent in OpenClaw, which handles everything after the brief exists.
OpenClaw changes fast: check docs.openclaw.ai before giving any command or config key, and
prefer `openclaw doctor` and the docs over memory. Rules that never slide: keys only in `.env`
(in `.gitignore` before the first commit) or OpenClaw's own credential store, never pasted into
a chat; the agent drafts, the student sends; no skill or plugin installed unread; the Gateway
stays on loopback. Cost is a thread in every Advanced class: OpenClaw has no per-run budget, so
the caps live at each model provider, and trimming overhead is the lever.

## The arc

Orientation. Class 4 dictated steps (automation), Class 5 dictated the deliverable (agent),
Class 6 moves the same chain (brief and agent) somewhere they own every part. Plant the two standing rules: cap
spend before anything runs, and use the simplest setup that does the job. Today tests the
second rule: OpenClaw is not an upgrade everyone should take.

## The finish line

What works by the end of class: the whole chain running on their computer. The Class 4 brief is
rebuilt as a plain Python automation (built and reviewed on a branch) that runs at
7:00 with no OpenClaw involved; the Class 5 agent in OpenClaw acts on it at 7:30; the handoff
arrives in the chat app they choose (Slack, Telegram, WhatsApp and more), where they can also
message the agent. Be clear about scope: today is the setup and a first working version;
finishing it (every source and app connected, the handoff as good as Class 5's) is homework, and
cloud hosting (Render) is explained at the end, not done.

## What OpenClaw is

OpenClaw is free, open-source, self-hosted agent software (formerly Clawdbot / Moltbot). It
runs as a background program on their computer or a rented server and connects a model to
files, tools and chat apps. Three differences that matter: it runs where they put it (on a laptop it
sleeps with the laptop; on a rented server it runs around the clock), any model (60+ providers), and it lives in chat apps. The trade to say
plainly: they can change everything, and they maintain everything: updates, uptime, security,
debugging. Claude Code is their help desk for all of it.

## Three ways to run an agent

The comparison table. Walk it row by row, left to right, as a cost of ownership. Rows: who runs
it; models (Claude only on both Anthropic surfaces; any on OpenClaw); payment (Cowork is the
flat Claude plan with no usage bill; Managed Agents is prepaid API credits in the Console,
charged per token plus $0.08 per session-hour; OpenClaw is an account and card at each model
provider, plus hosting); token overhead (on Cowork and Managed Agents Anthropic decides what
loads with each call and they can't trim it; in OpenClaw every file, skill and check-in is
theirs to cut, which is Step 1); customization; how they reach it (Cowork via the Claude app on
desktop and phone; Managed Agents only via the Console, as Class 5 showed; OpenClaw via
Telegram, Slack, WhatsApp and more); what wakes it; deploy; maintain; debug (sessions in the
Console trace every step; OpenClaw means logs, config files and health checks, which is slower);
security (on OpenClaw the machine, keys and every installed skill are theirs to secure).

## Which one to use

The decision tree, built from the comparison table's rows (each question is labeled with the
rows it comes from). Start at the top; the first yes decides. 1 (models): does it need a model
other than Claude? Yes → OpenClaw. 2 (what wakes it, customize): does an event need to wake it (a webhook: a form
submitted, a file landing, a payment), or does it need custom tools (their own scripts)? Yes →
OpenClaw. 3 (customize): does it need a service reached with an API key rather
than an MCP connector? Cowork's connectors, custom ones included, are all MCP; a service that only
offers an API with a key (common for industry tools, internal systems, niche SaaS) can't be
plugged into Cowork. Managed Agents can call any API, with the key kept in a credential vault.
Yes → Managed Agents. This is the clean separator: Cowork also has custom connectors, tool
permissions and a sandbox, so those don't justify the move. No to all three (payment,
maintain): a Cowork project on the flat Claude plan, nothing to host. Messaging is deliberately
not a question: a Cowork project can be messaged from the Claude app on desktop and phone, so
being reachable doesn't by itself justify OpenClaw (only Managed Agents lacks it). Any OpenClaw
answer also brings the Maintain and Security rows: only choose it if they'll own the upkeep.
Worked example, said honestly: the Class 5 agent answers no to questions 1 and 2, so it can stay
where it is; they rebuild it in OpenClaw today to learn the surface on a job they know, for the
day a job answers yes. Consumer agents:
big companies are shipping agents for everyone (xAI's Grok Bot, in early beta since August 2026
in its top tier; Meta's Muse, a personal agent app launched September 2026; OpenAI and Google
have their own always-on agents), so a given job may soon be doable off the shelf and is worth
watching. The point to land: once they can build in OpenClaw they don't have to wait for anyone;
they can build anything. Product details here come from press coverage and change monthly;
don't quote prices as fact.

## Cost control

This class's cost beat. Managed Agents capped every run but gave no control over the overhead
riding on each call; OpenClaw flips both. No per-run budget field, so limits move to the model
provider: a monthly spend limit, prepaid credits, auto-reload off, at every provider they use
(each bills separately), and hosting bills separately too. Overhead: the injected workspace
files (AGENTS.md, SOUL.md, IDENTITY.md, USER.md, MEMORY.md, BOOTSTRAP.md on a new workspace),
the skill list and the tool list go out with every message. The default install is full of
extras; Step 1 removes them. The heartbeat defaults to every 30 minutes (48 wakes a day), and by
default each heartbeat is a full turn in the main session that resends the whole conversation
history plus the workspace files, so its cost grows with the chat. The 100K figure is the docs'
example for a long session, not a fixed cost: "~100K tokens down to ~2-5K per run" with
isolatedSession: true (no history); lightContext: true also skips the workspace files. Keep it off until it's set up lean. The classic surprise bill:
a key pushed to GitHub, found by bots within minutes. `.env` goes in `.gitignore` before the
first commit. Official page: docs.openclaw.ai/reference/token-use.

## The parts

The bridge from Managed Agents. Every Console part has an OpenClaw home: General (model, system
prompt) → openclaw.json for the model and AGENTS.md / SOUL.md / USER.md as the prompt; tools and
permission policies → tool allow and deny lists plus exec approvals; MCP servers and API calls →
the same MCP servers and API calls, plus plugins and their own scripts; skills → skills (a folder with SKILL.md, the same idea as
Class 4); environment → their computer (sandboxing is optional, off by default, Docker-based);
credential vault → OpenClaw's credential store for model keys, `.env` for script keys;
deployment → automations (schedules) and the heartbeat; sessions → sessions and logs in the
Control UI and terminal; handoff-log.md → MEMORY.md plus daily notes in memory/. New: channels
and webhooks, which Managed Agents couldn't do.

## The workspace

The agent is a folder of plain-text files, which is why VS Code: they can see and edit the agent
directly. Injected into every call (per the current docs): AGENTS.md (operating rules; the
biggest default file, about 8,000 characters of group-chat etiquette, emoji reactions, voice and
platform formatting most agents don't need), SOUL.md (personality), USER.md (about them),
IDENTITY.md (name, vibe), MEMORY.md (curated long-term memory, main session only, not in group
chats), BOOTSTRAP.md (a first-run interview on a brand-new workspace; delete it after). Not
injected: memory/YYYY-MM-DD.md (read as needed), HEARTBEAT.md (the heartbeat's checklist),
TOOLS.md (setup notes). Caps: 20,000 characters per file, 60,000 total. The model, channels,
schedules and permissions live outside the folder in ~/.openclaw/openclaw.json, with the logins
in ~/.openclaw/credentials; that folder stays out of GitHub.

## The Gateway and channels

The Gateway is the always-on background program (port 18789, bound to loopback so only their
own machine reaches it, token auth on by default). It serves the Control UI (`openclaw
dashboard`). Channels: Telegram and WebChat ship with it; Slack, WhatsApp, Discord, Signal,
Teams and more are official plugins. Pairing: a stranger who messages the bot gets an 8-character
code that expires in an hour, and nothing happens until the owner approves it (`openclaw pairing
approve telegram <CODE>`). The consequence to land: no Gateway, no agent; if the laptop sleeps
at 7:30, the 7:30 run doesn't happen, which is what cloud hosting solves.

## Tools, skills and permissions

Tools: exec (run commands), read/write/edit files, web search and fetch, browser, message, cron,
subagents. Skills: folders with a SKILL.md (name and description frontmatter); around 50 bundled
(the repo's skills folder had 49 in September 2026) and thousands on ClawHub. The skill list is
injected every call, so unused bundled skills cost tokens. Permissions: tools.allow / tools.deny
/ tools.profile, and exec approvals with a security level (deny, allowlist, full) and an ask
mode (off, on-miss, always); the stricter of config and approvals wins. The custom-tool payoff:
a Python script in the folder, a skill that says when to run it, and exec runs it. No separate
application needed, which removes the Class 5 limit.

## What wakes it

Four triggers against Managed Agents' two (a deployment, or them in a session). A message in a
channel. The heartbeat (default every 30 minutes; reads HEARTBEAT.md and replies HEARTBEAT_OK
unless something needs them; settings include isolatedSession, lightContext and activeHours).
Automations: `openclaw automations` (alias `openclaw cron`), schedules at exact times, each able
to run in an isolated session with its own model. Webhooks: another app posts to /hooks/agent
with a bearer token. Rule of thumb from OpenClaw's own guidance: exact times in a schedule, loose
periodic checks batched into the heartbeat.

## Any model

60+ providers including Anthropic, OpenAI, Google, xAI, Moonshot (Kimi), OpenRouter and local
models via Ollama. Set with `openclaw models set <provider/model>`, add fallbacks with `openclaw
models fallbacks add`, switch mid-chat with `/model`. Three points: fit the model to the job
(strong for judgment, cheap for routine checks, the chain idea inside one agent); a fallback
takes over when the main model is down or rate-limited; test before trusting, because models
follow instructions differently. Eric runs his on Kimi. Each provider is its own account, bill
and spend limit.

## Security

They are the security team now. ClawHub: in February 2026 researchers (Koi Security, the
"ClawHavoc" report) found 341 malicious skills out of about 2,857, mostly dropping a macOS
password- and data-stealer. A skill is code running with the agent's access: install only what
they or Claude Code have read. Whoever can reach the Gateway controls the agent, so it stays on loopback; `openclaw security audit` checks
the setup. Keys live in `.env` or OpenClaw's credential store, never in a chat, the agent's
files, or GitHub. Updates: security fixes ship often (CVE-2026-25253, fixed in January 2026,
let one malicious link take over an install via the Control UI). Class 5 rules carry over: it
drafts, they send, and anything it reads from strangers can try to give it orders.

## Install

Before Step 1. They make a folder (morning-agent), open it in VS Code, and have Claude Code
install OpenClaw with the official installer (macOS/Linux: `curl -fsSL
https://openclaw.ai/install.sh | bash`; Windows: the install.ps1 script; it handles Node) and
make the folder a private GitHub repo with `.env` in `.gitignore` before any commit. They run
`openclaw onboard --install-daemon` themselves in the VS Code terminal, because it's interactive
and the model key goes in there, not in a chat. Choices: ask first rather than full access; their
provider and model; this folder as the workspace (if onboarding doesn't offer it, Claude can set
OPENCLAW_WORKSPACE_DIR); skip the suggested ClawHub skills and plugins and the memory import
(overhead and risk). Then `openclaw doctor` and `openclaw gateway status`. The memory/ folder and
MEMORY.md hold personal context, one reason the repo must be private.

## Step 1 · Clean it out

Eric's rule: the first thing after installing is cleaning it out, because whatever's loaded
rides on every call. Measure first: `/context list` or `/context detail` in the Control UI chat
shows each file's and skill's size. It's a baseline cleanout, not tailored to any job: the goal is a clean slate, and Step 2 adds
this agent's job. Cleanup: delete BOOTSTRAP.md (onboarding may already have); strip every default
example and boilerplate from AGENTS.md, SOUL.md, USER.md and TOOLS.md (group-chat etiquette,
emoji reactions, voice storytelling, platform formatting, the heartbeat check-in examples, sample
notes), keeping only the red lines and the rule to write memories to files; turn off every bundled
skill in openclaw.json (`skills.allowBundled` is the allowlist for bundled skills;
`skills.entries.<name>.enabled: false` for individual ones), adding back only what a job needs
later; heartbeat off (`every: "0m"`). Claude shows each change first.
Restart the Gateway, run `openclaw doctor`, measure again. The difference is saved on every
message, schedule and check-in. Confirm exact config keys against docs.openclaw.ai.

## Step 2 · Bring in your agents

Prompts in this deck are pasted into Claude Code, which has no idea what "Class 4" or "Class 5"
means, so they name the agents by role and Console name (the morning-briefing agent, the action
agent) instead of by class number. Rebuild from what works, not a description; both links of the chain come over. They download
handoff-log.md from the briefing folder into the project. Claude uses the ant CLI (logged in
during prereqs) to pull the Class 4 briefing agent and its skill (`ant beta:agents retrieve`, and
`ant beta:skills:versions download` for the skill's files) and the Class 5 agent into
export/; the Console's Export as code is the other route. A Raw agent definition holds
model, system prompt, tools and MCP servers; skills appear only as IDs, hence the separate skill
download. Translate the Class 5 agent now: who they are → USER.md; the job, the three-section
deliverable and limits → AGENTS.md; tone → SOUL.md; handoff-log.md's standing notes → MEMORY.md.
Keep files short (overhead). The brief waits for Step 4; the exported briefing skill is only its
spec and does not go into the agent's skills/ (it would add overhead to every agent call). Vault credentials never export, which is
correct; each app is reconnected one at a time. Then Claude gets every app the two agents used
working: it connects the same MCP servers, and for each API walks the student through getting the
key, which the student pastes into `.env` themselves (Claude creates `.env` first and confirms
it's in `.gitignore`); each connection is tested before moving on. Fallback where a service has no
MCP server or key-based API: a trusted plugin, skill or script.

## Step 3 · Model and keys

Main model plus a fallback via Claude Code. The main model makes this agent's judgment calls, so
not the cheapest; routine jobs (heartbeat, simple automations) can get a cheaper model later.
`.env`: created in Step 2 (and confirmed in `.gitignore`); every later key goes there too, pasted
by the student in VS Code. Scripts read from it; Claude never sees the keys in chat. The habit
before every commit: ask Claude whether anything secret is about to be committed.

## Step 4 · The brief, in Python

The design rule (Eric's): the brief is an automation, every step dictated, so it needs no agent
and no OpenClaw; OpenClaw is for the steps after the brief exists. Loading OpenClaw's workspace
files, skill list and tool list to produce a brief would be pure overhead. Branching is taught
hands-on here: main is the version that runs; a branch is a copy where they change things
safely, merged only after review. On a branch called brief-automation, Claude writes
scripts/brief.py from the exported briefing skill (the spec): it pulls each source through its API
with keys from `.env`, does every dictated step (fetching, counting, dates, formatting), makes a
single call to a cheap model for the one judgment ("what needs me today"), and saves the brief to
briefs/, dated. Honesty rules carry over from Class 4: say when a source failed; write a brief
even on a quiet day. Test it, review it (the code-review and security-review agents set up in the prereqs run on it), fix what's real, then merge into main and run brief.py once to check today's brief lands in briefs/. Every change from now on is branch, review, merge; once it runs in the cloud, main is what runs, so only reviewed code reaches it. (No second AI coder in class: Eric decided against installing another tool.) Keep personal output folders
(briefs/, logs/, memory/) out of commits via `.gitignore`. Sources with a simple API key are
easiest first; Google's APIs need an OAuth client, so Claude may suggest starting with one source
and adding the rest as homework. The model key for the judgment call also lives in `.env`.

## Step 5 · Schedule the chain

The two Managed Agents deployments rebuilt, each with the right tool. 7:00: brief.py on the
computer's own scheduler (on a Mac, Claude sets up a launchd job, which also runs a missed job
when the Mac wakes; cron works too), logging to logs/brief.log so a failed run is visible. 7:30:
an OpenClaw automation (`openclaw automations`) in an isolated session on the main model,
"Handle my morning.", reading today's brief from briefs/ and saving the handoff, dated, to their
Drive or Dropbox folder (connected in Step 2) so they can open it from anywhere; a file in the VS
Code project would be unreachable from a phone. The brief can stay local because it's an
intermediate file only the agent reads; the handoff is the deliverable. Step 6 adds sending it in
the chat app too. Claude then lists the next few run times for each, which catches schedule
typos before a morning is missed (Class 4's cron lesson: `* 7 * * 1-5` runs every minute of the
7am hour, `0 7 * * 1-5` once). Once the handoff is right, pause both Managed Agents deployments (Class 4 and Class 5),
or they get two briefs and double drafts. Heartbeat stays off; when wanted, a short HEARTBEAT.md,
isolated light session and activeHours keep each wake to a few thousand tokens. The laptop must
be awake (or wake) for 7:00 and the Gateway running for 7:30 until it's hosted. Same shape as
Class 5: an automation handing off to an agent.

## Step 6 · Connect a chat app

The student picks the chat app they already live in (this student lives in Slack). Telegram and
WebChat ship with OpenClaw; Slack, WhatsApp, Microsoft Teams, Discord, Signal, iMessage and more
are official plugins (check docs.openclaw.ai/channels for the current list and each one's setup).
Claude Code walks them through creating the bot or app for that platform (Telegram: @BotFather,
`/newbot`; Slack: a Slack app in their workspace), puts any token in `.env`, and connects the
channel with DM policy on pairing. The student messages the bot, gets a pairing code, and Claude
approves it (`openclaw pairing approve <channel> <CODE>`). It's the last build step, so once connected Claude also sends the 7:30 handoff there.
Then a real job, and they check the answer against the source (act-then-verify from Class 5). The catch with Slack at work: a company
workspace usually needs an admin to approve a new app; if that won't happen today, start with
Telegram (needs only them) and add Slack once it's approved. WhatsApp links a personal account by
QR code, so it speaks as them: prefer a separate number or a bot-style channel.

## Webhooks

Concept, not built today. hooks.enabled plus a hook token gives the Gateway endpoints
(POST /hooks/wake, /hooks/agent, /hooks/<name>) with bearer-token auth; tokens in the query
string are refused. Examples: a form submission drafting kickoff notes, a contract landing in Dropbox
and getting summarized with its dates flagged, anything Zapier or Make can see. The catch: a webhook needs an
address the internet can reach, and a laptop on loopback isn't one, so webhooks come with cloud
hosting; the token is a key and goes in `.env`. Stretch homework once hosted.

## When it breaks

No Sessions page does this for them. First check: is the Gateway running (`openclaw gateway
status`)? Config changes only take effect after a Gateway restart (`openclaw gateway restart`).
Then `openclaw status` (channels, sessions, usage), `openclaw
doctor` (and `--fix`), `openclaw logs --follow`, and the Control UI's session transcripts. The
move from the Class 1 prereqs: describe the symptom and let Claude Code dig ("My 7:30 run didn't
come. Check OpenClaw's status and logs and tell me why."), then fix the cause on a branch. Common
causes: laptop asleep, Gateway not running after a restart, a model key out of credit or rate
limited, a config typo `doctor` catches, a tool call waiting on an approval.

## To the cloud

Explained, not done. Render is a hosting service with a documented OpenClaw setup
(docs.openclaw.ai/install/render): a render.yaml blueprint running Docker, connected to their
GitHub repo. It runs main, and every merge redeploys, which is why branch-review-merge matters.
The free plan has no disk, so memory and state reset on every deploy; a paid plan with a disk
(the blueprint defaults to Starter with 1GB at /data) keeps them. Keys go in Render's environment
settings, never the repo. The Gateway stays private: reach the Control UI over an SSH tunnel or
Tailscale, not a public port. One more bill to cap. On Render the brief becomes a cron job (Render has
them) and the agent a running service. Once hosted, both run with the laptop closed and webhooks
become possible.

## Homework

Finish the chain until its handoff matches Class 5's. Connect every source the brief reads and
every app the agent acts in, one per branch:
the same MCP server or API it used in the Console, a trusted plugin or skill (read before installing), or a script tool. Add a second chat app
if useful (Slack at work once an admin approves the app). Watch cost daily for a week at each provider and trim anything that grew back.
Then decide: move it to Render, or go back to the Managed Agents chain if that did the job; either is
right under the simplest-setup rule. Help fully with mechanics; what it may do, which model, and
whether it's worth owning are their calls.

## You shipped it

Recap of the course's end state: the decision (Cowork first, Managed Agents next, OpenClaw only
when a job needs it); the chain rebuilt (the brief as a plain Python automation with no agent,
the agent in a cleaned-out OpenClaw acting on it); a chat they can message the agent in; code in GitHub changed only by
branch, review, merge, keys kept out. The rules that travel to any surface: dictate the
deliverable, one job per agent, cap what it can spend, use the simplest setup that works.

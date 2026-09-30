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
a Python script registered as a real tool (name, description, input schema) that the model sees in
its tool list. The simplest documented route is MCP: a small local Python MCP server exposing the
tool, added with `openclaw mcp add` (docs.openclaw.ai/tools/mcp; MCP tools go through the same tool
policy as everything else). A plugin with `api.registerTool` also works but needs TypeScript and a
manifest. A skill is not a tool: a skill only tells the agent how to work. No separate application
needed, which removes the Class 5 limit.

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

## Git words

Adapted from Class 1's "Git words" slide, plus branch and merge, which this class uses hands-on in
Step 4. The student may never have used git (Advanced skipped Classes 1 to 3). Don't lecture the
definitions back; check which word is unclear and anchor it to something they know. The analogy
that lands: git is Track Changes for the whole project. The one that trips people is commit vs push
(both sound like "save"): commit = a checkpoint on their computer; push = send those checkpoints up
to GitHub. Branch = a safe copy to change; main = the version that runs; merge = bring an approved
branch into main. They never type git commands: they ask Claude Code by name.

## Saving and pushing

Three stages. Their computer: edit and commit (snapshots only they have). Push: to GitHub, a
private backup with full history (lose the laptop, lose nothing). Merge into main: only approved
changes; main is the version that runs, and when they host it (Render), every merge to main
redeploys. Unlike Class 1 there's no live website, so a push here is a backup, not a publish; the
"publish" moment is the merge to main once a host watches main. Plain-English asks: "Commit and push
this.", "What changed since my last commit?", "Something broke: go back to the last commit." The
repo is private and .env never leaves the computer because .gitignore excludes it (set up in the
Install prompt before the first commit). Personal outputs (briefs/, logs/, memory/) are kept out
too.

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


After onboarding, from Eric's run of 2026.9.7 (2026-09-30), what the prompt's "fix the warnings
worth fixing" means, for Claude to carry out: `openclaw gateway status` should show the LaunchAgent
loaded (starts at login), running, probe ok, bind 127.0.0.1:18789 (loopback only), matching CLI and
gateway versions. `openclaw doctor` warnings worth acting on: the gateway token is stored in plain
text in ~/.openclaw/openclaw.json (gateway.auth.token); fix with `openclaw secrets configure`, then
`openclaw secrets audit --check`. Legacy browser relay login and browser cookie import are on by
default; they only matter for the Chrome extension, so turn both off if unused. Keep the loopback
bind: doctor lists it as a warning, but it's the safe default. No command owner is set until a chat
channel is connected; connecting one in onboarding (or `openclaw channels add`) sets it, so the
student can run admin commands from chat. Informational, leave alone: "N skills unusable" (missing
tools or keys; Step 1 turns bundled skills off anyway, and `openclaw doctor --fix` would hide them),
Codex or other tools' assets found, heap/desktop/GitHub token/speech notes. No backup yet: run
`openclaw backup create` once the setup works (homework). Workspace: onboarding writes AGENTS.md,
IDENTITY.md, SOUL.md and USER.md into the folder; the --workspace setting lands on the agent itself
(agents.defaults.workspace stays empty, which is fine). Commit the instruction files (the repo is
private, and hosting later deploys from it; USER.md holds personal context, so look it over first);
MEMORY.md and memory/ stay out via .gitignore because the agent writes them. Name the agent
carefully at the first onboarding question: the name shows up in paths and sessions (renaming is
possible but fiddly).
## How it signs in

Onboarding asks for an auth method after the provider. For Anthropic: "Anthropic Claude CLI (Keep
using an existing Claude Code CLI login on this host)", "Anthropic API key", "Anthropic
setup-token". Definitions, checked 2026-09-30:
API key: a key from the provider's developer console (for Anthropic, the Claude Console they used
in Classes 4 and 5). Pay-as-you-go, with spend limits at the provider; works locally and on a
server. This is what the class teaches: the only option with clear policy and a spend cap, which
the whole cost thread depends on. OpenClaw's own docs call API-key auth "preferable for shared
automation or predictable production spend."
CLI login: OpenClaw runs the provider's own installed CLI (for Anthropic, the `claude` binary, as
`claude -p`) as a subprocess under the user's login; it doesn't read or forward the token
(docs.openclaw.ai/gateway/cli-backends). It only works on the machine where that CLI is logged in,
so it can't go to Render. Anthropic allows an end user signing in to the unmodified Claude Code
binary with their own subscription, but its usage limits assume "ordinary, individual usage" (an
always-on agent isn't that), every run including heartbeats draws on the 5-hour and weekly
limits, and Anthropic has changed the rules for third-party tools several times in 2026 (blocks in
January, a terms update in February, a billing change for third-party harnesses in April). UNTESTED: it failed in Eric's own test run (2026-09-30), so the class
doesn't rely on it. If a student tries it anyway on a computer-only agent, they should know it
can eat the subscription or be blocked, and fall back to an API key if it fails. OpenClaw sets the heartbeat default to 1h (not 30m) under subscription auth.
Setup-token: `claude setup-token` prints a long-lived subscription OAuth token (sk-ant-oat01-...)
that OpenClaw stores and sends itself. That's credentials routed through a third-party app, which
Anthropic's terms prohibit (code.claude.com/docs/en/legal-and-compliance). Never.
Other providers: the menu differs, but many offer the same split (a CLI or OAuth login on a
consumer subscription vs a pay-per-use API key); same rule, API key. If a student already chose the
CLI login, `openclaw onboard` can be rerun or the auth changed later (check the current docs for
the command).


Where the key is stored (fresh 2026.9.7 onboarding asks "Where is this API key stored?"):
Environment variable, OpenClaw secret store, or Configured secret provider. Choose Environment
variable. It keeps the key out of openclaw.json (the plain-text warning doctor flagged) and
matches Render, where keys are dashboard environment variables. The secret store is not encrypted
("Store values are not encrypted at rest", a SQLite file under ~/.openclaw) and needs the key
pre-seeded; a configured provider means 1Password, Bitwarden or Vault, too much for this class.
Mechanics, done by Claude Code in the Install prompt so students never handle shell files: it
adds an `export ANTHROPIC_API_KEY=` line to the shell profile (~/.zshrc on a Mac), opens that
file in VS Code for the student to paste the key after the = sign, and has them open a new
terminal before onboarding (onboarding checks the terminal's environment). Never typed as a
terminal command (it would land in shell history) and never pasted into the chat. Caveats, from
the docs and OpenClaw's code: installing the gateway service copies the value into its LaunchAgent
plist (plain text); changing the key later means reinstalling the service; and per OpenClaw's own
docs, any plaintext credential the agent can reach is readable via its file or shell tools. That's
why the real protection is the key itself: a new key just for this agent, with a spend limit in
the Claude Console, revocable on its own if it leaks.
## Finish onboarding

The rest of the wizard, from Eric's run of OpenClaw 2026.9.7 on 2026-09-30 (QuickStart mode; it keeps
the gateway on loopback, port 18789, a generated gateway secret, Tailscale off). Channel setup is
part of onboarding, so students connect their chat app here rather than in a separate step.
Select channel: the wizard lists every channel (Telegram "simplest way to get started", Slack
"supported (Socket Mode)", Discord, WhatsApp "recommend a separate phone + eSIM", Microsoft Teams,
iMessage, Signal, SMS via Twilio, and many more); the student picks the one they live in and
follows its steps. DMs default to pairing: an unknown sender gets a code, approved with
`openclaw pairing approve <channel> <code>` (Claude Code can run it). A company Slack usually needs
a workspace admin to approve a new app; if not today, Telegram (needs only them) and switch later.
One chat app per agent. If they skipped the channel, rerun onboarding or have Claude Code add it.
Memories found: the wizard detects other AI tools' memories (Eric's showed Claude with 556) and
offers to import them; choose No (overhead, and private context the agent doesn't need; it can be
done later from Settings → Import Memory). Search provider: some need an API key, some work
key-free (docs.openclaw.ai/tools/web); pick a key-free one or skip. Skills status shows how many
skills are eligible (Eric's: 151 eligible, 32 missing requirements); for "Install missing skill
dependencies" choose Skip: press Space to select "Skip for now", then Enter (Enter alone doesn't
select it). Step 1 turns bundled skills off anyway. If an older OpenClaw config exists on the
machine, the wizard asks whether to move existing agents to the new workspace; on a fresh install
it won't.

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
even on a quiet day. Claude runs it once, shows today's brief, and reviews the code (the code-review and security-review agents set up in the prereqs run on it), fixing what's real. It does not merge: the student reads the test brief and approves it first ("Approved, merge it into main."). The approval is the lesson: a person signs off on test results before anything reaches main. Every change from now on is branch, test, approval, merge; once it runs in the cloud, main is what runs, so only reviewed code reaches it. (No second AI coder in class: Eric decided against installing another tool.) Keep personal output folders
(briefs/, logs/, memory/) out of commits via `.gitignore`. Sources with a simple API key are
easiest first; Google's APIs need an OAuth client, so Claude may suggest starting with one source
and adding the rest as homework. The model key for the judgment call also lives in `.env`. Name tools for what they do, so the model picks the right one: morning_briefing, not a vague verb. The same script is also the agent's custom tool, which is how tooling is taught, and it is registered as a TOOL, not a skill (a skill only describes how to work; a tool is something the model can call, with a name, description and inputs). The slide's prompt just says "register it as a tool my OpenClaw agent can call"; how to do it is here, for Claude to carry out, not for the student to learn. Route: Claude writes a tiny local MCP server in Python (the official `mcp` SDK, FastMCP) exposing one tool, morning_briefing, which runs scripts/brief.py and returns the brief; it's added with `openclaw mcp add brief --command python3 --arg <server file> --cwd <repo>` and checked with `openclaw mcp doctor brief --probe` (docs.openclaw.ai/tools/mcp). Same script, two triggers: the scheduler at 7:00 with no agent involved, and the agent calling morning_briefing on request (midday, "Rerun my brief"), so the dictated work stays deterministic and cheap instead of the agent redoing it. Unverified until the dry run: exactly how the MCP tool's name appears to the model (check the probe output), and that the tool profile in use allows MCP tools (`coding` and `messaging` do; `full` does; a sandbox needs `bundle-mcp` in tools.sandbox.tools). Alternative: a plugin with `api.registerTool` plus an openclaw.plugin.json manifest, which needs TypeScript.

## Step 5 · Schedule the chain

The two Managed Agents deployments rebuilt, each with the right tool. 7:00: brief.py on the
computer's own scheduler (on a Mac, Claude sets up a launchd job, which also runs a missed job
when the Mac wakes; cron works too), logging to logs/brief.log so a failed run is visible. 7:30:
an OpenClaw automation (`openclaw automations`) in an isolated session on the main model,
"Handle my morning.", reading today's brief from briefs/ and saving the handoff, dated, to their
Drive or Dropbox folder (connected in Step 2) so they can open it from anywhere; a file in the VS
Code project would be unreachable from a phone. The brief can stay local because it's an
intermediate file only the agent reads; the handoff is the deliverable. It's also sent in the chat
app connected during onboarding. Claude then lists the next few run times for each, which catches schedule
typos before a morning is missed (Class 4's cron lesson: `* 7 * * 1-5` runs every minute of the
7am hour, `0 7 * * 1-5` once). Once the handoff is right, pause both Managed Agents deployments (Class 4 and Class 5),
or they get two briefs and double drafts. Heartbeat stays off; when wanted, a short HEARTBEAT.md,
isolated light session and activeHours keep each wake to a few thousand tokens. The laptop must
be awake (or wake) for 7:00 and the Gateway running for 7:30 until it's hosted. Same shape as
Class 5: an automation handing off to an agent. Then the tool test: they message "Rerun my
brief." and check the agent called the morning_briefing tool (visible in the session transcript)
rather than fetching the sources itself, and that a fresh brief came back.

## Webhooks

Concept, not built today. hooks.enabled plus a hook token gives the Gateway endpoints
(POST /hooks/wake, /hooks/agent, /hooks/<name>) with bearer-token auth; tokens in the query
string are refused. Examples: a form submission drafting kickoff notes, a contract landing in Dropbox
and getting summarized with its dates flagged, anything Zapier or Make can see. The catch: a webhook needs an
address the internet can reach, and a laptop on loopback isn't one, so webhooks come with cloud
hosting; the token is a key and goes in `.env`. Stretch homework once hosted.

## To the cloud

Explained, not done in class. The desired setup (Eric's): the student signs up for Render with
their GitHub account, links THEIR class repo, and every push to main redeploys their agent. Facts
below were checked against docs.openclaw.ai (install/render, install/docker, concepts/agent-workspace),
render.com docs and pricing, and Telegram's Bot API on 2026-09-30; the wiring in "How their repo
becomes deployable" is not a documented OpenClaw recipe, so Eric dry-runs it before recommending it.
Check Render's pricing page before quoting a price.

What OpenClaw documents. A render.yaml Blueprint (in github.com/openclaw/openclaw, with a "Deploy to
Render" button pointing at that repo): a Docker web service with a health check (/startupz); a 1GB
persistent disk at /data, with OPENCLAW_STATE_DIR=/data/.openclaw and
OPENCLAW_WORKSPACE_DIR=/data/workspace; OPENCLAW_GATEWAY_PORT=8080; an auto-generated
OPENCLAW_GATEWAY_TOKEN. The docs deploy OpenClaw's own repo or a fork, not a workspace repo, which
is why their repo needs the two files below. An official image exists: ghcr.io/openclaw/openclaw
(mirrored on Docker Hub as openclaw/openclaw); pin a release tag, not latest.

How their repo becomes deployable (Claude Code does this, on a branch, approved before merge):
(1) a small Dockerfile that starts FROM the pinned OpenClaw image and keeps its entrypoint (the
docs warn a custom entrypoint skips a startup step); (2) a render.yaml adapted from OpenClaw's,
using runtime: docker so Render builds from their repo, branch main, and autoDeployTrigger:
commit (deploy on each commit to main; the default for new services). Render can't reach the disk
during the build, so the workspace files can't be copied into /data at build time: a small start
step copies the files the student owns (AGENTS.md, SOUL.md, USER.md, IDENTITY.md, skills/) from the
image into /data/workspace on each start, and leaves the agent's own files (MEMORY.md, memory/)
alone. The rule to teach: the repo owns the instructions; the disk owns the memory. Without that
split, a redeploy would overwrite what the agent has learned.

Then in Render: New → Blueprint → pick their repo → set the model key in Dashboard → Environment
(never in the repo; .env is already gitignored) → deploy. The Control UI is at
https://<service>.onrender.com/, connected with the gateway token (Dashboard → service →
Environment); Dashboard → service → Shell opens a shell with the disk at /data. Local settings in
~/.openclaw (model key, paired channels) don't carry over and shouldn't be in the repo, so they
pair the chat app again on the deployed instance.

Cost decides the plan. Free web services can't attach a disk and spin down after 15 minutes without
traffic; without a disk, OpenClaw's state and the agent's memory reset on every deploy (for a free
demo the disk block is removed from render.yaml). An agent they keep needs Starter: $7/month plus
$0.25 per GB per month for the disk (render.com/pricing, September 2026), about $7.25 for 1GB. One
more bill, separate from the model provider.

Redeploys and secrets. Every commit to main redeploys, which is why branch, test, approval, merge
matters: main is what runs. Env var changes: Render offers "Save, rebuild, and deploy", "Save and
deploy", or "Save only" (not used until the next deploy); a plain restart doesn't pick changes up.
Anything written outside /data is wiped on the next deploy.

Class-day trap: one bot, one agent. OpenClaw's Telegram channel uses long polling by default, and
Telegram allows only one way of receiving updates per bot, so a local Gateway and a Render Gateway
on the same token fight over messages (a getUpdates conflict). Turn off the laptop's agent once the
Render one is live, or give each its own bot.

The chain in the cloud. brief.py can run as a Render cron job from the same repo, with the agent as
the web service. A Render disk attaches to one service only, so the cron job can't write into the
agent's /data: in the cloud the brief goes to Drive or Dropbox and the agent reads it there. Once
hosted, both run with the laptop closed and webhooks become possible.

## When it breaks

No Sessions page does this for them. First check: is the Gateway running (`openclaw gateway
status`)? Config changes only take effect after a Gateway restart (`openclaw gateway restart`).
Then `openclaw status` (channels, sessions, usage), `openclaw
doctor` (and `--fix`), `openclaw logs --follow`, and the Control UI's session transcripts. The
move from the Class 1 prereqs: describe the symptom and let Claude Code dig ("My 7:30 run didn't
come. Check OpenClaw's status and logs and tell me why."), then fix the cause on a branch. Common
causes: laptop asleep, Gateway not running after a restart, a model key out of credit or rate
limited, a config typo `doctor` catches, a tool call waiting on an approval.

## Homework

Finish the chain until its handoff matches Class 5's. Connect every source the brief reads and
every app the agent acts in, one per branch:
the same MCP server or API it used in the Console, a trusted plugin or skill (read before installing), or a script tool. Watch cost daily for a week at each provider and trim anything that grew back.
Then decide: move it to Render, or go back to the Managed Agents chain if that did the job; either is
right under the simplest-setup rule. Help fully with mechanics; what it may do, which model, and
whether it's worth owning are their calls.

## You shipped it

Recap of the course's end state: the decision (Cowork first, Managed Agents next, OpenClaw only
when a job needs it); the chain rebuilt (the brief as a plain Python automation with no agent,
the agent in a cleaned-out OpenClaw acting on it); a chat they can message the agent in; code in GitHub changed only by
branch, review, merge, keys kept out. The rules that travel to any surface: dictate the
deliverable, one job per agent, cap what it can spend, use the simplest setup that works.

# Teaching notes — Advanced Class 4 (Automations in Managed Agents)

Per-slide notes for the bot view. `##` = slide label. Private. Teach the skill, don't
perform the build. The student is comfortable with Claude and Cowork but has not written
code. Today they rebuild the morning brief in Claude Managed Agents in the Claude Console
(platform.claude.com): a custom skill (steps plus a script) holds the dictated steps, both drafted in
Quickstart along with the agent that holds what matters to them, logins live in a credential vault,
and a scheduled deployment runs it with a per-run budget. The brief lands in Google Drive or
Dropbox. Managed Agents is a beta product whose Console screens change: search the current
docs (platform.claude.com/docs/en/managed-agents) before directing any click. The rules that
never slide: keys go only in the vault, never in a chat, skill, or prompt; tools a
scheduled run uses must be set to always allow (MCP tools default to always ask, and an
unattended run that asks waits forever); every tool that writes, sends or deletes, other
than the one that saves the brief, is turned off.

## The arc

The map of the whole Advanced mini course, so the student sees how the three classes stack before starting. Class 4 (today, Managed Agents): an automation, with dictated steps (a script plus one judgment call) writing the morning brief, triggered by a schedule. Class 5 (Managed Agents): an agent built field by field in Create agent; the same skill is attached, but now the agent decides when to run it, acts on what it finds, and rewrites the brief into Taken care of / Needs your action / FYI. Class 6 (VS Code with Claude Code): the agent rebuilt in OpenClaw, where they own the code: custom tools that run their own code, any model, and webhooks that wake it up; class covers setup and getting it running, and homework finishes it. Nothing is thrown away between classes. Two rules run through all three: cap spend before anything runs, and use the simplest deployment that does the job (a Cowork project if it can run there, Managed Agents for simple agents, OpenClaw only when an agent needs heavy customization). If a student asks whether they need Class 6, the honest answer is that most agents don't; it's for when they do.

## The finish line

Show the destination: the same morning brief they may already have in Cowork, rebuilt so every part is visible and controllable. The pitch is control, not novelty: fixed steps in code, one judgment step, a spend cap per run, and a transcript of every run. If a student asks "why rebuild something that works?", the answer is that Cowork's task is a black box that does its best with sentences; this version is one they can inspect, cap and harden, and it's the foundation Class 5's agent is built on.

## The map

This slide answers a question advanced students ask: which Claude surface is for what. Use Anthropic's own definitions (quoted from support.claude.com and the docs). Chat: conversations that can "search through your previous conversations" and "remember context from your chats" (the "Search and reference chats" and "Generate memory from chats" settings; memory is on by default on Free, Pro and Max, excludes chats inside projects). Chat works in an isolated sandbox: it creates files and artifacts you download, but can't read or edit files on your computer. Projects: "self-contained workspaces with their own chat histories and knowledge bases." Artifacts: "anything Claude makes for you that you'd put in front of someone: a design, a deck, a document, a dashboard, or a small interactive tool." Cowork: "the same agentic architecture that powers Claude Code, with no terminal required"; it takes on multi-step tasks and executes them, reading and writing local files, with connectors and scheduled tasks. Claude Code: "an agentic coding tool that reads your codebase, edits files, runs commands, and integrates with your development tools" (Class 6). Managed Agents: a "pre-built, configurable agent harness that runs in managed infrastructure" (today and Class 5). The distinction to land: a project is a workspace; an artifact is a finished thing Claude produces for you to share. (Chat vs Cowork is on the cards: Chat makes things for you to download; Cowork works on your actual files.) Anthropic is rolling out a merged Chat-and-Cowork experience, so a student may see them as one conversation; if so, explain the difference as "making things for you" versus "working in your files and accounts," which still holds. Don't turn this into a feature tour; the point is choosing the right home for a job.

## Why Managed Agents

The four things they get that Cowork doesn't expose: exact cron schedules, a hard dollar cap per run, any service with a remote MCP server or an API key, and a full session transcript per run. Be honest about the trade: it's a separate Console account billed by usage (not their Claude plan), and setup takes more clicks. A daily brief on a Sonnet model is roughly a few dollars a month; don't promise a precise figure.

## The key question

The core concept, taught one level deeper than the Beginner track. An automation's steps are DICTATED: the agent follows them and doesn't choose, so its autonomy is taken away on purpose. (Not "the steps are taken away"; the steps are fully specified and the agency is removed.) Every fixed step is dictated; what differs is who carries it out. Exact tool calls reach the apps: one named MCP tool with fixed inputs, to read a source or save the brief; Claude makes the call, but there is nothing to decide. A script does the pure computing: counting, date math, formatting, where code gives the same answer every run for almost nothing and can be tested. Judgment is used only where no rule can decide, which is "what needs me today." The student does not write code; Claude writes the script. Don't frame code as always better than a tool call: a script reaching an app needs its own API token and access set up (see the vault), while an MCP tool call is the normal way to reach an app. A script calling an API is the fallback for an app with no MCP server.

## The parts

Map each Managed Agents object to what they know from Cowork, so nothing feels foreign: skill = the task's steps; agent = the project and its instructions (model, system prompt, tools); MCP servers and APIs = connectors (an MCP server is the usual connection; an app with no MCP server is reached through its API from the script, with its token in the vault); credential vault = signing in to a connector; environment = the cloud computer each run gets (Cowork handles this invisibly); deployment = the scheduled task. A session is the record of one run. If a student wants to know where memory stores fit, say they come in Class 5.

## Before you start

This slide is the class PREREQUISITE: students do it before class (it is listed on the course page). In class, only confirm it: they can sign in to the Console, credits are loaded, and Managed Agents shows in the sidebar. If a student arrives without it, get the account and credits done first; nothing else in the build works without it. The Console is a separate account from the Claude app plan: platform.claude.com, a card on file, $10 of prepaid credits with auto-reload left off (the hard ceiling from the next slide). Managed Agents is enabled by default for API accounts (it's beta, no waitlist). Pricing: model tokens at API rates plus $0.08 per session-hour, counted only while a run is working. Viewing session transcripts needs the Developer or Admin role in the workspace; on a personal account they are the admin. If a student handles sensitive client data, mention that Managed Agents isn't covered by zero-data-retention agreements, and let them decide what to connect.

## Cost control

Cost control is a thread through every Advanced class; this is where it starts, before anything runs. The fear is real: people do wake up to four-figure API bills. The cause is almost never one expensive run; it's a cheap run multiplied: a cron typo, an agent retrying in a loop, a leaked key. Three levels of limits, set before the first run: per run (the deployment budget, $1, which pauses the run at the cap), per month (a spend limit on the Console workspace), and the hard ceiling (prepaid credits with auto-reload off, so nothing can spend money that wasn't loaded). Walk them through finding the workspace spend limit and the auto-reload setting in the current Console; search the docs if the screens have moved. The concrete trap: `* 7 * * 1-5` is every minute from 7:00 to 7:59, sixty runs a morning; `0 7 * * 1-5` is once at 7:00. Always read the upcoming runs the Console lists. Close on the through-line of the Advanced track, simplicity and cost control: Cowork runs on the Claude subscription, not the API, so it has no usage bill to cap. If a Cowork project can do a job, that is the better home; Managed Agents is for when they need what only it offers (exact schedules, per-run caps, any API, inspectable runs). The same rule carries to Class 6: use the simplest deployment that does the job. Other cost levers worth naming if asked: a Sonnet model instead of Opus, scripts instead of model reasoning for fixed steps, pulling only what the brief needs, web searches ($10 per 1,000), and scheduling no more often than the job needs.

## Step 1 · Describe it

The whole build starts in the Console: Managed Agents → Quickstart, where the student pastes the prompt and Quickstart interviews them and drafts the agent and its skill. Coach the interview, not the code: which three sources, and exactly what to pull from each so it's the same every morning. Push for exact rules ("unread from clients, last 24 hours"), not vague ones ("check my email"). Check the output: a skill named morning-briefing (lowercase, hyphens, no "claude" or "anthropic") with every step in order, tagged exact tool call / script / judgment, and only one judgment step (tool calls to reach apps, the script for counting, dates and formatting); the script alongside it; a system prompt saying what matters to them; and the list of MCP servers, API tokens, packages and websites, used in the vault and environment steps. The honesty rules (say what failed at the top; write "all clear" on a quiet day) belong in the skill. If Quickstart doesn't produce the skill and script itself in their Console, check the current docs for how to add a custom skill to the workspace (custom skills can be uploaded as a zip or files) and attach it to the agent. Source choice is where most trouble starts: Google's official Gmail, Calendar and Drive MCP servers are a Developer Preview that needs a Google Cloud project and an OAuth client, which is heavy for this audience. Services with simple OAuth MCP servers (Slack, Notion, and others) are much easier. Search for the service's current remote MCP server before promising one. Start with three sources or fewer.

## Step 2 · The agent

Quickstart fills in the agent's fields; the student checks each rather than trusting the draft: model (a Sonnet model is plenty and cheaper than Opus), system prompt (what "matters" means to them; the judgment step's rulebook, equivalent to Cowork project instructions), MCP servers (every one on the list; their permissions are the next slide), and the morning-briefing skill attached with its script. Why a skill rather than a long prompt: it loads only when needed, and the script runs as code with only its output entering context. Changing the brief later means changing the skill; the agent and deployment stay. If a field is wrong, they edit the agent. Create agent, the field-by-field form, is Class 5's opener; don't teach it in depth today.

## Step 3 · The vault

Credential vaults hold every login and key: OAuth or a bearer token for each MCP server (matched to the server URL), and environment-variable secrets for the script. The mechanism to explain: the run holds only a placeholder, and the real secret is substituted as the request leaves the sandbox, so the agent never sees it. Practical consequences if a script fails auth: the script must send the token as-is in a request header; credentials created in the Console inject into headers only unless body injection is enabled on the form; and the credential's allowed hosts and the environment's networking must both allow the host. Vaults are shared across the workspace. Hold the line firmly: keys go only in the vault. If a student starts to paste a key into a chat (including to you), stop them and redirect to the vault.

## No one's watching

The permission teach, specific to unattended runs. Built-in tools default to always allow; MCP toolsets default to always ask; an always-ask call in a scheduled run pauses the session indefinitely (idle, requires action), so the brief never arrives. Auto lets the server decide per call and can still pause, so it isn't safe unattended either. What to set: always allow for the reading tools the skill names and the one save tool; turn off every other write, send or delete tool. There is no "never" policy: turning a tool off (disabling it on the agent) is the lock, and the agent can't call it at all. Contrast with a prompt instruction, which is a request.

## Step 4 · The environment

Each run gets a fresh cloud sandbox configured by the environment. Two settings: packages (pip and others) the script needs, installed before the run and cached; networking, where limited means only listed hosts plus an allow-MCP-servers switch and an allow-package-managers switch. Environments made in the Console may default to limited, which is the usual cause of "host blocked" errors: add the host, or enable MCP server access. Nothing in the sandbox survives the run, which is why the brief is saved to Drive or Dropbox.

## Step 5 · Prove it

Run it once in the test session and read the transcript: the skill loading, the script running, each tool call and result. Four checks: the transcript shows the dictated steps in order; "needs you today" looks right (fix the system prompt, not the brief); the file is really in Drive or Dropbox; and the run's cost, shown on the session, times about 22 weekdays is roughly their monthly bill. If that number surprises them, fix it now (model, how much it reads) before it's on a schedule. Name the principle: a tool call that says "saved" isn't the same as a file existing. If something fails, read the failing step in the transcript and describe it to Claude; common causes are a tool left on always ask, a blocked host, a missing package, or a vault credential that doesn't match the server URL.

## Step 6 · Schedule it

Deployments (Managed Agents → Deployments) bind agent, environment and vault to a cron schedule and time zone, with a prompt sent at each run and an optional budget copied onto every run. Cron is five fields: minute, hour, day of month, month, day of week; `0 7 * * 1-5` is weekdays at 7:00. The Console validates it and shows upcoming runs. Runs can start up to 9 minutes late (jitter). Avoid 1 to 3am because of daylight-saving changes. The budget is a hard cap: at the cap the run pauses (budget reached) rather than being killed, and raising the cap resumes it. Run now tests the deployment immediately; insist on it, and have them read the upcoming runs to confirm the schedule means what they think (the cost-control slide's cron typo). Confirm the current form fields in the Console before directing them.

## When it breaks

Four layers of honesty: the brief names any source it couldn't reach at the top; it writes "all clear" on quiet days so a missing brief means breakage; every run is a session under Managed Agents → Sessions with status, cost and full transcript; the budget pauses a runaway run, and a deployment whose run can't start (for example an archived vault or environment) pauses itself, and missed runs aren't made up. The upgrade over Cowork: diagnose by reading the run, not by guessing.

## Homework

Two tasks. Add one source that makes the brief theirs (vault credential, server or token, one step in the skill, run once). Harden one step: find something Claude still works out on every run (sorting, counting, formatting) and ask whether a script can do it instead, then update the skill and run once. Help fully with the mechanics; the choices (which source, which step to harden) are theirs.

## You shipped it

Recap: a skill with dictated steps (tool calls to reach apps, code for the computing, one judgment call), logins in a vault the agent never sees, tools set to always allow or turned off so unattended runs never stall, a deployment with an exact schedule and a record of every run, and spend capped at three levels: per run, per month on the workspace, and by the prepaid credits. The bridge to Class 5: the trigger moves. They build an agent with Create agent, attach this same skill, and the agent decides when to run it instead of the clock, then acts on what it finds. The line to leave them with: an automation has its steps dictated; an agent chooses its own.

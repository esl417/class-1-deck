# Teaching notes — Advanced Class 4 (Automations in Managed Agents)

Per-slide notes for the bot view. `##` = slide label. Private. Teach the skill, don't
perform the build. The student is comfortable with Claude and Cowork but has not written
code. Today they rebuild the morning brief in Claude Managed Agents in the Claude Console
(platform.claude.com): a custom skill (SKILL.md plus a script) holds the dictated steps, an
agent made with Quickstart holds what matters to them, logins live in a credential vault,
and a scheduled deployment runs it with a per-run budget. The brief lands in Google Drive or
Dropbox. Managed Agents is a beta product whose Console screens change: search the current
docs (platform.claude.com/docs/en/managed-agents) before directing any click. The rules that
never slide: keys go only in the vault, never in a chat, skill, or prompt; tools a
scheduled run uses must be set to always allow (MCP tools default to always ask, and an
unattended run that asks waits forever); every tool that writes, sends or deletes, other
than the one that saves the brief, is turned off.

## The finish line

Show the destination: the same morning brief they may already have in Cowork, rebuilt so every part is visible and controllable. The pitch is control, not novelty: fixed steps in code, one judgment step, a spend cap per run, and a transcript of every run. If a student asks "why rebuild something that works?", the answer is that Cowork's task is a black box that does its best with sentences; this version is one they can inspect, cap and harden, and it's the foundation Class 5's agent is built on.

## The map

This slide answers a question advanced students ask: which Claude surface is for what. Chat is one conversation. A project is a home for one job (files and instructions every chat in it reads). An artifact is a thing Claude produces for you to use or share (a doc, a page, a small app); it is output, not a workspace. Cowork is Claude working in your files and accounts with connectors and scheduled tasks, no code. Claude Code builds software in a folder of files (Class 6). Managed Agents are agents configured field by field and run in Anthropic's cloud (Classes 4 and 5). The one-line distinction to land: a project is where the work lives; an artifact is something the work produces. Don't turn this into a feature tour; the point is choosing the right home for a job.

## Why Managed Agents

The four things they get that Cowork doesn't expose: exact cron schedules, a hard dollar cap per run, any service with a remote MCP server or an API key, and a full session transcript per run. Be honest about the trade: it's a separate Console account billed by usage (not their Claude plan), and setup takes more clicks. A daily brief on a Sonnet model is roughly a few dollars a month; don't promise a precise figure.

## The key question

The core concept, taught one level deeper than the Beginner track. An automation's steps are DICTATED: the agent follows them and doesn't choose, so its autonomy is taken away on purpose. (Not "the steps are taken away"; the steps are fully specified and the agency is removed.) Three forms a step can take, strongest first: a script (code; same result every run, near-free, testable), an exact tool call (one named MCP tool with fixed inputs, carried out by Claude but with nothing to decide), and judgment (only where no rule can decide, which is "what needs me today"). Why prefer code: consistency and cost, and a script's output is all that reaches Claude. The student does not write code; Claude writes the script. Which steps can be scripts depends on the service: one that offers a personal API token sent in a header works well from a script; Google's OAuth-based services generally don't, so those stay exact tool calls through an MCP server.

## The parts

Map each Managed Agents object to what they know from Cowork, so nothing feels foreign: skill = the task's steps; agent = the project and its instructions (model, system prompt, tools); MCP servers = connectors; credential vault = signing in to a connector; environment = the cloud computer each run gets (Cowork handles this invisibly); deployment = the scheduled task. A session is the record of one run. If a student wants to know where memory stores fit, say they come in Class 5.

## Before you start

The Console is a separate account from the Claude app plan: platform.claude.com, a card on file, a small credit purchase. Managed Agents is enabled by default for API accounts (it's beta, no waitlist). Pricing: model tokens at API rates plus $0.08 per session-hour, counted only while a run is working. Viewing session transcripts needs the Developer or Admin role in the workspace; on a personal account they are the admin. If a student handles sensitive client data, mention that Managed Agents isn't covered by zero-data-retention agreements, and let them decide what to connect.

## Step 1 · Write the skill

The student maps their morning with Claude in the Claude app (Chat or Cowork) and Claude writes the skill. Coach the interview, not the code: which three sources, and exactly what to pull from each so it's the same every morning. Push for exact rules ("unread from clients, last 24 hours"), not vague ones ("check my email"). Check the output: SKILL.md with `name` (lowercase, hyphens, no "claude" or "anthropic") and `description` frontmatter, steps in order with every step tagged script / exact tool call / judgment and only one judgment step; a script in a scripts folder; the list of MCP server URLs, API tokens, packages and websites; a zip. The honesty rules (say what failed at the top; write "all clear" on a quiet day) belong in the skill. Source choice is where most trouble starts: Google's official Gmail, Calendar and Drive MCP servers are a Developer Preview that needs a Google Cloud project and an OAuth client, which is heavy for this audience. Services with simple OAuth MCP servers (Slack, Notion, and others) or personal API tokens (Todoist and similar) are much easier. Search for the service's current remote MCP server before promising one. Start with three sources or fewer.

## Step 2 · Upload the skill

Custom skills are uploaded to the Console workspace as a zip (or files) and shared by every agent in it. Skills uploaded on claude.ai do not sync to the Console. Confirm the current upload location in the docs before directing them. Why a skill rather than a long prompt: it loads only when needed, and the script runs as code with only its output entering context. Changing the brief later = ask Claude to edit the skill, upload the new version; the agent and deployment stay.

## Step 3 · The vault

Credential vaults hold every login and key: OAuth or a bearer token for each MCP server (matched to the server URL), and environment-variable secrets for the script. The mechanism to explain: the run holds only a placeholder, and the real secret is substituted as the request leaves the sandbox, so the agent never sees it. Practical consequences if a script fails auth: the script must send the token as-is in a request header; credentials created in the Console inject into headers only unless body injection is enabled on the form; and the credential's allowed hosts and the environment's networking must both allow the host. Vaults are shared across the workspace. Hold the line firmly: keys go only in the vault. If a student starts to paste a key into a chat (including to you), stop them and redirect to the vault.

## No one's watching

The permission teach, specific to unattended runs. Built-in tools default to always allow; MCP toolsets default to always ask; an always-ask call in a scheduled run pauses the session indefinitely (idle, requires action), so the brief never arrives. Auto lets the server decide per call and can still pause, so it isn't safe unattended either. What to set: always allow for the reading tools the skill names and the one save tool; turn off every other write, send or delete tool. There is no "never" policy: turning a tool off (disabling it on the agent) is the lock, and the agent can't call it at all. Contrast with a prompt instruction, which is a request.

## Step 4 · The agent

Quickstart (Managed Agents → Quickstart) builds an agent from a description and shows each field; it includes a test session. Have them check the fields rather than trust the draft: model (a Sonnet model is plenty and cheaper than Opus), system prompt (what "matters" means to them; this is the judgment step's rulebook, equivalent to Cowork project instructions), MCP servers with permissions set as on the previous slide, and the morning-briefing skill attached. If Quickstart doesn't attach a custom skill or an MCP server correctly, they can edit the agent afterwards. Create agent, the field-by-field form, is Class 5's opener; don't teach it in depth today.

## Step 5 · The environment

Each run gets a fresh cloud sandbox configured by the environment. Two settings: packages (pip and others) the script needs, installed before the run and cached; networking, where limited means only listed hosts plus an allow-MCP-servers switch and an allow-package-managers switch. Environments made in the Console may default to limited, which is the usual cause of "host blocked" errors: add the host, or enable MCP server access. Nothing in the sandbox survives the run, which is why the brief is saved to Drive or Dropbox.

## Step 6 · Prove it

Run it once in the test session and read the transcript: the skill loading, the script running, each tool call and result. Three checks: the transcript shows the dictated steps in order; "needs you today" looks right (fix the system prompt, not the brief); the file is really in Drive or Dropbox. Name the principle: a tool call that says "saved" isn't the same as a file existing. If something fails, read the failing step in the transcript and describe it to Claude; common causes are a tool left on always ask, a blocked host, a missing package, or a vault credential that doesn't match the server URL.

## Step 7 · Schedule it

Deployments (Managed Agents → Deployments) bind agent, environment and vault to a cron schedule and time zone, with a prompt sent at each run and an optional budget copied onto every run. Cron is five fields: minute, hour, day of month, month, day of week; `0 7 * * 1-5` is weekdays at 7:00. The Console validates it and shows upcoming runs. Runs can start up to 9 minutes late (jitter). Avoid 1 to 3am because of daylight-saving changes. The budget is a hard cap: at the cap the run pauses (budget reached) rather than being killed, and raising the cap resumes it. Run now tests the deployment immediately; insist on it. Confirm the current form fields in the Console before directing them.

## When it breaks

Four layers of honesty: the brief names any source it couldn't reach at the top; it writes "all clear" on quiet days so a missing brief means breakage; every run is a session under Managed Agents → Sessions with status, cost and full transcript; the budget pauses a runaway run, and a deployment whose run can't start (for example an archived vault or environment) pauses itself, and missed runs aren't made up. The upgrade over Cowork: diagnose by reading the run, not by guessing.

## Homework

Two tasks. Add one source that makes the brief theirs (vault credential, server or token, one step in the skill, run once). Harden one step: find an exact tool call and ask Claude whether a script can do it instead, then upload and run once. Help fully with the mechanics; the choices (which source, which step to harden) are theirs.

## You shipped it

Recap: a skill with dictated steps (code where possible, one judgment call), logins in a vault the agent never sees, tools set to always allow or turned off so unattended runs never stall, and a deployment with an exact schedule, a hard cap and a record of every run. The bridge to Class 5: the trigger moves. They build an agent with Create agent, attach this same skill, and the agent decides when to run it instead of the clock, then acts on what it finds. The line to leave them with: an automation has its steps dictated; an agent chooses its own.

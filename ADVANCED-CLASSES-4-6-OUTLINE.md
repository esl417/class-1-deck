# Advanced Classes 4 to 6: Outline

Status as of 2026-09-30: all three decks are done, live and linked from the hub, built alongside
Eric's own runs. This doc describes what the decks actually present; the decks themselves
(`index.html` + `teaching.md` in each folder) are the source of truth for exact wording.

| Class | Folder | Slides | Surface |
|---|---|---|---|
| 4 · Automations | `advanced-class-4-automations/` | 19 | Claude Managed Agents (Claude Console) |
| 5 · Agents | `advanced-class-5-agents/` | 19 | Claude Managed Agents (Create agent) |
| 6 · OpenClaw | `advanced-class-6-openclaw/` | 29 | VS Code + Claude Code + OpenClaw |
| 6 · Prereqs | `advanced-class-6-openclaw/prereqs.html` | 19 | Before-class setup |

**Numbering (2026-09-30):** the decks now label themselves Class 1, 2 and 3 to match the Maven course (Build an AI Agent with Claude Code). Folder names and URLs keep 4 to 6; this doc still says Class 4 to 6 in places.

The Beginner track (`class-4-automations`, `class-5-agents-beginner`,
`class-6-the-loop-beginner`, `CLASSES-5-6-OUTLINE.md`) is separate and untouched.

## Who it's for

Students already comfortable with Claude: they use Cowork and may run small agents there, but
haven't touched code. First paid student: a creative director at an agency who lives in Slack,
develops processes and manages 18 direct reports. Skip what Beginner teaches (what a connector
or an agent is); spend the time on control surfaces, cost and choosing the right surface.

## The arc

| | Class 4 | Class 5 | Class 6 |
|---|---|---|---|
| Idea | Automation: the steps are dictated | Agent: the deliverable is dictated | Own the code |
| What runs | A 7:00 deployment writes the brief | A separate 7:30 agent acts on it | The same chain, rebuilt on your machine |
| Output | Morning brief in Drive/Dropbox | Handoff: Taken care of / Needs your action / FYI | Same handoff, also sent to a chat app |

## Rules that run through all three

- **Cost control in every class.** Only the Advanced track bills by API usage. Class 4 has its
  own cost slide (per run, per month, prepaid ceiling, the cron typo); Class 5 adds "agents cost
  more" and two parts, two bills; Class 6 moves the caps to the model provider and makes token
  overhead the lever.
- **Use the simplest setup that does the job.** Cowork runs on the subscription with no usage
  bill; Managed Agents next; OpenClaw only when a job needs it.
- **Automation vs agent.** Automation = steps dictated (autonomy taken away). Agent = the
  deliverable/outcome dictated, it chooses the steps. A skill is not a tool.
- **Separation of duties / the chain.** One job per agent; the 7:00 brief (an automation) hands
  a file to the 7:30 agent; each link has its own model, cap and record.
- **Keys** only in a vault (Managed Agents) or `.env` / environment variables (Class 6), never in
  a chat. The agent drafts; the student sends.
- **Paste-in prompts are self-contained and plain:** no "Class 5"/"Step 5" references, say what
  not how, placeholders highlighted; any terminal command says "in a new VS Code terminal".

## Class 4 · Automations (Managed Agents)

Title: "Your morning brief, rebuilt in Managed Agents."

**Framing:** the arc; the finish line (brief on a schedule); **the map** of six Claude surfaces
(Chat, Projects, Artifacts, Cowork, Claude Code, Managed Agents, with Anthropic's definitions;
answers artifacts vs projects); **why Managed Agents** (exact schedules, a hard cap per run, any
service with an MCP server or API key, every run on the record; billed separately).

**Core teach, the key question:** dictate the steps, keep one judgment call. Exact tool calls
reach the apps, a script does counting/dates/formatting, judgment only for "what needs me today".
**The parts:** six parts and what each was in Cowork.

**Before class:** a Claude Console account (platform.claude.com), $10 credits, auto-reload off.
Pricing: model usage plus $0.08 per session-hour.

**Cost control slide:** per run (Quickstart sets $5, lower to $1 on the deployment), per month
(workspace spend limit), hard ceiling (prepaid credits). The typo: `* 7 * * 1-5` = 60 runs a
morning; `0 7 * * 1-5` = once. Cowork runs on the subscription instead.

**Build:** Step 1 describe the brief to **Quickstart** (it interviews, drafts the agent and the
morning-briefing skill, sorts each step into tool call / script / judgment); Step 2 check every
field; Step 3 environment (packages, limited networking); Step 4 the vault (just Connect for most
apps; client ID/secret only if Connect fails; API tokens as secrets); Step 5 test-run in the
panel and debug; Step 6 deployment (`0 7 * * 1-5`, time zone, "Run the morning-briefing skill
exactly as written.", budget $1, check upcoming runs, don't Run now yet); Step 7 permissions
(always allow the reading tools and the save tool, turn off every other write/send/delete tool,
then Run now). **When it breaks:** the session is the stack trace. **Homework:** add a source and
tune the brief. Close: next class an agent acts on this brief; the automation keeps running.

Known gap, left as is when Eric called the deck done: the deck teaches a script inside the skill,
but Eric found Python tools can't really be built in the Console.

## Class 5 · Agents (Managed Agents, Create agent)

Title: "An agent that works your brief before you read it."

**Framing:** the arc; the finish line (three lists); **two jobs, two parts** (the Class 4
deployment keeps running at 7:00; the agent is a separate part at 7:30; never pause Class 4).

**Mental model:** **Tools** (built-in, MCP servers, API calls; Python scripts as tools arrive in
Class 6); **Custom tools** need your code running somewhere (name/description/schema only; the run
waits for your own app, which the Console can't host); **Cost** (agents cost more, two parts two
bills, subagents multiply); **The chain** diagram (brief agent/automation → brief → action agent →
handoff → hypothetical wrap-up; one job per agent; strictly an automation handing off to an
agent); **The deliverable** (dictate the deliverable, not the steps).

**Build in Create agent:** Step 1 General (system prompt template that points to handoff-log.md
for memory and directions, names the folder, dictates the three-section deliverable and limits;
stronger model here); Step 2 Tools (always allow what the deliverable needs; send and delete
turned off); Step 3 Skills and Multiagent left empty on purpose (subagents ≠ the chain). **How it
remembers:** handoff-log.md in the briefing folder (no memory store; the first run creates it;
the system prompt is the student's, the log is the agent's). Step 4 test run (start a session
with the briefing's vault, "Handle my morning.", act-then-verify); Step 5 second deployment
`30 7 * * 1-5`, prompt "Handle my morning.", budget, Run now.

**Reach it remotely:** Managed Agents has no messaging channel. Three ways: a Cowork project (the
Claude app reaches it), the Slack polling workaround (costs per check, lags), or Class 6. The
lesson: in Managed Agents, build agents you don't need to message. **Tune what reaches you**,
**Homework** (a week of handoffs + the Class 6 prereqs, linked), close.

## Class 6 · OpenClaw (VS Code + Claude Code)

Title: "Your agent, rebuilt on code you own." Prereqs: `prereqs.html` (Class 1 prereqs minus
Vercel/Impeccable, plus the ant CLI logged in with the Console account), linked from the hub card
and Class 5.

**Choosing a surface:**
- **What OpenClaw is:** open-source, self-hosted; on a laptop it sleeps when the laptop does, on a
  rented server it runs around the clock; any model; lives in chat apps. You maintain everything.
- **Comparison table** (Cowork / Managed Agents / OpenClaw): who runs it, models, payment,
  token overhead (set by Anthropic vs yours to trim), customize, reach it, what wakes it, deploy,
  maintain, debug, security.
- **Decision tree**, three questions from the table, first yes decides: needs a non-Claude model →
  OpenClaw; an event must wake it (webhook) or it needs custom tools → OpenClaw; needs a service
  reached with an API key, not an MCP connector → Managed Agents; otherwise Cowork. OpenClaw
  answers bring the maintain and security rows with them. Note: consumer agents (xAI's Grok Bot,
  Meta's Muse) are coming; after this class you can build anything. Messaging is deliberately not
  a question (Cowork can be messaged).
- **Cost:** no per-run budget field; caps at each provider; overhead (workspace files, skill
  list, tool list) rides every call; the heartbeat (every 30 min by default) resends the whole
  chat history each wake; a leaked key is a blank check.

**What's inside OpenClaw:** the parts map (each Managed Agents part → its OpenClaw home; MCP
servers and API calls stay MCP servers and API calls); the workspace files (AGENTS, SOUL, USER,
IDENTITY, MEMORY loaded every call; memory/, HEARTBEAT, TOOLS not); the Gateway (always-on
program; whoever reaches it controls the agent; channels; pairing); tools, skills and permissions
(a Python script registered as a tool is how custom tools become real); what wakes it (message,
heartbeat, schedule, webhook); any model (one command, a fallback, test before trusting; Eric runs
Kimi); security (read every skill: 341 malicious skills on ClawHub, Feb 2026; keep the Gateway
private; keys never in a chat; update).

**GitHub:** git words (git, repo, commit, push, pull, clone, branch, merge) and saving and pushing
(commit to save, push to back up, merge to make it real; no live site, so push = backup).

**Install and onboarding (tested on OpenClaw 2026.9.7):**
- Create a **new API key just for this agent, with a spend limit**, in the Claude Console.
- **One Install prompt** does everything: official installer, private GitHub repo with a
  .gitignore for .env and the agent's memory files, the API key as an environment variable the
  onboarding terminal can see (the student pastes it into a file Claude opens; checked without
  showing it), then `openclaw onboard --classic --workspace "$PWD"` in a new VS Code terminal, and
  when the student says it's done: check health, fix anything risky, commit and push.
- **How it signs in:** API key (what we use: paid, capped, works on a server); CLI login
  (untested: failed in Eric's test; computer-only, eats the subscription, can be blocked);
  setup-token (never: prohibited by Anthropic's terms). Onboarding offers to use the existing
  ANTHROPIC_API_KEY: yes. Other providers have the same CLI-vs-API-key split.
- **Finish onboarding:** pick a chat app in the wizard (Telegram simplest; a work Slack may need
  an admin), approve the pairing code; No to importing memories; skip the search provider; skip
  missing skill dependencies (Space to select, then Enter). The chat app is connected here, not
  in a separate step.

**Build (five steps):**
1. **Clean it out** (measure with `/context detail` in the Control UI before and after): strip
   boilerplate from the workspace files (keep the red lines and memory rule), turn off every
   skill (bundled or from other tools on the computer), turn off every tool except read/write/edit
   of its own files (shell and web search off), heartbeat off, commit and push.
2. **Bring in your agents:** `ant` downloads the briefing agent (with its skill) and the action
   agent into export/; the action agent is translated into USER/AGENTS/SOUL/MEMORY; every app is
   reconnected (same MCP servers; API keys pasted into .env by the student), each tested by having
   the agent use it. Google apps need a Google client (Claude walks them through it); set its
   publishing status to **In production, not Testing**, or the sign-in expires every 7 days. An
   "unverified app" warning is expected.
3. **Model and keys:** main model plus a fallback; .env from Step 2; ask before every commit
   whether anything secret is in it.
4. **The brief, in Python, on a branch:** the brief is an automation, so it's **plain Python with
   no OpenClaw** (code for the dictated steps, one cheap model call for the judgment, saved to
   briefs/). The same script is registered as a tool, **morning_briefing**, so the agent can rerun
   it on request. Branching explained on the slide; **nothing merges until the student approves
   the test brief.**
5. **Schedule the chain:** brief.py at 7:00 on the computer's own scheduler; an OpenClaw
   automation at 7:30 ("Handle my morning.") saves the dated handoff to Drive/Dropbox (reachable
   from anywhere) and sends it in the chat app; list the next run times to catch typos. Then pause
   both Managed Agents deployments. Heartbeat stays off. Test the tool: "Rerun my brief."

**After the build:** webhooks (concept; need an internet-reachable address, so they come with
hosting); **to the cloud** (Render explained, not done: sign up with GitHub, link the class repo,
every push to main redeploys; the repo needs a small Dockerfile from the official OpenClaw image
plus a render.yaml; the repo owns the instructions, the disk owns the memory; Starter plan with a
disk; turn off the laptop's agent so two agents don't fight over one bot; unverified as a whole,
dry-run before recommending); when it breaks (gateway status first, doctor, logs, restart after
config changes; describe the symptom to Claude Code); homework (connect every app, watch cost for
a week, then decide Render or back to Managed Agents); close (the decision, the chain rebuilt,
branch-test-approve-merge, same rules anywhere).

**Dropped on purpose:** second-AI (Codex) code review (no extra AI coder to install); a separate
chat-app step (onboarding does it); a second chat app (one chat app per agent).

## Infrastructure

Each deck is static HTML with a `teaching.md` (labels match `data-label` exactly) compiled into
`llm.md` by `build-llm.mjs`; `infra/worker.js` BOT_VIEWS serves `llm.md` to AI crawlers (deploy
with `cd infra && npx wrangler deploy` after route changes). Vercel deploys on push. This file is
in `.vercelignore`.

## Open

1. Class 4 still teaches a script inside the skill although Python tools can't be built in the
   Console (left as is).
2. The shared bot-view preamble (`llm-preamble.md`) describes a non-technical small-business owner
   and a Class 6 "Go-to-market", which doesn't fit the Advanced track.
3. Class 6's Render setup (own-repo Dockerfile + render.yaml + start step) hasn't been dry-run.

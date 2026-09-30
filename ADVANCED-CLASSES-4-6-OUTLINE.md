# Advanced Classes 4 to 6: Outline (working draft)

Status as of 2026-09-29. Class 4 deck done (advanced-class-4-automations/, built alongside
Eric's own run in the Console). Class 5 deck done 2026-09-30 (advanced-class-5-agents/), built alongside Eric's run.
Class 6 deck built 2026-09-30 (advanced-class-6-openclaw/, 27 slides), awaiting Eric's review; the Class 6
prereqs (ant CLI added) are linked from the hub and from Class 5's homework and close.
Open from Class 4: Eric noted Python tools can't be built in the Console, but the deck still
teaches a script inside the skill; left as is when he called the deck done. The
Beginner track (class-4-automations, class-5-agents-beginner, class-6-the-loop-beginner,
CLASSES-5-6-OUTLINE.md) is unchanged and stays as is.

## Who it's for

Students already comfortable with Claude: they use Cowork, may already run small agents
(the first paid student tracks flights, prices and home tasks in Cowork), but have not
touched code. They want Claude Code, want to understand the product surfaces (artifacts vs
projects etc.), and want agents in their workday. First student: a creative director at an
agency, lives in Slack, develops processes, manages 18 direct reports.

Skip what the Beginner track spends time on (what a connector is, what an agent is, how to
write instructions). Spend it on the control surfaces instead.

## The arc

| | Class 4 | Class 5 | Class 6 |
|---|---|---|---|
| Surface | Managed Agents (Console) | Managed Agents (Console) | VS Code + Claude Code |
| Core idea | Automation: steps dictated | Agent: it decides, and acts | Own the agent: OpenClaw |
| Who pulls the trigger | A deployment (timer) | The agent | The agent, plus outside events |
| Morning artifact | The brief | The brief, rewritten: Taken care of / Needs your action / FYI | Same agent, rebuilt on OpenClaw (finished as homework) |

**Why Managed Agents for 4 and 5:** it lays every control surface out as a field (model,
system prompt, tools, MCP, permission policy per tool, skills, subagents, deployments,
vaults, memory), so the concepts are visible rather than hidden behind an app. Its limits
(no custom tool code of your own in the cloud) are what motivate Class 6.

## Cost control: a thread through every class

Only the Advanced track bills by API usage, and surprise bills are the fear ("woke up to a
$2,100 API bill"); few competitors teach it. Every Advanced class has a cost beat.
- **Tied to simplicity:** Cowork runs on the Claude subscription, not the API, so it has
  no usage bill. Another reason to run agentic work in a Cowork project when it can do the
  job. Keep driving simplicity and cost control together in every class.
- **Class 4:** its own slide before anything runs. Three levels: per run (deployment
  budget), per month (workspace spend limit), the hard ceiling (prepaid credits,
  auto-reload off). The cron typo (`* 7 * * 1-5` = 60 runs a morning). Read each run's
  cost in its session; x22 weekdays = the monthly bill.
- **Class 5:** agents cost more than automations: they choose steps, retry, search, and
  spawn subagents (which multiply cost). Every session gets a budget.
- **Class 6:** **first thing after installing OpenClaw: clean it out.** Strip the default
  junk that adds overhead (boilerplate in the workspace files, bundled skills and
  plugins it doesn't need), because whatever is loaded rides along on every call and
  costs tokens every time. Exact list to decide when building the deck. OpenClaw runs on
  your own key with no Anthropic-side per-run cap, so the workspace limit and prepaid
  credits carry the weight. Heartbeat frequency is a cost
  setting. A key committed to GitHub is the classic surprise bill: `.env` in `.gitignore`
  before the first commit (ties to branching). Render bills separately.

## Class 4 Advanced: Automations

**Where:** Console → Quickstart ("describe what you need") to create the agent. Create
agent is saved for Class 5, where every field gets taught.

**Opener: the map.** Chat, projects, artifacts, Cowork, Claude Code, Managed Agents: what
each is for and when to reach for it. Answers "artifacts vs projects." Why go past Cowork:
schedules to the minute, a hard spend cap per run, any service with an API or remote MCP
server, a real sandbox, and every run kept as an inspectable session.

**Core teach, deterministic vs judgment:** an automation's steps are *dictated* for the
agent to follow; its autonomy is taken away. In Cowork a "fixed step" is still an English
sentence Claude executes. Here every fixed step is dictated, split by who carries it out:
**exact tool calls** (one named MCP tool, fixed inputs) reach the apps; a **script** does the
pure computing (counting, dates, formatting), same result every run for almost nothing;
**judgment** only for "what needs me today." Not "code wherever possible": reaching an app
from a script needs its own token and setup, so a script calling an API is the fallback for
an app with no MCP server. Quickstart writes the skill and script; the student doesn't.

**Build: the morning brief, done the robust way.** Conceptually simple, but the value is in
coding it, plugging in every source they want, and tailoring it.
- The student describes the brief in **Quickstart**, which drafts the agent and a
  **skill** (dictated steps plus a script). No separate app, no upload.
- A **deployment** runs it on a schedule with a per-run budget. Its prompt says: run the
  briefing skill, exactly these steps.
- Sources come in through MCP servers, credentials through a vault. Never in a prompt.
- **Output lands wherever they configure it; advise Google Drive or Dropbox** so it can be
  opened from anywhere.
- Honesty rules carry over from Beginner: say when a source failed; write a brief even on a
  quiet day.

## Class 5 Advanced: Agents

**Where:** Console → Agents → **Create agent**. The form is the syllabus: walk every
section.
- General: name, model and effort, description, system prompt.
- Tools: built-in tools (`agent_toolset_*`: bash, files, web search/fetch, etc.) with their
  permission policies (always allow / always ask / auto; disabling a tool is the "never").
  These are the preloaded tools to point at and introduce.
- MCP servers: their apps.
- **Custom tools: concept only.** Name, description, input schema — and the catch: when
  the agent calls one, *your own application* must run the code and send the result back.
  There is nowhere in the Console for that code to live, and a scheduled run would sit
  waiting. This is the surface's limit, shown on purpose; Class 6 removes it.
- Skills: left empty on purpose; the briefing skill stays with the Class 4 agent.
- Multiagent: subagents and advisors (introduce; stretch homework).

**Separation of duties (decided 2026-09-29, replacing "the trigger moves").** The Class 4
deployment keeps running unchanged at 7:00: small, segmented, managed. The Class 5 agent is
a separate part with its own deployment at 7:30 that finds the brief file and acts on it.
Each part is configured, capped and debugged on its own, so the brief can change without
editing the agent that acts. Don't pause the Class 4 deployment.
Its own slide right after cost ("The chain"): agents daisy-chained, each writing a file the
next reads; in Managed Agents each link gets its own model (cheaper model where power isn't
needed = cost control), low overhead, traceable per link, and new jobs are just new links.

**Reaching the agent remotely (slide "Reach it remotely"):** Managed Agents has no messaging
channel (researched 2026-09-30: webhooks are outbound only, the agent is only an MCP client;
Claude Tag can't run a Managed Agent). Teach three ways: 1) a Cowork project, which the Claude
app reaches natively (simplest); 2) the Slack workaround, a small scheduled agent that polls a
#requests channel (works, but costs per check and lags; the lesson is to build agents you
don't need to message); 3) Class 6, an OpenClaw agent on Slack or Telegram.

**Build: Beginner Classes 5 and 6 collapsed into one.** The agent picks up the report, acts on
it within the authority it's given, and writes a handoff in three sections: **Taken
care of / Needs your action / FYI.** That is what they read every morning. A full agent.
The agent's system prompt dictates the deliverable (outcome), not steps and not "how far it
can go": the three sections with a definition of done for each (Eric's framing, 2026-09-29).
Carry over from Beginner: act-then-verify, state between runs (handoff-log.md in the folder),
nothing sent as the student without them.

## Class 6 Advanced: OpenClaw in VS Code

**Where:** VS Code with Claude Code. Chosen over the desktop app because an OpenClaw agent
*is* its files (SOUL.md, AGENTS.md, USER.md, TOOLS.md, HEARTBEAT.md, memory/), which VS
Code keeps visible, and because VS Code lets a second AI (Codex or another model) review
Claude's code for bugs: the author shouldn't grade its own work.

**Prerequisite: the Class 1 prereqs, done before class** (`class-1-website-build/prereqs.html`):
VS Code + Claude Code installed and signed in, GitHub (and Vercel) accounts, CLIs logged in,
terminal check, fewer approvals, review agents, CLAUDE.md. The Class 5 deck's homework or
close should point students to it, and the hub card for Class 6 should carry the same
"Do first" link the Classes 1–3 cards use.

**Class 6 prereqs deck** (drafted 2026-09-29; linked and `ant` CLI added 2026-09-30):
`advanced-class-6-openclaw/prereqs.html` + `prereqs-teaching.md`, a copy of the Class 1
prereqs with Vercel and Impeccable removed, "website" → "agent", a "skip to the Terminal
check if you did Class 1" note, the review-agents handout pointed at
`/class-1-website-build/agents.html`, and the Claude Console login from Class 4 mentioned.
To do when Class 6 is built: Eric reviews it, add the hub "Do first" link, deploy the
Worker (its BOT_VIEWS route is already in `infra/worker.js`).

**Disclaimer, up front: use the simplest deployment you can.** OpenClaw is not the
upgrade everyone should take. Choose the lightest option that can do the job:
- **Cowork project** if the job can be run from there. Least to maintain.
- **Managed Agents** for a simple agent with little customization. Anthropic hosts it
  and it's easier to maintain.
- **OpenClaw** only for an agent that needs a lot of customization (its own code and
  custom tools, its own channels, webhooks, **any model you want**), because you now own
  the code, the hosting and the upkeep.

**Any model:** Managed Agents runs Claude only; OpenClaw can swap to whatever model fits
the job (Eric runs Kimi 3). Worth teaching both as flexibility and as a cost lever (a
cheaper model for routine runs), with the cost beat's caveat that each provider bills and
caps spend separately.
The class teaches OpenClaw so they can go there when a job needs it, not as the default.

**Start from the working agent, as files.** First move in Class 6: pull the Class 5 agent
into the project folder so Claude has a working example to rebuild from in OpenClaw instead
of a description; the files go into GitHub with everything else.
- The Console's **Raw** view is only the agent definition (model, system prompt, tools, MCP
  servers). Skills appear as references (a skill ID), not their contents.
- The whole agent is several separate resources: the agent, its skill (SKILL.md + script),
  the environment, the deployment, and the vault. Vault credentials are never exported
  (correctly).
- The docs' route is **Export as code** in the Console ("Manage this agent as code"), whose
  download includes a `claude-lock.json` so `ant apply` updates the same resources.
  Unverified: whether the download includes the skill folder, environment and deployment
  files. Eric to click it and check.
- Fallback that always works: Claude Code uses the `ant` CLI (`brew install
  anthropics/tap/ant`, then `ant auth login` in the browser, no key to paste) to fetch the
  agent (`ant beta:agents retrieve`) and download the skill
  (`ant beta:skills:versions download`). Add `ant` to the Class 6 prereqs draft.

**Scope: config and getting it off the ground, not the full agent.** Homework is finishing
the build.

**As built (2026-09-30).** First half is teaching: what OpenClaw is, the comparison table
(who runs it, models, payment, token overhead, customize, reach, what wakes it, deploy,
maintain, debug, security), the decision tree (Cowork → Managed Agents → OpenClaw, plus the
consumer-agents note: Grok Bot, Meta's Muse), cost, the parts map from Managed Agents, the
workspace files, Gateway and channels, tools/skills/permissions, what wakes it, any model,
security. Build: Install (onboarding run by the student in the VS Code terminal), Step 1
clean it out (measured with `/context detail`), 2 pull in the Class 5 agent via `ant`, 3 model
+ fallback + `.env`, 4 Telegram with pairing (Slack is a plugin needing admin approval, so
homework), 5 a Python script tool on a branch, 6 second-AI review and merge, 7 schedule 7:30
as an automation (pause Class 5 or OpenClaw once both run, or drafts double). Then webhooks
(concept), when it breaks, Render (explained), homework, recap.
Corrections from research against docs.openclaw.ai: TOOLS.md and HEARTBEAT.md are NOT
injected every call (AGENTS, SOUL, IDENTITY, USER, MEMORY, BOOTSTRAP are); the cron command is
now `openclaw automations`; Telegram is built in, Slack is a plugin; Render is documented
(render.yaml; free plan has no disk, so state resets). Unverified: whether onboarding asks for
the workspace path; exact config keys should be checked in the docs during the build-along.
- Same concepts, new home: system prompt → SOUL/AGENTS.md, tools → skills and scripts,
  permissions → allowlists, memory → memory files, deployment → heartbeat/cron.
- **Custom tools become real:** a script the agent calls as a tool, running where they now
  control the code.
- Messaging the agent in the cloud.
- **Webhooks:** outside events that wake the agent.
- Keys go in `.env` via Claude Code, never in a chat.
- Code lives in **GitHub**. **Render** (hosting) picks up the GitHub repo and runs the
  agent in the cloud; explained at the end, not taught hands-on.
- **Branching in GitHub (taught hands-on):** main is the agent that runs; every change
  happens on a branch, gets reviewed (the second-AI review lands here), then merges. Ties
  to the cloud step: a deploy that picks up main only ever gets reviewed code.

## Folders

`advanced-class-4-automations/`, `advanced-class-5-agents/`, `advanced-class-6-openclaw/`.
The hub's single "Coming soon" card becomes three cards.

## Open

1. **Class 4 build, hands-on checks in the Console:** Quickstart output for a briefing
   agent; uploading a custom skill with a script and having a deployment run it; the Drive
   / Dropbox MCP path and vault setup; per-run budget on a deployment.
2. **Class 5:** the agent calling the Class 4 skill on its own; where the three-section
   report persists between sessions. Decided: no memory store. The agent keeps handoff-log.md in the
   briefing folder (standing notes + dated entries), found via a line in the system prompt.
   Observed in Eric's build 2026-09-30. Sessions are the human's record, not the agent's.
3. **Cost screens:** confirm the Console's workspace spend limit and the auto-reload
   toggle exist where the Class 4 cost slide says.

# Advanced Classes 4 to 6: Outline (working draft)

Status as of 2026-09-29. Agreed with Eric in conversation; no decks built yet. The
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

## Class 4 Advanced: Automations

**Where:** Console → Quickstart ("describe what you need") to create the agent. Create
agent is saved for Class 5, where every field gets taught.

**Opener: the map.** Chat, projects, artifacts, Cowork, Claude Code, Managed Agents: what
each is for and when to reach for it. Answers "artifacts vs projects." Why go past Cowork:
schedules to the minute, a hard spend cap per run, any service with an API or remote MCP
server, a real sandbox, and every run kept as an inspectable session.

**Core teach, deterministic vs judgment:** an automation's steps are *dictated* for the
agent to follow; its autonomy is taken away. In Cowork a "fixed step" is still an English
sentence Claude executes. Here the fixed steps can be a **script**: same result every run,
near-free, and Claude does only the judgment step. Push everything that can be code into
code. Claude (in Cowork or chat) writes the script; the student doesn't.

**Build: the morning brief, done the robust way.** Conceptually simple, but the value is in
coding it, plugging in every source they want, and tailoring it.
- The fixed steps are a **skill** (SKILL.md plus a script) the student uploads.
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
- Skills: the Class 4 briefing skill attached here.
- Multiagent: subagents and advisors (introduce; stretch homework).

**The trigger moves.** The same briefing skill from Class 4 is now called by the agent when
it decides it needs it, instead of by the timer. Nothing rebuilt; only who pulls the
trigger changed. That is the automation → agent line in one move.

**Build: Beginner Classes 5 and 6 collapsed into one.** The agent gets the report, acts on
it within the authority it's given, and rewrites the report into three sections: **Taken
care of / Needs your action / FYI.** That is what they read every morning. A full agent.
Carry over from Beginner: authority levels, act-then-verify, a log/state between runs,
nothing sent as the student without them.

## Class 6 Advanced: OpenClaw in VS Code

**Where:** VS Code with Claude Code. Chosen over the desktop app because an OpenClaw agent
*is* its files (SOUL.md, AGENTS.md, USER.md, TOOLS.md, HEARTBEAT.md, memory/), which VS
Code keeps visible, and because VS Code lets a second AI (Codex or another model) review
Claude's code for bugs: the author shouldn't grade its own work.

**Scope: config and getting it off the ground, not the full agent.** Homework is finishing
the build.
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
   report and the log persist between sessions (memory store vs Drive file).
3. **Cost:** separate API account billed by usage ($0.08 per running session-hour plus
   tokens); needs a prerequisite step and a rough monthly estimate for a daily brief.

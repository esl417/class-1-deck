# Teaching notes — Advanced Class 5 (Agents in Managed Agents)

Per-slide notes for the bot view. `##` = slide label. Private. Teach the skill, don't
perform the build. The student finished Advanced Class 4: in the Claude Console
(platform.claude.com) they have a morning-briefing skill, an agent built with Quickstart, an
environment, a credential vault with their app logins, and a scheduled deployment with a
per-run budget that saves a brief to Google Drive or Dropbox. Today they build a separate agent
field by field in Create agent, with its own deployment at 7:30: it finds the brief the Class
4 automation saved, acts on it to produce a deliverable dictated in its system prompt, and writes a handoff: Taken care of / Needs your action / FYI. The Class 4 deployment
keeps running unchanged (separation of duties). Managed Agents is beta and its Console screens change: search the current docs
(platform.claude.com/docs/en/managed-agents) before directing any click. Rules that never
slide: nothing goes out as the student (send and delete tools turned off; it drafts, they
send); tools an unattended run uses are set to always allow (always ask would stall it);
keys only in the vault; cap every run.

## The arc

Where Class 5 sits: Class 4 automated the brief with dictated steps and a timer; Class 5 adds a separate agent that decides its own steps and acts on that brief; Class 6 rebuilds the agent in OpenClaw where they own the code. Nothing from Class 4 is thrown away or changed. The two through-lines: cap spend before anything runs, and use the simplest setup that does the job.

## The finish line

Show the destination: the handoff, not the brief. Three sections: Taken care of (drafts made, tasks filed, each checked), Needs your action (only what needs their judgment, with options prepared), FYI (changes, skipped items). The promise is delegating vigilance: they stop being the person who checks whether something needs doing. Reassure that the Class 4 pieces are reused.

## Two jobs, two parts

Separation of duties, the design idea behind the build. The Class 4 automation keeps running at 7:00 exactly as it is: dictated steps, reads sources, saves the brief, never acts. The Class 5 agent is a separate part with its own deployment at 7:30: a goal instead of steps, it finds that file, decides what each item needs, acts within its limits and writes the handoff. Why keep them apart: each is managed on its own, so they can change what the brief pulls without editing the agent, or tighten the agent's limits without touching the brief; each has its own sessions, cost and cap, so when something breaks they know which part to open. Don't have them pause or merge the Class 4 deployment. The automation-vs-agent test still applies: can you write the steps down before you see what arrives? If yes, automation; if the next step depends on what it finds, agent. Common confusion: "the brief already used judgment, so wasn't it an agent?" No: judgment inside one step you placed is still an automation; choosing the steps is what makes an agent.

## Tools

Keep the terms clean: tools are what the agent uses to act; a skill is not a tool (it's packaged instructions the agent loads, here the Class 4 briefing steps). An automation calls the same things in the same order; an agent picks the tool each item needs. In Managed Agents, tools come three ways: built-in tools (the agent toolset: bash, read, write, edit, glob, grep, web_search, web_fetch; web search costs $10 per 1,000 searches), MCP servers (their apps, now including actions like creating drafts, events and tasks), and API calls (any service with an API, called from the shell or web fetch with a token stored in the vault as a secret; the real key is swapped in as the request leaves, so the agent never sees it; used for apps with no MCP server). The fourth kind arrives in Class 6: their own Python scripts, handed to an OpenClaw agent as tools. Managed Agents can't run a custom tool's code for them, which is the next slide.

## Custom tools

Show the surface's limit on purpose. Add custom tool asks for a name, a description (what it does and when to call it) and an input schema, with no place for code. When the agent calls a custom tool, the session emits the call and pauses (idle, requires action) until the user's own application runs the code and sends back the result. Nothing in the Console runs that code, so in a scheduled run the session would wait indefinitely. (Self-hosted sandboxes can serve custom tools, but that's beyond this class.) Class 6 is where they get a place their own code runs and a script becomes a real tool. Don't have them add a custom tool today.

## Cost control

The Class 5 cost beat. Agents cost more than automations because they choose their own steps: more tool calls, retries, web searches, and possibly subagents (each its own thread, billed against the same session budget, at its own model's rates; advisor consultations too). Controls: a per-run budget on the agent's deployment (set in Step 5, a little above the test run's cost), and leaving Multiagent empty for now. The brief and the agent are separate deployments with separate caps and separate costs in Sessions, which makes it easy to see which part costs what. The Class 4 workspace monthly limit and prepaid credits with auto-reload off still hold. The simplicity reminder: Cowork runs on the Claude subscription with no usage bill, so if a Cowork project can do the job, that's the better home.

## The chain

Generalize the two-part design into a chain: small agents run one after another, each writing a file the next picks up (daisy chained). The brief (Class 4) and the acting agent (Class 5) are the first two links. What Managed Agents gives each link: its own model (and effort), so the brief can run on a cheaper model than the agent that acts, which is a direct cost control; low overhead, since each link loads only its own instructions and tools rather than one big agent carrying everything; traceability, since each link has its own sessions, cost and cap, so a broken link is found and fixed on its own; and extensibility, since a new job is one more link with its own deployment. The third box on the slide (a wrap-up agent reading the week's handoffs) is hypothetical, an illustration only; the class doesn't build it. The generalizable rule: each agent gets one job (one persona). This example is simple enough that the brief and the actions could be combined into one agent, and a student may point that out; the reason to split is greater cost control (a cheaper model and its own cap for the brief) plus the traceability above. Be precise about terms: the first link has dictated steps, so it's an automation (it happens to run as a Managed Agents agent object); today's chain is an automation handing off to an agent, not an agent handing to an agent. Contrast with subagents (Multiagent in the form): those run inside one session under one shared budget; a chain is separate deployments, each managed on its own. Ordering matters: schedule each link after the one it depends on, with slack for the up-to-9-minute start jitter, and have each link say so clearly when its input file is missing.

## The deliverable

The core design idea, framed as Eric wants it: an automation gets its steps dictated; an agent gets its DELIVERABLE (the outcome) dictated and works out the steps. They can't write a step for every email, so they specify exactly what the finished handoff must look like: Taken care of (each item done and checked, e.g. the draft is really in Gmail and the task really on the list, each with a link), Needs your action (only what needs their judgment, each with options already prepared), FYI (what changed and what it skipped, one line each). The sharper the definition of done, the better the agent performs. Limits still apply but are secondary: it drafts and never sends, and it leaves alone the kinds of items they name. Safety: the agent reads untrusted input (email from anyone), and an email can contain instructions aimed at it (prompt injection); a clear deliverable plus send and delete tools turned off keep it on task, and "if unsure, put it under Needs your action" is the default. Push for concrete wording ("a scheduling request is done when a reply proposing two times is drafted"), not vague ("handle important emails").

## Step 1 · General

Managed Agents → Agents → Create agent. The form is the syllabus; walk it top to bottom. General: name, model and effort, description (optional), system prompt. The template covers who they are and what matters (carry over the Class 4 system prompt's rules), the morning routine (find today's brief in their Drive or Dropbox folder and work every item; if there's no brief, say so at the top of the handoff), the deliverable (the three-section handoff with a definition of done for each section, saved to Drive or Dropbox, dated), the limits (draft never send, leave alone the kinds they name, and "if unsure, put it under Needs your action," since nobody is there to ask at 7am), and "read yesterday's handoff first" so it doesn't redo work or drop what's still waiting. Each session starts with fresh context, so the previous handoff in the folder is its memory; no separate log or memory store is needed. The Console's sessions are the student's record of every run (for debugging), not something the agent reads. Model: this link makes the judgment calls, so it gets the stronger model in the chain; a Sonnet model at low effort is plenty, raising effort only if its calls are weak (higher effort costs more per run). Tie back to the chain slide: the Class 4 brief agent only sorts, so they can move it to a lighter model for a direct saving.

## Step 2 · Tools

The built-in toolset is present by default with its permission policy shown (Auto in the form); per-tool permissions are under Tool permissions. Add an MCP server for each app it reads or acts in, including the Drive or Dropbox folder where the brief lands (reuse Class 4's, plus ones for actions like drafts and tasks). Permission policies: always allow, always ask, auto; there's no "never" policy, so turning a tool off (disabling it) is the lock. For an unattended agent: always allow for the built-in tools, the reading tools, and the actions the deliverable needs (create draft, create task, save the handoff); turn off send, anything that deletes, and any action the deliverable doesn't need. Auto can still pause for approval, so don't rely on it unattended. New MCP servers prompt for a credential as in Class 4 (leave the optional fields empty, acknowledge, Connect). Keep "leave alone" in the system prompt, not in permissions: it's about kinds of items, and permissions are per action.

## Step 3 · Skills and multiagent

The last two sections of the form, both left empty on purpose. Skills: the morning-briefing skill stays attached to the Class 4 agent; this agent only needs the file the brief produces. That boundary is the separation of duties: the brief can change without editing this agent. (A skill is packaged instructions, not a tool; they could add one later, e.g. how they write replies, but not today.) Multiagent has two options: subagents (other agents it can delegate to, each its own thread, sharing the session budget) and an advisor (a second model it can consult, billed at that model's rates against the same budget). Introduce both, leave them empty, and note they're a stretch for later. Distinguish them from the chain on slide 8: subagents run inside one session under one shared budget, while each link in a chain is its own deployment with its own model, cap and sessions. Then Create agent.

## Step 4 · Test run

A debugging loop, as in Class 4. Give it "Handle my morning." Today's brief must be in the folder first (if not, Run now on the Class 4 deployment). Four checks: its choices (found today's brief, then chose a different tool per item: the agent deciding its steps); act-then-verify (the draft is really in Gmail, the task really on the list; a tool call saying "created" isn't proof); the deliverable (Needs your action holds only what needs them; fix the deliverable in the system prompt, not the handoff); cost (compare to a Class 4 run, times 22 weekdays). Tools still on always ask will pause the test for approval; that's fine while they watch, but set them in Step 2 before scheduling.

## Step 5 · Schedule it

Leave the Class 4 deployment running as it is; this is a second deployment. Fields: the new agent, Class 4's environment and vault, `30 7 * * 1-5` in their time zone (after the 7:00 brief; scheduled runs can start up to 9 minutes late, so if the brief sometimes lands late, move the agent later, not earlier), the prompt "Handle my morning." (a goal, not steps), and a per-run budget a little above the test run's cost. At the cap a run pauses rather than being killed. Then Run now once and read the session: it's the first run with nobody to approve anything, so it proves the permissions hold. If it stalls, look for a tool call waiting on approval. Confirm the current form fields in the Console.

## Direct it

Besides the schedule, they can start a session with the agent any time and hand it a job, phrased as an outcome, the same way the handoff is dictated ("Prep me for the 2pm: one page, open questions first"). Same system prompt and limits. Have them notice it chooses where to look. It can't know what happened in a meeting, so the request has to carry decisions ("we agreed on the 15th and a revised quote"). Describe-don't-micro-direct applies: tell it the outcome, not the clicks.

## Tune what reaches you

The first week is calibration, and the fix is always the deliverable in the system prompt, not the handoff itself. Too much reaching them: things they'd handle the same way every time; say that kind of item belongs in Taken care of and what done looks like. Too little: it handled something they wanted to see; say that kind of item belongs in Needs your action, and why. When something surprises them, open that run's session and read why before changing anything, then fix the cause: the deliverable or a tool permission.

## Homework

Two things before Class 6. A week of starting every morning with the handoff and sharpening the deliverable; the arrival test is that they send its drafts with barely a change. And the Class 6 prerequisites (VS Code, Claude Code, GitHub installed and logged in; about an hour; the Class 6 prereqs page at /advanced-class-6-openclaw/prereqs.html), because Class 6 starts building immediately. Help fully with mechanics; what counts as done, and what always comes to them, is their call.

## You shipped it

Recap: a two-link chain (the Class 4 brief feeding the agent, each with its own model and cap), an agent built in Create agent with its deliverable dictated in the system prompt, the Class 4 brief still running as its own automation and feeding the agent, tools allowed or turned off (it drafts, they send), yesterday's handoff as its memory, and a capped weekday run. Bridge to Class 6: they own the code, rebuilding this agent in OpenClaw where custom tools run and any model can power it. Say the simplicity rule plainly: if this agent already does the job, staying in Managed Agents is the right call; Class 6 is for when an agent needs more.

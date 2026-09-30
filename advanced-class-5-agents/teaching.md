# Teaching notes — Advanced Class 5 (Agents in Managed Agents)

Per-slide notes for the bot view. `##` = slide label. Private. Teach the skill, don't
perform the build. The student finished Advanced Class 4: in the Claude Console
(platform.claude.com) they have a morning-briefing skill, an agent built with Quickstart, an
environment, a credential vault with their app logins, and a scheduled deployment with a
per-run budget that saves a brief to Google Drive or Dropbox. Today they build a new agent
field by field in Create agent, attach the same skill, give it authority in four lists, a
memory store for its log, and a deployment whose prompt is a goal ("Handle my morning")
instead of steps. It rewrites the brief into Taken care of / Needs your action / FYI.
Managed Agents is beta and its Console screens change: search the current docs
(platform.claude.com/docs/en/managed-agents) before directing any click. Rules that never
slide: nothing goes out as the student (send and delete tools turned off; it drafts, they
send); tools an unattended run uses are set to always allow (always ask would stall it);
keys only in the vault; cap every run.

## The arc

Where Class 5 sits: Class 4 automated the brief with dictated steps and a timer; Class 5 hands the trigger to an agent that decides its own steps and acts; Class 6 rebuilds it in OpenClaw where they own the code. Nothing from Class 4 is thrown away. The two through-lines: cap spend before anything runs, and use the simplest setup that does the job.

## The finish line

Show the destination: the handoff, not the brief. Three sections: Taken care of (drafts made, tasks filed, each checked), Needs your action (only what needs their judgment, with options prepared), FYI (changes, skipped items). The promise is delegating vigilance: they stop being the person who checks whether something needs doing. Reassure that the Class 4 pieces are reused.

## The trigger moves

The automation-to-agent line in one move. Class 4: a timer starts the run and the skill's steps are dictated (autonomy removed on purpose). Class 5: a timer still wakes it, but the deployment's prompt is a goal, and the agent decides to run the skill, what to look up next, and what to do per item. The test to have them say out loud: can you write the steps down before you see what arrives? If yes, keep it an automation (cheaper, more predictable); if the next step depends on what it finds, it's an agent's job. Common confusion: "the brief already used judgment, so wasn't it an agent?" No: judgment inside one step you placed is still an automation; choosing the steps is what makes an agent.

## Tools

Keep the terms clean: tools are what the agent uses to act; a skill is not a tool (it's packaged instructions the agent loads, here the Class 4 briefing steps). An automation calls the same things in the same order; an agent picks the tool each item needs. In Managed Agents, tools come three ways: built-in tools (the agent toolset: bash, read, write, edit, glob, grep, web_search, web_fetch; web search costs $10 per 1,000 searches), MCP servers (their apps, now including actions like creating drafts, events and tasks), and API calls (any service with an API, called from the shell or web fetch with a token stored in the vault as a secret; the real key is swapped in as the request leaves, so the agent never sees it; used for apps with no MCP server). The fourth kind arrives in Class 6: their own Python scripts, handed to an OpenClaw agent as tools. Managed Agents can't run a custom tool's code for them, which is the next slide.

## Custom tools

Show the surface's limit on purpose. Add custom tool asks for a name, a description (what it does and when to call it) and an input schema, with no place for code. When the agent calls a custom tool, the session emits the call and pauses (idle, requires action) until the user's own application runs the code and sends back the result. Nothing in the Console runs that code, so in a scheduled run the session would wait indefinitely. (Self-hosted sandboxes can serve custom tools, but that's beyond this class.) Class 6 is where they get a place their own code runs and a script becomes a real tool. Don't have them add a custom tool today.

## Cost control

The Class 5 cost beat. Agents cost more than automations because they choose their own steps: more tool calls, retries, web searches, and possibly subagents (each its own thread, billed against the same session budget, at its own model's rates; advisor consultations too). Controls: a per-run budget on the deployment (set in Step 6, a little above the test run's cost), pausing the Class 4 deployment so they don't pay for two runs every morning, and leaving Multiagent empty for now. The Class 4 workspace monthly limit and prepaid credits with auto-reload off still hold. The simplicity reminder: Cowork runs on the Claude subscription with no usage bill, so if a Cowork project can do the job, that's the better home.

## Authority

The core design idea. They can't write a step for every email, so they give it authority: for each kind of item, handle it (do it, report after), prepare it (get it ready, they finish, e.g. a Gmail draft they read and send), bring it to me (only they can decide), leave it alone. Push for concrete kinds of items ("scheduling requests," "invoices over $1,000," "anything from Acme"), not vague ones ("important emails"). Start conservative and widen as trust grows. The safety point to land: the agent reads untrusted input (email from anyone), and an email can contain instructions aimed at it (prompt injection). What protects them is structural: the four lists, send and delete tools turned off, and "if unsure, bring it to me." Nothing goes out as them.

## Step 1 · General

Managed Agents → Agents → Create agent. The form is the syllabus; walk it top to bottom. General: name, model and effort, description (optional), system prompt. The template covers who they are and what matters (carry over the Class 4 system prompt's rules), the morning routine (run the skill, then work each item by the lists), the four lists with their own examples in the brackets, the rule "if unsure, bring it to me" (nobody is there to ask at 7am), act-then-verify, the handoff log (read first, update last), and the three-section handoff saved to Drive or Dropbox. Model: a Sonnet model at low effort is a sensible start; raise effort only if its calls are weak, since higher effort costs more per run.

## Step 2 · Tools

The built-in toolset is present by default with its permission policy shown (Auto in the form); per-tool permissions are under Tool permissions. Add an MCP server for each app it reads or acts in (reuse Class 4's, plus ones for actions like drafts and tasks). Permission policies: always allow, always ask, auto; there's no "never" policy, so turning a tool off (disabling it) is the lock. For an unattended agent: always allow for the built-in tools, the reading tools, and the actions the lists need (create draft, create task, save the handoff); turn off send, anything that deletes, and any action the lists don't need. Auto can still pause for approval, so don't rely on it unattended. New MCP servers prompt for a credential as in Class 4 (leave the optional fields empty, acknowledge, Connect). Keep "leave it alone" in the lists, not in permissions: it's about kinds of items, and permissions are per action.

## Step 3 · Skills

Add skill → morning-briefing. This is where the trigger moves: the skill (the Class 4 briefing steps) is unchanged, and the agent now decides when to run it. Keep calling it a skill, not a tool. Multiagent has two options: subagents (other agents it can delegate to, each its own thread, sharing the session budget) and an advisor (a second model it can consult, billed at that model's rates against the same budget). Introduce both, leave them empty today, and note they're a stretch for later. Then Create agent.

## Step 4 · Memory

Each session starts with fresh context, so without a record it would redo work and lose track of what's waiting. A memory store is a workspace-scoped set of text documents mounted into the session's sandbox; the agent reads and writes it with its file tools (the agent toolset must be enabled), and a note about the mount is added to its system prompt automatically. Create one under Managed Agents → Memory stores (name it handoff-log). Memory stores are attached when a session is created, so they attach it on the deployment in Step 6 (and in the test run's session if the form allows). Contents: what it handled, what it prepared, what's waiting, what changed. They can read and edit entries in the Console; if an entry is wrong, fix it. Stores attach read-write by default; because this agent reads untrusted email, a prompt injection could write into the log, which is one more reason for the weekly skim.

## Step 5 · Test run

A debugging loop, as in Class 4. Give it "Handle my morning." Four checks: its choices (ran the skill, then chose a different tool per item: the agent deciding its steps); act-then-verify (the draft is really in Gmail, the task really on the list; a tool call saying "created" isn't proof); the lists (Needs your action holds only what needs them; fix the lists in the system prompt, not the handoff); cost (compare to a Class 4 run, times 22 weekdays). Tools still on always ask will pause the test for approval; that's fine while they watch, but set them in Step 2 before scheduling.

## Step 6 · Schedule it

Pause the Class 4 deployment first (it's now redundant and costs money). New deployment: the new agent, Class 4's environment and vault, the handoff-log memory store, `0 7 * * 1-5` in their time zone, the prompt "Handle my morning." (a goal, not steps), and a per-run budget a little above the test run's cost. At the cap a run pauses rather than being killed. Then Run now once and read the session: it's the first run with nobody to approve anything, so it proves the permissions hold. If it stalls, look for a tool call waiting on approval. Confirm the current form fields in the Console.

## Direct it

Besides the schedule, they can start a session with the agent any time and hand it a job ("prep me for the 2pm," "draft the reply to Dana"). Same system prompt, lists and limits. Have them notice it chooses where to look. It can't know what happened in a meeting, so the request has to carry decisions ("we agreed on the 15th and a revised quote"). Describe-don't-micro-direct applies: tell it the outcome, not the clicks.

## Tune what reaches you

The first week is calibration. Too much reaching them: move that kind of item to handle or prepare. Too little: it handled something they wanted to see, so move it to bring to me and say why. When something surprises them, open that run's session and read why before changing anything, then fix the cause: a list in the system prompt, a tool permission, or a wrong log entry. Fix the lists, not the handoff, so it sticks for every morning after.

## Homework

Two things before Class 6. A week of starting every morning with the handoff and tuning the four lists; the arrival test is that they send its drafts with barely a change. And the Class 6 prerequisites (VS Code, Claude Code, GitHub installed and logged in; about an hour; the Class 6 prereqs page at /advanced-class-6-openclaw/prereqs.html), because Class 6 starts building immediately. Help fully with mechanics; what it may handle alone is their call.

## You shipped it

Recap: an agent built in Create agent with directions and four lists, the Class 4 skill, run when the agent decides, tools allowed or turned off (it drafts, they send), a memory store log, and a capped weekday run. Bridge to Class 6: they own the code, rebuilding this agent in OpenClaw where custom tools run and any model can power it. Say the simplicity rule plainly: if this agent already does the job, staying in Managed Agents is the right call; Class 6 is for when an agent needs more.

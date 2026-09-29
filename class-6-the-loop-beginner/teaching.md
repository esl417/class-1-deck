# Teaching notes — Class 6 (The Loop)

Per-slide notes for the bot view. `##` = slide label. Private. Teach the skill, don't
perform the build. The student arrives with a Cowork project containing: a scheduled task
that writes the morning brief (Class 4), directions in the project instructions and
connector settings that let the agent draft in Gmail and file tasks (Class 5, with Gmail
"send email" set to never), and a week of directing the agent plus a list of what they ask
it to do most. Today the agent stops waiting to be asked: a second scheduled task reads the
brief first, acts within the authority the student writes down, keeps a log, and writes a
morning handoff. The promise is delegating vigilance: the student stops being the one who
checks. The rules that never slide: the agent never sends (send email stays never; the
send button is the student's), anything that deletes stays never, and connector settings
(what an app connection may do) are not the same thing as the approval setting under the
message box (Claude asking before it acts). A 2-hour class: the morning loop must ship;
the daytime check is optional.

## The finish line

Show the destination: a handoff instead of a brief. The brief says "Sarah needs the revised timeline"; the handoff says the reply is already drafted in Gmail, and names the two things only the student can decide. The point to land is not the draft, it's that the student didn't have to notice. Reassure that nothing is rebuilt: same project, same brief, same agent.

## The shift

The three-class arc as one picture. Class 4: a schedule starts it, the student wrote the steps, it reports. Class 5: the student starts it, it decides the steps, it acts. Class 6: a schedule starts it and it decides the steps, so it reads first and hands over the rest. The phrase to leave with them is "delegating vigilance": the value isn't drafting while they sleep, it's no longer being the person who checks whether something needs drafting. If a student asks how this differs from Class 4 (both run on a schedule): who decides the steps. The brief follows fixed steps; the loop decides what each item needs.

## The loop

Demystify "proactive." An agent that seems to keep watch is running the same loop repeatedly: look, decide, act, write it down, look again. Class 4 built look (the brief), Class 5 built decide and act with the student starting it, and today closes the loop so it starts the next round itself. The second idea: a schedule starts the loop but doesn't dictate the work. "7:30 every morning" says when to look; what it does depends on what it finds. That is the difference from the brief, whose steps are fixed.

## Authority, not a script

The core design idea. They can't list every case, so instead of steps they give it authority: for each kind of thing, how far it may go alone. Handle it (do it and report after), prepare it (get it ready and the student finishes it, e.g. a Gmail draft they read and send), bring it to me (only the student can decide), leave it alone. Use "bring it to me," not "needs approval," so it isn't confused with connector settings. The goal line: not "never involve me" but "only involve me where my judgment is actually needed."

## Step 1 · Its authority

They add a "When the handoff task runs" section under the directions they wrote in Class 5, with four lists (handle, prepare, bring to me, leave alone), their own examples in the brackets, and a closing rule: if unsure, don't act, bring it to me in the handoff (there's no one to ask at 7:30). Scoping it to the handoff task by name matters: every task in the project reads the instructions, and the 7:00 brief must stay read-only and fixed. Tie it to last week's homework list (what they asked it to do most): the jobs on it that it gets right go under handle or prepare; anything they still correct stays under bring to me. Prep notes go into the handoff itself, since Drive stays read-only. Starting conservative is correct; they widen it as trust grows. Push for concrete kinds of things ("scheduling requests," "invoices over $1,000," "anything from Acme"), not vague ones ("important emails").

## Step 2 · No one watching

When the loop runs at 7:30, nobody is there to answer "ask you first," so for every action the handoff task uses (reading, creating Gmail drafts, filing tasks) they choose allow in + → Connectors → Manage connectors, and never for actions they never want, like deleting. Don't let them try to enforce "leave alone" here: it's about kinds of messages, and connector settings are per action, so setting Gmail reading to never would break both the brief and the handoff. "Leave alone" lives in the instructions. Send email stays never; that's what makes "prepare" safe, because it can leave a draft but cannot send it. "Ask you first" still works when they direct it themselves; it just isn't a setting to rely on for unattended work. Keep connector settings (what the app connection may do) separate from the approval setting under the message box (Claude asking before it acts).

## Step 3 · Its log

Each run starts fresh, so without a record it would draft the same reply twice or lose track of what's waiting on the student. The fix is a running "Handoff log" in the project: what it handled, what it prepared, what's waiting on the student, what changed since the last run, read at the start of every handoff run and updated at the end (scoped to the handoff task, so the brief doesn't touch it). This is also how it notices change, which the daytime check depends on. The log is the student's to read; if something in it is wrong, they tell the agent to fix it. If a run can't find or update the log, that's the first thing to troubleshoot: ask it where it saved the log and have it confirm it read the latest version.

## Step 4 · The handoff task

The brief stays exactly as it is: it's still the automation, and keeping it fixed is the Class 4 lesson. They add a second scheduled task at 7:30, after the brief, by pasting the prompt with Cowork selected. The prompt carries three of the class's ideas: follow the authority lists, act then verify (check the draft is really in Gmail, the task really on the list, and say so if not), and write the handoff in five parts (found, handled, prepared, changed, needs your decision), saved in the project and dated like the brief, updating the log last. Leave "Require this computer" off. If the brief sometimes finishes late, move the handoff later rather than earlier.

## Step 5 · Prove it

Run it once now, and check it like a new assistant's first morning: does "needs my decision" contain only things that really need them; is everything it says it did actually in Gmail and the task list; does the log match. Name the principle: act, then verify. "I created the draft" isn't a draft existing, which is why the task checks its own work and why the student checks too until they trust it. If something's off, describe what they saw to Claude and fix the cause (usually the authority lists or the task prompt), then run it again.

## Tune what reaches you

The first week is calibration, and the handoff will be off one way or the other. Too much reaching them: things they'd have handled the same way every time, so move that kind of thing to handle or prepare. Too little: it handled something they wanted to see, so move it to bring to me and say why. The fix always goes in the instructions (the four lists), not in editing the handoff, so it sticks for every morning after.

## During the day

Optional, once the morning loop has earned trust. "Proactive" is just the loop running again: a check every hour or two looks at what changed since the last run (using the log), acts if something did, and updates the handoff. Be honest about the mechanism: it can't be notified the instant something changes; it finds out the next time it looks, so hourly means within the hour. Usage: daytime checks use their plan. They should watch Settings → Usage for a few days; if they hit limits on Pro, check every few hours instead of hourly, or move to Max, where they're unlikely to hit them.

## Read the handoff

The new morning habit: read the handoff, not the inbox. They review what changed, what it did, and what's still theirs. Two habits keep it trustworthy: silence never means fine (it writes a handoff every weekday, even a quiet one, so no handoff on a weekday means something broke and they check the task's last run), and a weekly skim of the log to catch a habit they don't like before it becomes a problem.

## Where this goes next

A tour, not homework, and it should stay a tour: nobody builds this in class. The slide follows the Managed Agents section of the Claude Console menu (platform.claude.com), so students can match it to what they'll see: Quickstart, Agents, Sessions, Deployments, Environments, Credential vaults, Memory stores. Explain each through what they already built. Agents: the agent's definition (model, system prompt, tools and MCP servers, skills, and a permission policy per tool: always_allow, always_ask, or auto, where the server decides per call) — in the app, their directions, connectors and connector settings. There is no "never" policy: to stop a tool entirely you disable it on the agent, which is the equivalent of the app's never. Sessions: each run, with its full history kept; you can watch it, read it and send it a message mid-run — in the app, a conversation or one scheduled run. Deployments: scheduled runs on a cron schedule, down to the minute, with an optional dollar budget per run — in the app, scheduled tasks. Environments: the cloud sandbox configuration, meaning installed packages and network access — the app handles this for them, which is part of why the app is simpler. Credential vaults: stored credentials for MCP servers (OAuth or tokens) and environment-variable secrets that are swapped in at the moment of a request, so the agent uses a key without seeing it — in the app, signing in to connectors. Memory stores: persistent memory mounted into sessions — in the app, memory plus the Handoff log. Quickstart: the Console's guided builder with a built-in test session, the right place to start. Be honest about moving up: it's in beta, it needs its own API key billed by usage (separate from their Claude plan), and session runtime costs $0.08 per session-hour, counted only while the session is running (not while it's idle or waiting). Most students never need it; the point is knowing the ceiling exists and what each part is called.

## What it opens up

What Managed Agents adds, each in plain words. Webhooks: define the term first (a web address another service calls the moment something happens, like a form submission or a payment). Be precise about the mechanics if asked: Managed Agents doesn't hand you such an address directly; something has to make the API call that starts a session when the event happens, typically a tool like Zapier's or Make's webhook step, or a little code. (Managed Agents' own "webhooks" feature is the other direction: it notifies you when a session starts, idles, hits its budget or ends.) Any app with an API: any service with an API or a remote MCP server, not just the connector directory; credentials live in a vault and are substituted at the moment of the request, so the agent can use a key without ever seeing it. Its own computer: each session gets a cloud sandbox with a shell, packages and files. A team of agents: a coordinator can hand threads of work to other agents. A definition of done: a rubric it iterates against until the result passes. Exact schedules and hard caps: cron schedules to the minute, and hard dollar budgets per session or per scheduled run. The closing move matters most: they don't need a class for this, because Claude can walk them through it. Have them ask Claude to guide the rebuild of their handoff as a Managed Agent, pasting in their directions; Claude should check the current docs before directing them through the Console, since it's a beta product whose UI changes.

## Homework

A week of starting every morning with the handoff and tuning the four lists, turning on a daytime check once mornings feel right. Then the next chore: map one more job they do by hand and ask the Class 5 question (can you write the steps before you see what arrives?) to decide whether it's an automation, something they direct, or something it watches for them. Help fully with the mechanics; the choice of chore and where it sits are theirs.

## You shipped it

Close the course, not just the class. What now runs: the brief (automation), the agent they direct, the loop that reads first and hands over the rest, and limits set on purpose, with nothing sent until they send it. The arc to leave them with: it tells you, you tell it, it does it, and it works for any chore where they can say what "handled" means. If a student asks what they actually learned: telling an automation from an agent, writing down their judgment, giving software authority with limits, and checking its work until they trust it.

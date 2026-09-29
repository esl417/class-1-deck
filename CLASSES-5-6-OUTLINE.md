# Classes 5 and 6: Outline (working draft)

Status as of 2026-09-28. Class 5 is close to settled. Class 6 is proposed, not agreed.
CLASSES-OUTLINE.md and the agent course copy still describe the older design; this file
is the current reference until they are updated.

## The arc (Classes 4 to 6)

**It tells you → you tell it → it does it.** Each class takes one more thing off the
owner's hands.

| | Class 4 | Class 5 | Class 6 |
|---|---|---|---|
| Core idea | Automate a process | Delegate a task | Delegate vigilance |
| Who starts it | A schedule | You | A schedule |
| Who decides what to do | You, in advance (fixed steps) | The agent | The agent |
| Who reviews the situation first | You | You | The agent |
| Your role | Read the brief | Give direction | Handle exceptions |
| The morning artifact | Brief: "here's what needs you" | Brief + chat: "tell me what to handle" | Handoff: "here's what I handled, and the two things only you can decide" |

## Platform (decided)

- Everything lives in **one Cowork project** in the Claude app, **in the cloud from day
  one**. There is no local-to-cloud move.
- Accounts are reached through **connectors** (Gmail, Calendar, Drive, a task manager).
  No code, no API keys, no terminal.
- **Project instructions** hold what matters to the owner; only the owner edits them.
  **Memory** is what the agent records from corrections.
- **Connector permissions** (per action: allow / ask / never) are the safety
  layer: limits are settings, not promises.
- "Require this computer" is only for sources that live on the owner's computer.
- Phone access is the Claude app. There are no event triggers in Cowork, so "during the
  day" means an hourly scheduled check.
- Rejected: Claude Code Projects (not rolled out), the Agent SDK and OpenClaw (too
  technical), a Python script in a cloud routine (account-access friction), and routines
  triggered from outside via Zapier or Apps Script (a second product to maintain).

## Class 5: The agent (you tell it)

**You build:** the Class 4 project becomes something you talk to. It reads the morning's
brief, and you direct it: "prep me for the 2pm," "handle #2," "reschedule Thursday." It
acts on your behalf when you tell it to: drafting replies, filing tasks, writing prep
notes.

**Teachings:**
- **Automation vs. agent:** an automation follows steps you wrote in advance; an agent
  decides its own steps toward a goal you set. The test: can you write the steps down
  before you see what arrives?
- **The brief is the agent's to-do list.** Every item links to its source, which is what
  makes "handle #2" work.
- **The connectors are its tools.** It picks a different one for each item: calendar for
  a reschedule, email for a reply, tasks for a follow-up.
- **Memory:** it records what it learns from your corrections. Instructions are yours;
  memories are its own.
- **Draft, don't send.** It acts only when you tell it to, and nothing leaves without
  you. Decided 2026-09-28: connector settings are per action (+ → Connectors → Manage
  connectors → the connector: allow / ask / never). Gmail **send email is set to never**
  and drafting is allowed, so the control is the send button (the owner reads each draft
  and sends it). Deletes are never; everything else is the owner's call. Connector
  settings are what an app connection may do; the approval setting under the message box
  is Claude asking before it acts, a separate thing.
- **From your phone:** direct it from the Claude app.

## Class 6: The loop (it does it) — proposed

**Promise: delegate vigilance.** The valuable thing is not that Claude can draft an email
while you sleep. It's that you stop being the person who keeps checking whether an email
needs drafting.

**You build:** the agent reads the brief before you do, handles what it's authorized to,
prepares what needs your input, and rewrites the brief into a **morning handoff**:
- what it found
- what it already handled
- what it prepared for you
- what changed
- what needs your decision

During the day an hourly check wakes it up. It compares against what it saw last time,
acts if something changed, and updates the handoff. For example: *"The 2pm moved to 3pm.
I updated your prep note and flagged the conflict it creates at 3:30."*

**Teachings:**
- **The agent loop:** observe → decide → act → record → observe again. Class 4 built
  *observe*. Class 5 taught *decide + act* with you starting it. Class 6 closes the loop.
- **A trigger starts the loop; it doesn't dictate the work.** "Every morning" or "every
  hour" says when to look. What it does depends on what it finds.
- **Give it authority, not a script.** For each kind of item, decide whether it may
  handle it, prepare it, bring it to you, or must leave it alone.
- **The agent needs state:** what it already handled, what is still waiting, what
  changed since the last run. Otherwise it rediscovers the world every time.
- **Act, then verify.** Check that the result really happened; a tool call is not the
  same as success.
- **Escalate exceptions.** The goal isn't "never involve me." It's "only involve me where
  my judgment is actually needed."
- **The brief becomes a handoff, not an inbox.** You review what changed, what it did,
  and what remains yours.
- **Proactivity is the loop running again.** It is not magic: you give it triggers that
  cause it to wake, reassess and act.
- **Usage callout:** checks during the day draw on your plan. Watch Settings → Usage for
  a few days. If you hit limits on Pro, check every few hours instead of hourly, or move
  to Max, where you're unlikely to hit them.

**Scope for a 2-hour class:**
- **Must ship:** the morning loop, meaning one run a day that produces the handoff.
- **Demo and homework:** the hourly check during the day.

**Approval design:** "prepare" means creating a Gmail draft, and the owner approves by
sending it. This holds: send email can be set to never on its own while drafting stays
allowed, so an unattended run can draft but cannot send. Nothing depends on an approval
prompt reaching a task that runs with nobody watching. (An earlier note here said draft
and send were one paired permission; that was wrong.)

**The alternative still on the table:** Class 6 expands to more of the business (a
second job or a second agent) instead. The current view is to use it as closing
homework ("the next chore"), not as the whole class.

## Open: needs a hands-on test

Ordered by what breaks the most:

1. **State:** can a scheduled run leave a file that the next run reads and updates?
   Class 6 depends on it.
2. **Pro accounts:** do cloud Cowork projects and scheduled tasks work there?
   Everything seen so far is on Max.
3. **Gmail:** answered. Settings are per action; send email can be set to never while
   drafting is allowed.
4. **Brief → agent:** can a conversation in the project read what the scheduled task
   produced?
5. **Steadiness:** does the same inbox give the same brief across three runs?
6. **Blocked stays blocked:** do permission settings hold in scheduled runs nobody is
   watching?
7. **Unattended approvals:** what does a scheduled task do with a "Needs approval"
   action? This only matters if the draft-as-approval design isn't enough.
8. **Drive:** can the Drive connector edit an existing doc (for "updated your prep
   note"), or only create new ones?

## What changes elsewhere

- Class 4 deck: rewritten for Cowork (2026-09-28). Its UI steps still need confirming on
  screen: the path to connector permissions, where the brief is saved, and how to run a
  task once.
- `class-4-automations/DESIGN-INTENT.md`: still describes the Python design.
- CLASSES-OUTLINE.md and COURSE-INTRO-OUTLINE.md: still list Class 6 as go-to-market.
- Agents lightning lesson: its "What's next" slide and its $25/month and always-on-home
  lines.
- Strategy lightning lesson: "Class 6 is go-to-market, built on StratEngine."
- Maven course page and ericgrows.com/live: "moves it off your laptop," "$25/month,"
  and "own key, billed by usage." The copy follows the design, not the other way round.
- The shared preamble in llm-preamble.md says "Claude Code," which no longer fits
  Classes 4 to 6.

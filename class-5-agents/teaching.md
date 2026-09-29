# Teaching notes — Class 5 (Agents)

Per-slide notes for the bot view. `##` = slide label. Private. Teach the skill, don't
perform the build. The student built a morning briefing last class: a scheduled task in a
Cowork project that reads their accounts through connectors and writes a brief whose items
link to their sources. Today the same project gets an agent they hand work to. The rules
you must never let slide: the agent never SENDS anything (in the Gmail connector's settings, send email is set to
never and creating drafts is allowed; the control is that the student reads each draft and
presses send themselves), and anything that deletes is set to never. Don't mix up the two
kinds of permission: the connector settings (+ → Connectors → Manage connectors) decide what
an app connection can do; the approval setting under the message box is about Claude
asking before it acts. The ideas to land: an automation follows
steps written in advance; an agent decides its own steps toward a goal. Instructions are
the student's; memory is the agent's.

## The finish line

Show the destination before explaining anything: the student points at an item in their brief and the work gets done, with a draft waiting in Gmail for them to read and send. The contrast that sells it is time: twenty minutes of opening the thread, checking the calendar, finding the task and writing, versus one sentence. Reassure early that it is the same project and the same accounts as last class; nothing new to install. If a student didn't finish last class's brief, get that running first (even a single run is enough), because the agent works from it.

## The line

The spine of the class. Automation: the student decides the steps in advance and they are the same every run (the brief). Agent: it gets a goal and works out the steps once it sees what's in front of it. The test to make them say out loud: can you write the steps down before you see what arrives? If yes, keep it an automation, because it is cheaper and more predictable. If the next step depends on what it finds, it is a job for an agent. Common confusion: "but the brief uses Claude too, so isn't it an agent?" No. Using judgment inside one step the student placed is still an automation. What makes it an agent is that it chooses the steps.

## Three messages

Make the test concrete. Three items from one morning each need a different thing looked up: a reschedule needs the calendar, a proposal follow-up needs the task list (and ends in flagging it to the owner, because only they can fix an overdue proposal), a "did you see my notes" needs the shared doc. No single recipe covers "handle whatever came in." If a student asks why not just write three recipes: because tomorrow brings a fourth kind of message, and the fifth. You can describe what good looks like; you cannot list every case.

## What an agent is

Demystify: an agent is instructions + tools + limits + memory, and they have three of the four from last class (instructions, connectors, and their permissions). Today they swap the instructions out in Step 1: who it is, how it uses the brief, and what it may do. Tools are the connectors; the agent picks which one each job needs. Limits are the connector permissions; today they loosen one or two on purpose. Memory is new: what it learns from corrections, kept between conversations. The distinction to plant now because it matters all class: the instructions are theirs (only they edit them); the memory is its own (it writes it, they can read and delete it).

## The to-do list

The brief becomes the agent's to-do list, and the links on each item are what make "handle #2" work: the agent follows the link to the real thread instead of the student describing the situation. If a student's brief items don't link to their sources, fix that first: have Claude add a link to every item in the scheduled task and run it once. Also reinforce who is driving today: nothing happens until the student points at an item.

## Step 1 · Its directions

After Class 4 the project's instructions only say what matters for the brief. Step 1 swaps them out for the agent's directions: the student opens the Morning Briefing project's instructions, replaces what's there with the template, and fills in the brackets. The brief's scheduled task still reads these instructions to decide what matters, so if they had rules they still want the brief to follow ("anything from a client is urgent"), have them carry those over into the "How I work" part. Most of the template is the same for everyone and should stay: how it uses the brief (read the newest one first, "#2" means item 2 of today's brief, follow each item's link before acting) and what it may do (draft replies for approval, file tasks, prep notes in the conversation; never send, never delete, ask when unsure). The bracketed parts are theirs: what the business is, how they sound, who gets priority, what always comes to them. Push for specifics, the way they would brief a new hire; vague answers produce a generic assistant. The slide says to edit freely, and mean it: add rules, cut ones that don't apply, change what it's allowed to do, as long as "never send" and "never delete" stay unless they understand what removing them means. Only the student edits the instructions. Then the check: with Cowork selected, ask which brief item to deal with first and why. A good answer names a real item and a reason they'd agree with; if it can't find the brief, have it look for where the scheduled task saves briefs and read the newest one.

## Step 2 · Loosen its limits

Last class everything that writes was set to never. The directions from Step 1 say what it may do; the connector settings make sure it can't do more. Where they live: in the message box, click + → Connectors → Manage connectors, then click a connector. Every action the connector offers has its own setting: allow it, ask first, or never. The one fixed rule: in Gmail, send email is set to never. Creating drafts is allowed, so it can write replies. Anything that deletes stays never. Everything else is the student's call, connector by connector: allow what they're comfortable with, ask for anything they want to see first, never for anything they don't want it doing. The control to name: the send button. The agent can write a draft but cannot send it; the draft waits in Gmail until the student reads it and presses send. These connector settings decide what an app connection may do; keep them separate from the approval setting under the message box, which is about Claude asking before it acts.

## Step 3 · Hand it work

The moment the class is for. Three directions from their own brief, one at a time: prep for a meeting (it reads the invite, the thread and open tasks, and writes a prep note in the conversation; Drive stays read-only, so it should not try to save a file there), draft a reply (it looks up what the reply needs, then leaves a draft in their Gmail for them to read and send), turn an item into a task (it files it on their list). Have them narrate what it chose to look at: that is the agent deciding its own steps, the thing that makes it an agent. Then make them open Gmail and their task app and see the draft and the task sitting there. If it does something they didn't expect, don't fix the output yet; that's the "When it gets it wrong" slide.

## Step 4 · Teach it once

It will get small things wrong. The skill: tell it, and ask it to remember, instead of silently fixing the draft. Show the persistence: a new conversation tomorrow still knows. Then the sorting rule they will use all week: a rule for everyone ("money questions come to me") goes in the instructions, which they edit; a fact it learned ("Dana prefers calls") goes in memory, which it keeps. Encourage them to look through its memory now and then and delete anything wrong or stale; memory they never review can drift.

## From your phone

The project lives in their Claude account, not on the laptop, so the same agent is in the Claude app on their phone: same project, Cowork selected, same instructions, memory and limits. Have them try it live ("handle #3 from this morning's brief") and then check the draft in Gmail on their phone. The payoff to paint: walking out of a meeting and asking for the follow-up draft, which is waiting by the time they sit down. The agent can't hear the meeting, so the request has to carry what was agreed ("we agreed on the 15th and a revised quote"); point that out. If the app's layout differs from the desktop, help them find the project first, then the Cowork toggle.

## When it gets it wrong

A mistake is information. Fixing the draft fixes today; fixing the cause fixes every day after. First ask it "why did you do that?", then fix the right layer: a missing rule goes in the instructions, a wrong fact gets corrected in memory, and an action it shouldn't have been able to take means tightening that permission. Reinforce describe-don't-micro-direct: "that reply was too formal for a client I've known for years" teaches it more than rewriting the email themselves.

## What it still waits for

Name the honest limit of today's build so Class 6 lands: it only works when they open the app and hand it something. They still read the brief first and still decide what to hand over; nothing happens while they're busy. Next class it reads the brief before they do, handles what they've authorized, and hands them a short list of what it did and what only they can decide. The framing to leave them with is not "an agent that drafts while you sleep" but "you stop being the person who has to check."

## Homework

The goal before next class: an agent the student trusts with the work they hand it, one they rarely need to correct, because Class 6 hands it jobs to do without being asked and that only works on a foundation they already trust. The three directions are the student's choice of how to get there; all are valid, and they pick the one that helps their business most. (1) Give the agent more automations: another scheduled task in the same project (a weekly wrap-up, a Friday unpaid-invoice check, a Monday plan), which gives the agent more to work from; it's the Class 4 pattern again (fixed steps, exact rules, read-only), so reuse that slide's approach. (2) Expand the morning brief: add a source, sharpen what counts as urgent, or change the sections, which improves both the brief and the agent's to-do list. (3) Keep refining the agent: hand it items every morning, and on each correction ask why, then fix the cause (a rule in the directions, a fact in memory, or a connector setting). Help fully with the mechanics; the choice of direction and the judgment calls are theirs. A practical test that they've arrived: they send its drafts with barely a change, and they've stopped double-checking the tasks it files. Whatever they pick, they keep one list: what they ask the agent to do most often. Those repeat jobs are next class's starting point, the jobs the agent takes on without being asked.

## You shipped it

Recap: an agent in the same project as the brief, directions that say who it is, how it uses the brief and what it may do, limits loosened on purpose (it drafts and files, and nothing goes out until they send it), and a memory that keeps what it learns. The through-line to Class 6: it stops waiting to be asked. It reads the brief first, handles what they've authorized, and hands them a morning handoff: what it found, what it did, and the few things only they can decide. If a student asks what they actually learned, name it: telling an automation from an agent, writing down how they work, deciding what software may do in their accounts, and correcting it at the cause.

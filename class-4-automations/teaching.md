# Teaching notes — Class 4 (Automations)

Per-slide notes for the bot view. `##` = slide label. Private. Teach the skill, don't
perform the build. The build lives in the Claude app: a Cowork project with a scheduled
task that reaches the student's accounts through connectors. New territory this class:
connecting real accounts, so the rule you must never let slide is that read-only is a
SETTING (connector permissions: send, delete and anything that changes an account set to
Blocked), and that no password or key is ever typed into the chat. Also teach the
fixed-rule-vs-judgment split, one connector per app, and a brief that is honest when it
fails.

## What this is

Teach the category so the whole class clicks: an automation does the busywork so the student doesn't. The examples (sort my inbox, draft the reply, summarize the thread, chase follow-ups) share one thing worth naming — each READS something and makes a small JUDGMENT (what's urgent, how to reply, what matters). That "deciding" is the interesting part and exactly the one step today's build leaves to Claude. If a student thinks automation means "rigid robotic macros," reframe it: the value is the judgment step, not just moving data around.

## The thing itself

The morning briefing, shown — teach why it feels different from a raw feed. It pulls from where their day actually lives and, instead of dumping lists, USES JUDGMENT to sort signal from noise (needs-you-today / worth-a-glance / handled-noise). Something read all of it and told them where to look first — that's the part only judgment can do, and the one step they leave to Claude. Every item links back to the email, meeting or task it came from; mention it, because next class an agent works from those links. Reinforce the safety framing that recurs all class: it READS but never touches — never sends, deletes, or moves anything in their accounts. It briefs; they stay in control of every action. A worried student needs to hear that clearly.

## The method

The skill they'll reuse for ANYTHING they automate, and the only real work they do: map the process the way they actually do it, step by step, then hand the map to Claude — Claude sets up the automation around it. They're not writing code, they're describing a routine. The reassurance to give: they don't have to map it perfectly alone — Claude helps map it, filling in skipped steps and asking about forgotten cases. Mapping is a conversation, not a test. If a student freezes on "I don't know how to describe my process," tell them to describe it roughly and let Claude interrogate it into completeness.

## The key question

The concept that makes automations reliable — teach it well. Ask of every mapped step: can a FIXED RULE do it (one right answer, same every run) or does it need JUDGMENT? Most steps are fixed (pull today's calendar, unread email from the last 24 hours, tasks due today); only "what's urgent vs noise" needs judgment. The discipline: write every fixed step as an exact instruction, and leave Claude to decide only what no rule can. That is the line between an automation and an agent: in an automation, the student decides the steps in advance and they never change; an agent (next class) decides its own steps. Two reasons — CONSISTENCY (exact instructions give the same brief every morning; vague ones let it wander) and COST (the less it has to figure out, the less plan usage each run takes). If a student wants to just say "give me a morning brief," this is the pushback: a vague instruction hands Claude the steps, which makes it an agent, and the brief will drift from morning to morning.

## Pluggable

Teach the architecture idea and the one requirement. Each app gets its own connector — a ready-made link inside the Claude app, one sign-in, no keys to copy — so they plug in whatever's relevant to THEM. Pick ~3 to start so the briefing runs today, add more later. The one requirement for any source: it has to be in the Claude app's connector directory. If it isn't, leave it for now rather than improvising a workaround. Everything stays read-only, and a few slides later they lock that in as a setting. Why one connector per app matters (say it — it pays off next class): if one breaks the others keep working, adding a source never touches the rest, AND next class an agent uses these same connectors to act on the brief.

The bigger principle to extrapolate — teach it, because it applies to EVERYTHING they build, not just source-picking: start narrow and small, prove it works end-to-end, THEN tack things on. "Pick three sources" is one instance of a general rule. If a student tries to do too much at the start — every source, every feature, all at once — they create a huge fix-it backlog: many things broken simultaneously, and it becomes near-impossible to tell which piece failed. Whereas a narrow first version that actually runs gives them a working baseline to add to one piece at a time, testing each. So if a student wants to connect ten things at once, or pile on features before the core runs, steer them back: get the smallest working version running first, then grow it. This is the same "core first, then extend" idea as the Set-up-the-build note — this is the WHY behind it.

## Runs without you

Teach what makes it an automation, and the one exception. The briefing is a SCHEDULED TASK: they set the time once and Claude runs it in the cloud every morning, whether their computer is on, asleep or closed. Nothing to install, no server. They can read the brief from their laptop or from the Claude app on their phone. The exception worth understanding: the "Require this computer" toggle. If a source is a file that only exists on their computer, they turn it on, and then the task only runs while that computer is awake. Everyone else leaves it off. If a student asks "what if my laptop is closed?", this slide is the answer: it still runs.

## The project

Teach the project as the home for the whole build. In the Claude app, a project keeps everything for one job in one place: their instructions (what matters to them), the scheduled task, and every brief it writes. Claude doesn't remember yesterday's chat, but a project keeps its instructions, and every task in it reads them before it starts, so they set them once. Why it matters especially here: next class an agent joins this SAME project, reads the same briefs and follows the same instructions. Nothing built today gets rebuilt. Make sure they create a new project for the briefing rather than working in a loose chat.

## Set up the build

One prompt sets up the whole automation; the student answers its questions and checks the result, and doesn't paste more steps. They create a new project called Morning Briefing, switch its message box from Chat to Cowork (the toggle under the box), and paste the prompt there. If they paste it with Chat selected, have them switch to Cowork and paste again. The prompt has Claude ask which tools they want it to read (any tool with a connector, not just email, calendar and tasks), help them pick three to start, and agree, for each one, on exactly what to pull so it's the same every morning (the email/calendar/tasks rules in it are examples, not a fixed choice). That agreement is the key-question slide in practice: "check my email" is vague; "unread email from the last 24 hours" is a fixed rule. There is no separate plan step: after they paste it, Claude asks which tools to connect and what to pull from each, then sets it up. Once it's set up, coach them to check it covers four stages: 1 the connectors (one per app they picked, each connected before it runs), 2 the fixed steps (exactly which emails, which days, what format — the same every morning; this is the key-question slide made real), 3 the judgment step (one step that decides what matters, using the project's instructions), 4 schedule + prove it (their time, plus one run now so they see the brief). If any stage is missing, or the steps are vague ("check my email"), tell Claude what to fix. If it set the task to need their computer, ask why: it should only need it when a source lives only on that computer. The discipline to reinforce hard: START WITH THREE SOURCES OR FEWER. Get the whole thing working end-to-end first, THEN add more. This "core first, then extend" rule applies to everything they build.

## A new habit · Permissions

CRITICAL SAFETY TEACH — this is the most important note in the class. Connecting real accounts means Claude can reach them, so before the first run they decide exactly what it may do there. In Customize → Connectors every connector lists its actions (read, search, draft, send, delete…) and each gets one of three settings: Always allow (it just does it), Needs approval (it asks first), Blocked (it can't, even if it tried). Today's rule: allow the reading actions; set send, delete and anything that changes their accounts to Blocked. The briefing only reads, so reading is all it may do. Make the distinction land: "never send" written in the instructions is a request; Blocked is a lock. Next class they will loosen one or two of these on purpose, for drafting; today everything that writes is locked.

The second rule, enforced every time: NEVER have the student type a password or key into the chat. Connectors sign in through each app's own sign-in page, so Claude never needs one. If anything asks them to paste a password or key into the chat, they stop. If a student starts to paste one to you, STOP them and redirect to the connector's own sign-in. This is the one place in the class where a wrong move has a real security cost — hold the line firmly and explain why.

## Plan step 1 · The connectors

Teach the one-connector-per-app idea in plain words. Claude checks each app they picked; if one isn't connected yet, it tells them. Their only job: open Customize → Connectors, find the app, sign in with that app's own sign-in page, then set its permissions as on the Permissions slide. Why one per app: if one breaks the others keep working, and adding an app later means adding one more connector with nothing else changing. If a connector fails, test that one on its own. If their tool isn't in the connector directory, leave it for now and get the brief running with the ones that are.

## Plan step 2 · The judgment

Teach how the automation knows what "matters" — via the project's INSTRUCTIONS. Teach it from scratch, assume they've never written any: a box of plain-English rules that every task in the project reads before it starts. Every morning the task reads them before sorting. This is the ONE thing they truly shape. Teach them to write what urgent means TO THEM ("Flag anything from a client or with a deadline today. Skip newsletters. Keep it to five lines."). Change the instructions and tomorrow's brief changes — nothing else touched; tune them over the first few mornings until it thinks like them. Only they edit the instructions; the task reads them but never changes them, so what matters stays their call. The big idea to plant: these instructions are the SEED OF AN AGENT — next class an agent in this same project follows them too, and starts keeping its own memory of what it learns from them.

## Plan step 3 · Deliver + schedule

Two small pieces, Claude sets up both, student approves. (1) Where the brief lands: each morning's brief is saved in their project, dated, so they keep a history; they can open it from the laptop or the Claude app on their phone. Nothing is sent anywhere — it only reads sources and writes the brief. (2) The schedule: they pick the time (weekdays at 7:00am is a good default) and leave "Require this computer" off unless a source lives only on their computer. Their only input is the time.

## Plan step 4 · Prove it

Don't wait until tomorrow morning to find out if it works — run it now, live, in the room. Three checks: (1) ask Claude to run the task once → it pulls the sources, sorts, and writes the brief; (2) read it → does "needs you today" actually look right? If not, change the instructions, not the brief, so the fix sticks for every morning after; (3) confirm the schedule shows its next run at their time. "A real brief in the project + a schedule that runs tomorrow without you, laptop open or closed" = a working automation. If something's off (brief empty, a source missing, a connector errored), describe exactly what they saw to Claude — that's the habit for anything they build. Push back on any urge to "trust it'll work tomorrow" — prove it live now, because a scheduled thing that silently fails is worse than none.

## Extend it

Once the briefing works, they can add more FIXED jobs — still predictable, still scheduled, still read-only. Two easy adds: a weekly wrap-up task for Friday afternoon (what got done, what slipped, what's coming Monday — same sources and instructions, different schedule), and a step that searches the news for their industry or a competitor and puts the one headline worth knowing in the brief. The crucial boundary to teach: these are still THE AUTOMATION — fixed steps they wrote. It reads and reports; it doesn't act. Drafting replies, filing tasks and prepping meetings are acting on their behalf, and that's Class 5. If a student wants it to start doing things in their accounts, that's the line: today's tool is trustworthy precisely because its steps are fixed and its connectors are read-only.

## When it breaks

Teach the reliability mindset — the difference between a toy and a tool. An automation you rely on has one real danger: it stops working and you don't notice, which is worse than no automation because you've stopped checking by hand. So build in honesty, as two lines in the project's instructions: (1) it SAYS when something failed — if a connector is disconnected or a source can't be reached, the brief says so at the top ("couldn't reach your calendar this morning") instead of quietly leaving it out; (2) silence never means "fine" — it writes a brief even on a quiet day ("all clear, nothing urgent"), so NO brief means something's wrong, never "all good." A small ask that makes the thing trustworthy enough to actually depend on.

## Homework

Do-it-yourself homework — but that does NOT mean refuse to help. Walking them through it IS the skill; the class is about the student using Claude to implement things. Help them fully. The real line is engagement, not hand-holding: don't do it FOR them while they sit passive. Here the split is clean — the SETUP is fair game for Claude to walk them through (connecting the app, setting its permissions, adding the step to the task, running it once), but the DECISION is theirs: WHICH source to add — the one that makes the brief genuinely theirs (whichever of email, calendar or tasks they skipped, Notion, a Google Drive sheet, or something only they'd track). That choice is the point of the homework and no one else can make it. Reinforce it's the SAME pattern they did three times today: connect it, set permissions, add one step, run it once. Coach the pattern, help them implement, but keep the "what's worth tracking" call with them.

## You shipped it

Recap slide. Reinforce what they now have: a scheduled task that briefs them every morning with the laptop open or closed, fixed steps they wrote with one judgment step following instructions only they edit, connectors locked to read-only by a setting, and a brief that tells them when it breaks. The through-line to next class: an agent joins this SAME project, reads the brief, and they tell it what to handle ("prep me for the 2pm," "draft the reply to #2"). The distinction to leave them with: an automation follows steps you wrote, on a schedule; an agent decides its own steps toward what you ask. If a student is proud but unsure "what was the point beyond a morning email," name it: they learned to map a process, split fixed rules from judgment, lock down what software can do in their accounts, and build something reliable that runs without them — the foundation for real agents.

# Teaching notes — Lightning Lesson (What an AI Agent Really Is)

Per-slide notes, keyed by slide label (`##` = the slide's `data-label`). These are
written for the person reading this deck AFTER the session, with Claude, trying to
reproduce on their own business what they watched Eric do.

**This session was a demonstration. Nobody built along.** Eric set up the agent,
sent the job, and read the brief on his own screen. So a reader arriving here has
almost certainly NOT done any of it yet. Never speak as though they already have a
folder of messages or already have a brief. They watched; now they want to do it.

**What they are trying to reproduce, end to end:**

1. Open the Claude desktop app and go to the **Code** tab (not Chat, not Cowork).
2. Export a week of their own real customer messages as one spreadsheet and put
   it in a folder.
3. **Routines → New routine → Local.** Name it, paste the standing instruction
   into Instructions (the job, their own categories, the "be selective" line),
   pick the folder, Accept edits, schedule Daily, save.
4. **Run now.** Let it work, then read what it produced *and what it left out*.
5. Disagree with something, **Edit** the routine's instructions rather than the
   answer, and it stays fixed for every run after.

If someone lands here without a specific question, that sequence is the answer.
Walk them through it from wherever they actually are.

**Who they are:** non-technical small business owners, many of whom have been made
to feel stupid by developer tools before. Some are new to Claude this week. The
governing test for every answer: does this leave them calmer and more capable, or
further behind? Ask what they're seeing on screen before diagnosing, and never
assume terminal skills.

**The one framing that must not drift** (this is the deck's spine, and it is the
thing most likely to get edited away):

> The free lesson teaches *I can make an agent.* The course sells *I can make my
> business operate this way.*

The ceiling is **reach**, not scheduling and not automation. The agent they built
is real and it is genuinely theirs; what it cannot do is go and get the work. They
carry the pile to it. Name that limit once, on "What you own," and close it once,
on "What's next." Blur those two and the session has given the course away.

---

## What you need

The only genuine prerequisite is the **Claude desktop app, signed in, on a paid
plan**. No terminal, no code editor, no GitHub, no API key, no credit card.

If a student is unsure whether they qualify: they need a paid plan, because the
Code tab and Routines are not on the free tier. That is the one thing that will stop them cold, so check
it first if nothing is working.

Nothing here requires technical background. If they are hesitating because it
sounds like developer territory, that hesitation is the main obstacle, not any
actual difficulty.

**"Just watch this one" is sincere and load-bearing.** This audience tenses up the
moment they think they have to keep pace. Say it early and mean it.

## The finish line

**Show the destination before explaining anything.** The brief is on screen in the
first three minutes so that every abstract idea afterwards has somewhere to land.

The beat that matters is the second one: **point at the last section.** The spam,
the thank-you note and the two it handled itself are not in the brief proper —
they are listed at the end with a line each on why. Nothing told it which ones to
drop. That decision, made visible, is the entire lesson, delivered before the
word "agent" has been defined.

**Do not say the dropped items are missing.** An earlier draft of this deck taught
absence, and it is now wrong: the instruction asks the agent to show its working,
so the drops are on screen. Shown-with-a-reason is the stronger demo anyway —
the room can see the judgment and argue with it rather than inferring it.

Do not explain how it worked yet. Let it be slightly magic for ninety seconds. The
explanation is the next three slides and it lands better against a thing they have
already seen.

If someone asks "is this just a summary?" — that is the perfect question and the
answer is what they watch for at the check-in: what it left out, and why.

## Three words

**The distinction the whole session hangs on.** The framing that matters: the
word "agent" gets used loosely, by everyone, and hardly anyone stops to say which
thing they mean. That is all that is going on. There is no live debate about the
definition and nobody is being deceived — it is just loose usage.

**Be precise about WHERE the looseness lives.** Nobody calls a chatbot an agent;
that one is well understood and it is on the slide as the familiar baseline, not
as a source of confusion. The conflation is between **automation and agent**, and
it is the only one worth spending time on. Saying "all three get called agents"
is wrong and a student will know it is wrong.

Two framings to avoid, both of which were in earlier drafts of this deck:

- **Do not suggest anyone is being lazy or dishonest.** This audience has been
  made to feel stupid by jargon before, and telling them the confusion is
  someone's fault leaves them no better off.
- **Do not stage a disagreement that isn't happening.** Nobody is arguing about
  what the word means. Framing it as a contested term is just as wrong as framing
  it as a scam, and it makes the session sound academic.

The useful move is not to hand them the correct definition. It is to give them
three shapes they can recognise, so that when someone says "agent" they can ask
which one is meant. That is a question they can actually use.

- **Chatbot** — answers, then waits. Nothing happens unless you are there.
- **Automation** — repeats fixed steps you wrote down once.
- **Agent** — chooses. What it does next depends on what it finds.

**Do not sneer at automations.** Most business problems genuinely are automations,
they are cheaper and more predictable, and a student who leaves and builds one has
done the right thing. The deck says this out loud on the next slide and it should
be said warmly. Overselling agents here would undercut Class 4 and mislead people.

The three example lines under each card are doing quiet work — they are the same
task phrased three ways, so the difference is visible rather than asserted.

## The test

**One question: who decides what happens next?**

**The trap this slide exists to avoid, and it has caught two earlier drafts of
this deck: "is there judgment involved?" is NOT the test.** An automation can
absolutely contain a judgment call — a fixed script that stops at one step and
asks an LLM "is this urgent?" is doing real thinking, and it is still an
automation. Class 4 of the paid course builds exactly that. If you teach
judgment-equals-agent, you contradict the course and a sharp attendee will catch
it.

What actually separates them is **who chose the route**:

- **You chose it → automation.** You set the order; it follows the same path
  every run. Judgment can live *inside* a step you placed, and often should.
- **It chooses → agent.** You gave it the goal, not the sequence. What it does
  next depends on what it just found, so the path is different run to run.

The sentence to land: **judgment alone doesn't make it an agent — the question is
whether the thinking changes where it goes next.**

Be honest that most of their problems are the left column and they will be
happier building those. Credibility here buys the right to be believed about the
right column. This also sets up the next slide, where the standing instruction
hands over the route rather than the steps.

## Which tab

**The likeliest silent failure of the whole session.** Routines — a named agent
with its own instructions, folder and schedule — live in the **Code** tab. Chat
cannot do this, and Cowork's scheduled tasks now run in the cloud and cannot be
tied to a folder on the student's computer.

- **Chat** — the familiar one. You ask, it answers.
- **Cowork** — you hand over one job and walk away. Good, but it is one job.
- **Code** — works directly on the student's own machine. The only place you can
  set something up that keeps running after the window is closed. Where today
  happens.

**The name puts people off, and the same reassurance from the AI visibility lesson
applies:** nobody writes a line of code. It is called Code because it can act on
your machine, and an agent that runs on its own needs exactly that.

**Why not Cowork, if a student asks:** it is where you hand Claude one job. Today
we are setting up something with a name that stays in a list and runs on a
schedule, and that lives in Code. Not a knock on Cowork; a different shape of
thing.

If a student says they cannot find Routines: it is in the Code tab sidebar, or
under the sidebar's **More** menu, and needs a current desktop app. If it is
genuinely absent after an update, that has happened to others; restarting the app
or updating usually restores it.

## Local or cloud

**The New routine form asks this first, so the deck answers it first.** One rule,
and it is about where the work lives, not about the student:

- **Local** if *any* input or output is a file on their computer. It can open
  their folders and write back into them. It runs while the machine is on and the
  app is open.
- **Cloud** only if *everything* the agent touches already lives online — email,
  Drive, calendar, the tools they log into. It cannot see their computer at all.
  It runs with the lid closed.

Students will notice the two halves of the Local rule are the same statement
("needs files on my computer" and "an input or output is on my computer"). They
are. Say it once, as one rule.

**Today is Local, and say why in one sentence:** the spreadsheet is a file on the
desk, so the agent has to be where the desk is. Stop there. Do not go on to
explain that connecting the sources online is how it becomes a cloud routine
that runs with the lid closed — that is the "What's next" slide's job, and
saying it here gives the course away three slides before "What you own" has
named the limit.

**Do not overclaim what a cloud routine can connect to.** Anthropic's docs
confirm cloud routines run on their computers on a schedule with no access to
local files. Which online sources a non-technical student can hook to one is not
something to assert from the stage; if asked, the honest answer is that it works
when the sources are online and that connecting them is what the course does.

If a student picked Cloud by mistake and it cannot find their folder, this slide
is the diagnosis: it is on Anthropic's computers and their folder is not. Make a
new routine and choose Local.

**Missed runs catch up on their own, and say so, because everyone who has ever
set a schedule assumes they don't.** Verified against the desktop scheduled-tasks
doc on 2026-09-15: when the app starts or the computer wakes, it checks the last
seven days and fires exactly one catch-up run for the most recently missed time,
discarding anything older. A daily task that missed six days runs once. No
setting to enable, nothing to add to the instructions. (This is the opposite of
plain cron, which silently drops missed runs — anyone who has built their own
automations will expect the cron behaviour.)

Two honest caveats that go with it: the catch-up may fire at 11pm if the machine
slept all day, so if timing matters the guardrail goes in the instructions — the
doc's own example is "if it's after 5pm, skip the review and just summarize what
was missed." And **Keep computer awake** (Settings → Desktop app → General) stops
idle sleep but closing the lid still puts it to sleep.

## Set it up

**This is the slide that makes it an agent rather than a prompt, and it was
missing from an earlier draft.** A routine is a named thing with its own
instructions, its own folder, its own schedule, that sits in a list and can be
edited. A prompt in a chat window is none of those.

1. **Code** tab → **Routines** in the sidebar (or under **More**) → **New routine**
   → **Local**.
2. **Name** it (something like "customer signal agent"). Paste the standing
   instruction from the next slide into **Instructions**. Pick the folder the
   export is in — a folder is required. Set the permission mode to **Accept
   edits**: it can write its brief into that folder; anything beyond that asks
   first. (Do not pick Auto or Bypass on stage; the Safety slide is three slides
   away and this is where its rule gets applied.)
3. **Schedule → Daily.** Save. Then **Run now**, because nobody is waiting until
   9am. A session appears under **Scheduled** in the sidebar; that is where you
   watch it work.

**The alarm-clock line, and say it, because a sharp student will raise it:** a
schedule does not make this an automation. The test from the previous slides is
*who decides what happens next*. The timer decides only when it wakes up. Every
decision after that — what to read, what matters, what to drop — is the agent's.
Nothing about a cron changes who is deciding.

**The folder is the desk.** It reads every file in it and writes its output back
to the same place. Nothing is uploaded and nothing leaves the machine, which is
worth saying out loud to an audience nervous about handing over customer mail.
Honest limit, and it is the ceiling slide later: it runs only while the computer
is on and the app is open. A missed run catches up once, automatically, when the
machine wakes — the detail is in the "Local or cloud" notes.

**What persists.** After saving, the routine is a card in the Routines list, and
the instructions also exist as a real file on disk under
`~/.claude/scheduled-tasks/`. **Edit** on the routine changes the instructions,
schedule or folder for every future run. That is what "fix the criteria, not the
answer" means physically, on the "When it's wrong" slide.

**The UI labels are current as of 2026-09-15 but the app moves fast.** If a button
has been renamed, the shape still holds: Code tab, a routine, a folder, a
schedule, run it once by hand. Teach the shape, and read the current label off the
screen.

**What the messages are.** The demo folder holds ONE file: a week of support
messages exported as a spreadsheet, 16 rows, one per message, with the columns a
real helpdesk export carries (ticket, received, channel, name, email, plan,
subject, message, status). That is the honest shape of rung one — no email
integration, the owner exported last week and dropped the file in a folder. A
folder of separate text files would be less true to how this actually works.

The file is generated by `agents/sample-data/generate.py` and written into
`agents/sample-data/inbox/`. **Point the routine at a folder holding only the
export, never at `sample-data/`** — if Claude can see the generator it reads the
seeded design and the demo is spoiled. A student reproducing this should export their own week from whatever
holds their messages (helpdesk, contact form tool, shared inbox) and put that one
file in a folder.

The business in the sample is Bookable, a small scheduling and invoicing tool for
service businesses, which is why a QuickBooks sync request is natural. The mix is
deliberate:

- **Two clear escalations** — a double charge (money, wrong right now) and a
  cancellation (revenue risk, with a *reason* attached).
- **Two clear drops** — spam and a compliment. These prove exclusion.
- **One ordinary support issue** — a login problem. Handled, not escalated, so
  the room sees the middle of the range rather than only the extremes.
- **Three versions of the same question, worded differently** (QuickBooks in the
  demo). This is the one that makes the session.

**If you rebuild the set, keep the duplicate.** The pattern beat on "Read the
brief" has nothing to find without it, and that beat is the strongest proof in
the deck that this is judgment rather than sorting.

## The instruction

**The conceptual centre of the session: the difference between asking and
delegating.** A prompt asks for output and keeps the route — you decide what to
do with what comes back. A job hands the route over: criteria, an expected
deliverable, and the right to leave things out.

**Tie this back to the previous slide.** The test was "who decides what happens
next," and this instruction is where that decision physically gets handed over.
Not because it invokes judgment — a prompt can do that too — but because it names
the goal and leaves the sequence to the agent.

The left card is what a chat user would type, and it is not stupid — it would
work, and it would hand back all ten, shorter. The point is that **you still have
to read it and decide.** That is the thing being removed.

**"Be selective. If it doesn't deserve a founder's attention, leave it out."** is
the line that makes it an agent, and it is worth saying twice. Permission to omit
is permission to decide.

**The line after it is the one that makes the agent checkable**, and it is there
for a practical reason worth saying out loud: asking it to list what it dropped,
with a one-line reason each, is how you debug and evaluate judgment. Without it
the agent's decisions are invisible and you are trusting it blind. With it you
can see a bad call and fix the criteria.

This is a habit to teach generally, not a trick for this demo: **whenever you
hand judgment to software, make it show its working.** An agent that silently
omits things is one you can never audit.

**This text is what goes in the routine's Instructions box.** Paste it, save,
click **Run now**, and let it run. This is the aivisibility pattern: fire the
work, teach through the wait, come back to it. The next three slides are written
to fill that dead air and they teach things worth teaching regardless, so nothing
is wasted if the run is fast.

The left card says "all sixteen back" because the demo export has sixteen rows.
If the export changes, change the number.

If the run finishes early, do not skip the three teaching slides. They are the
session, not filler.

## What it actually is

*Taught while the agent works.*

**An agent is a job, and the freedom to do it.** Resist the urge to add a fourth
thing to this. An earlier draft of the deck listed five components and it was
murky; the simplification is the improvement.

The three chips are additive on purpose: a job worth doing, what you care about,
room to decide. **Take away the third and you have an automation. Take away the
first and you have a chatbot.** That single sentence ties this slide back to
"Three words" and is the cleanest definition in the deck.

The employee-versus-vending-machine comparison works well with this audience
because it is about delegation, which they already understand, rather than about
software, which they do not.

## The judgment

*Taught while the agent works.*

**The five categories are doing all the work, and none of them is technical.**
Noise, support issue, product signal, revenue risk, emergency.

The point to land: **you do not teach it your business, you teach it what counts.**
A student will assume the hard part is explaining their company. It is not. The
hard part is naming the handful of buckets they already sort by instinctively.

**"This is the part you can't buy"** is the honest and durable claim. Nobody can
sell them the list of what matters in their business, because it lives in their
head and has never been written down. Writing it down IS the work, and it is also
why a vendor's generic triage tool always feels wrong.

Encourage them to change the five. A clinic sorts by "is this clinical." A shop
sorts by "is this a refund." Their five will be different and should be.

## Safety

*Taught while the agent works.*

**Reframed from an earlier "consent" framing to safety**, which is the more useful
concept for this audience and the more honest one.

Three tiers: safe from day one (read, sort, recommend, draft); the line to hold
(anything reaching a customer, moving money, or irreversible waits for you); and
earn it slowly (let it act where you have watched it be right and where being
wrong is cheap).

**The reason the line exists is consequence, not distrust.** Say it that way. The
software is not shifty; it is that the fallout lands on them, so the decision
should too.

The warning is the practical version: do not wire an agent into something that
sends, deletes, or charges on day one. Start where the worst case is that you
disagree with it. Every student who gets burned on this got burned here.

## Check in

**Back to the run.** Answer whatever it asked, let it finish.

**What to say you are looking for:** not whether it wrote something, because it
always will. **Whether the things it left out were the right things to leave out.**
That sentence re-points the room at exclusion right before the payoff slide.

**If it asks a question, that is a feature.** An employee who never asks anything
is not careful, they are guessing. This reframe matters because a student watching
their own agent ask a question will otherwise read it as failure.

If the run went badly or produced something thin, say so plainly and work with what
is there. The audience forgives a live build going sideways; they do not forgive
being told something worked when it visibly did not.

## When it's wrong

**Fix the criteria, not the answer.** The whole slide is one idea.

Fixing the answer gets you a better brief today and the identical mistake next
week, forever. Fixing the criteria gets you a better brief today **and every week
after**, and the agent becomes more yours over time.

This is why the instruction lives in a document rather than a chat message. They
are not correcting an output, they are editing a standing job.

**Frame a disagreement as the first day of a new hire, not a failure.** This
audience reads any wrong answer as proof the technology does not work, and that
reading is the single biggest reason people abandon this after one try.

## What you own

**Lead with ownership, name the limit second, and stop there.** Do not explain how
the gap gets closed. Do not say "and in the course you'd connect your real inbox."
The "What's next" slide is ninety seconds away and does that job properly.

The ownership half is genuinely strong and should be sold properly: it has a job,
it has their judgment written down, it makes decisions they would otherwise make
themselves, and it costs nothing beyond the subscription they already have. **"Go
and use it" is sincere** — someone who only ever does the free version should be
better off, and you should mean that.

Then the limit, plainly: **you hired someone very good and you are still walking
the paperwork to their desk.** Say it, let it sit, move on. Do not elaborate.

**This slide protects the honesty of the whole session.** The seam between an agent
you hand a folder to and an agent that goes and gets the work is the pitch. Keep it
sharp and it sells itself; blur it and the class is given away.

## The ladder

**The course pitch without pitching.** They have done the first rung and can now
conceptualise the rest, which is a thing they could not do an hour ago.

Read the rungs as a progression of **what you stop carrying by hand**, not as a
feature list:

1. **Today** — a folder you hand it, a brief you open.
2. **Next** — it reads your actual inbox and helpdesk, and the answer is waiting
   where you already work.
3. **Then** — several sources at once, and it acts on the safe ones.
4. **Then** — something happens, several agents share one picture of the business,
   and the whole thing is watched.

**Do not oversell rung four.** It is real and it is where this goes, but a student
who expects it next month will be disappointed. The honest framing is that each
rung is the same idea reaching a bit further, and they have already done the part
that is conceptually hard.

## The real lesson

**The spine. A teaching slide, not a pitch, and the pitch does not start here.**

**Silence is the technique.** Three short paragraphs, big type, long pauses between
them. Do not fill the gaps. Read the last line, then stop talking for a full two
seconds before advancing.

The turn, said close to the slide wording because it is the thesis: they handed
over a decision and kept the veto. Customer messages were the vehicle, not the
point.

Then the skill, stated as something repeatable: **write down what you actually care
about** — the thing they have been carrying in their head and calling instinct —
and let something else apply it while they remain the one who decides.

The line to land, in their own words: the question stops being what software can do
and becomes which of your judgment calls you are willing to write down. That is the
durable takeaway and it is true whether or not anyone buys anything.

## What's next

Sets up the ask without making it. **Don't do the pitch twice** — the offer is one
slide away, and doing it here spends it early.

Three classes, one a week. Read the rows as a progression, not a list: first the
briefing, which is the readers — the agent's senses, built as a fixed routine.
Then the agent itself, which is today's build given those readers and a schedule.
Then the handoff, where it starts acting on the safe jobs and moves off the
laptop. Today was a short version of the second class.

**The card on the right is where today's ceiling gets closed, and this is the only
place it should be closed.** Frame it as three things the course gives the agent
they built today:

- **Senses.** It reads where the work actually lives — inbox, calendar, tasks,
  payments — instead of a folder they fill.
- **A home that's always on.** A machine that is up when the laptop isn't,
  remembers between runs, and can be reached — so it reacts when something
  happens, not only when a timer fires. A routine is "wake up, do one job, write a
  result, stop"; a home is what lets it listen and remember.
- **Hands, carefully.** It drafts and files the safe jobs and asks before anything
  it cannot undo.

**The paperwork stops being carried.** That is the sentence.

**The third table row is the transferable lesson, and worth reading aloud:** which
jobs belong in a routine and which need a home. If it can be done by waking,
thinking and writing, it is a routine. If it has to listen, remember, or do real
work on files, it needs the machine. Knowing the difference outlasts any one tool.

**What does not change, if anyone asks about cost:** the thinking costs money
either way — a routine bills against the Claude plan they already have, and the
course's agent bills the same way — and any outside tool they connect keeps its
own bill. The course does not make it free. It moves it off their laptop and into
the business. Say this plainly; this audience respects it.

This mini course is the back half of the six-class course, sold on its own, with a
third class that goes further on agents than the six-class version does. If a
student later takes the website course, what they paid here comes off the price.
Say that only if asked; the slide sells three classes.

Both doors are genuinely real. The whole course is free on YouTube at
**ericgrows.com**, same material, at their own pace. The paid cohort adds live help
when they get stuck. Routing someone to the free version who would be unhappy
paying is a good outcome.

## The offer

**Build an AI Agent for Your Busywork with Claude Code**, verified against the live
course page on 2026-09-15:

- Three weeks, October 15 to 31 (the next cohort)
- 6 live sessions, 3 lessons, 3 projects: 3 hours for each of the two build
  classes, 2 hours for the handoff class, plus an optional office hour each week
  and an optional bonus hour on strategy at the end
- $1,095, and **LL15** takes 15% off (about $931). One code, given to the people in
  this lesson. Do not attach a cohort restriction to it that the slide does not
  make.
- Lifetime access to recordings, office hours after every class, Maven guarantee
- Extra costs a student will ask about: a paid Claude plan, and the always-on
  home the agent moves to in Class 3, about $25 a month
- maven.com/ericgrows/build-an-ai-agent-for-your-busywork

**Say the safety line if anyone hesitates, because the course page makes the same
promise:** it reads their real accounts and never sends, deletes, or moves anything
on its own. In Class 3 it starts acting on the safe jobs they choose — drafting and
filing — and asks before anything it cannot undo. That is the same rule as the
Safety slide, carried through.

**No invented scarcity.** The page states no seat cap, so do not name one. No
countdown theater, no "spots are going fast." This audience detects that instantly.

Still free on YouTube at ericgrows.com for anyone who would rather do it alone.

## Questions

**The real close, and what they should actually do this week:**

1. Write down the five kinds of thing that land on them, and which need them.
2. Put a week of real messages in one folder.
3. Hand Claude the job from the slide, in their own words, with their own five.

Step one is the whole skill and it happens away from the computer. Say that.

Common questions and honest answers:

- **"Isn't this just a summary?"** No, and the proof is what it left out. A
  summary cannot omit. Point back at the dropped items and the pattern it found
  across messages.
- **"Why the Code tab and not Chat or Cowork?"** Chat answers questions. Cowork
  takes one job and does it. A routine is a named thing with its own folder and
  schedule that keeps running after you close the window, and that only lives in
  Code. Nobody writes code.
- **"If it runs on a timer, isn't it just an automation?"** No. The timer decides
  when it wakes up. It decides everything after that — what to read, what
  matters, what to drop. The test was never about the trigger; it was about who
  chooses the route.
- **"What if it gets it wrong?"** Expected, especially at first. Fix the criteria
  rather than the answer, and it stays fixed.
- **"Can it just reply to the customers for me?"** It can draft. Let it send only
  once you have watched it be right for a while, and only where being wrong is
  cheap. See the Safety notes.
- **"Do I need a paid plan?"** Yes, for the Code tab and Routines. That is the one
  hard requirement.
- **"Can it read my real inbox instead of a folder?"** That is exactly the next
  rung, and it is what the course covers. Be honest that it is a real step up and
  not something they will click into tonight.

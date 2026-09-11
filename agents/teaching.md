# Teaching notes — Lightning Lesson (What an AI Agent Really Is)

Per-slide notes, keyed by slide label (`##` = the slide's `data-label`). These are
written for the person reading this deck AFTER the session, with Claude, trying to
reproduce on their own business what they watched Eric do.

**This session was a demonstration. Nobody built along.** Eric set up the agent,
sent the job, and read the brief on his own screen. So a reader arriving here has
almost certainly NOT done any of it yet. Never speak as though they already have a
folder of messages or already have a brief. They watched; now they want to do it.

**What they are trying to reproduce, end to end:**

1. Open the Claude desktop app and go to the **Cowork** tab (not Chat).
2. Put a batch of their own real customer messages somewhere Claude can read them.
3. Hand over the standing instruction — the job, their own categories, and the
   "be selective" line.
4. Let it work, then read what it produced *and what it left out*.
5. Disagree with something, and fix the **criteria** rather than the answer.

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

If a student is unsure whether they qualify: they need a paid plan, because Cowork
is not on the free tier. That is the one thing that will stop them cold, so check
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
answer is on the "Read the brief" slide. Tell them to hold it.

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

**The likeliest silent failure of the whole session.** Skills, the agent loop and
long-running work live in Cowork. Chat cannot do this.

- **Chat** — the familiar one. You ask, it answers.
- **Cowork** — you hand over a job and walk away. Where today happens.
- **Code** — works directly on your own machine; where you install new abilities.

The rule of thumb worth giving them: **Chat is where you ask for things. Cowork is
where you hand over a job.** That sentence is also the conceptual lesson, which is
why this slide is not merely navigational.

If a student says the agent will not run or cannot see their files, check the tab
before anything else.

## Set it up

**Three clicks, and this is the slide that was missing.** An earlier draft jumped
straight from the concept to a running agent without ever saying where the work
lives or what you click. A student watching that could not reproduce it.

1. In the message box, choose **Cowork**.
2. In the prompt bar, click **Work in a project or folder** and pick the folder
   the messages are in. The operating system asks permission the first time.
3. Leave the permission mode on **Ask before acting** (the default). Claude
   pauses before anything touches the outside world — sending, posting, sharing.
   Permanent deletion always prompts and that cannot be turned off.

**The folder is the desk.** Claude reads every file in it and writes its output
back to the same place. Nothing is uploaded and nothing leaves the machine, which
is worth saying out loud to an audience nervous about handing over customer mail.

**The UI labels are current as of the build but Cowork moves fast.** If a button
has been renamed, the shape still holds: enter Cowork, attach a folder, keep the
cautious permission mode. Teach the shape, and read the current label off the
screen.

**What the messages should be.** The demo folder is ~10 short files, and the mix
is deliberate:

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

**Send it here and let it run.** This is the aivisibility pattern: fire the work,
teach through the wait, come back to it. The next three slides are written to fill
that dead air and they teach things worth teaching regardless, so nothing is
wasted if the run is fast.

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

## Read the brief

**The payoff, and the proof is what it threw away.** A summary cannot leave
anything out. That is what makes it a summary.

**Read the "didn't need you" section out loud — that is the demo.** The dropped
items are not absent from the file; they are listed at the end with a reason
each, because the instruction asked for that. This is better than silent omission
in every way that matters: the room sees the judgment rather than inferring it,
and you can point at a single line and ask whether you agree. Do not describe the
drops as missing — they are shown, deliberately, as the agent's working.

Walk the verdicts, not the messages. The shape to show is the full range: two
escalated, one handled but not escalated, two dropped, one pattern.

**Spend the time on the QuickBooks line.** No single message said "you have a
QuickBooks problem." The finding exists only across the pile, which means it had to
be *noticed* rather than read. That is the difference between judgment and sorting,
made visible in their own output.

It also sets up a genuinely useful business move that costs nothing: three people
asking the same question is a FAQ entry waiting to be written. Answer it once,
publicly, and it stops arriving. Mention it; do not build it.

**Have a real disagreement ready.** If the brief comes out clean, the next slide is
hypothetical and loses its force. Something ranked lower than you would have ranked
it is enough.

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

Read two rows across the table, not all six. The agent row is the obvious one. Pick
one other and read it the same way. That is enough for the shape to register: every
class builds one real thing and the point is always the skill underneath it.

**The card on the right is where today's ceiling gets closed, and this is the only
place it should be closed.** The automations class is how the agent stops waiting
for a folder — it reaches into the places the work actually lives. Then the agent
class gives that a brain. **The paperwork stops being carried.** That is the
sentence.

Both doors are genuinely real. The whole course is free on YouTube at
**ericgrows.com**, same material, at their own pace. The paid cohort adds live help
when they get stuck. Routing someone to the free version who would be unhappy
paying is a good outcome.

## The offer

**Run Your Whole Business with AI:**

- Six weeks, starting September 29
- $1,795, and **FOUNDER400** takes it to **$1,395**
- **10 founding seats** at that price
- Lifetime access to recordings, 3 months of StratEngine AI Professional
- maven.com/ericgrows/run-your-whole-business-with-ai

**The scarcity is real and should be stated flatly.** Ten seats is ten seats. No
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
- **"Why Cowork and not Chat?"** Chat answers questions. Cowork takes a job and
  works through material on its own. This needs the second one.
- **"What if it gets it wrong?"** Expected, especially at first. Fix the criteria
  rather than the answer, and it stays fixed.
- **"Can it just reply to the customers for me?"** It can draft. Let it send only
  once you have watched it be right for a while, and only where being wrong is
  cheap. See the Safety notes.
- **"Do I need a paid plan?"** Yes, for Cowork. That is the one hard requirement.
- **"Can it read my real inbox instead of a folder?"** That is exactly the next
  rung, and it is what the course covers. Be honest that it is a real step up and
  not something they will click into tonight.

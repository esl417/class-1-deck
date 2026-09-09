# Teaching notes — Lightning Lesson (Build a Dashboard That Thinks Like You)

Per-slide notes. `##` = slide label. Private.

**The shape of this session, and the thing to keep straight:** this is
**lecture and demonstration**. Nobody in the room builds along, and you should
never imply they should. The teaching is the spine; the demo is the proof.

**Nothing is built live in this session, and that is a deliberate decision made
on 2026-09-08 after timing it.** The real build takes **about sixteen minutes**
and varies a lot. The deck can field roughly fourteen minutes of teaching before
the reveal, so a live build would have meant stalling through four slides
watching a clock, and usually falling back to the pre-built file anyway --
after paying the anxiety cost. So: you show the prompt on slide 3, you teach,
and on slide 8 you open `dashboard.html`, which was produced by that exact
prompt against that exact data before the session.

**Say this out loud on slide 3, plainly and once.** "I ran this before we
started; it takes about fifteen minutes, so I'm not going to make you watch a
progress bar." That is the whole disclosure and it costs you nothing --
this audience has sat through enough live demos to be relieved. Do not be
cagey, do not imply it is running in the background, and do not say "here's one
I made earlier" as if it were an apology. It is the professional choice.

**What you lose, and how to get it back.** Running it live proved that one
plain-English paragraph really does the work. You now have to carry that
yourself on slide 3: read the prompt aloud, dwell on the fact that it is a
paragraph and not a command, and point out that everything on slide 8 came from
those words alone. The prompt is on screen the whole time; use it.

**The timing pressure is gone, so slides 4-7 can breathe.** There is no clock
underneath them any more. Teach them properly rather than stretching or
rushing. If you finish early, you have more Q&A, which this session can always
use.

**Why nobody builds along:** the previous lightning lesson had attendees install
and run something themselves, and it worked because the run was fire-and-forget
on their machine. A dashboard build is conversational and every attendee's
session would diverge within ninety seconds -- and it takes about sixteen
minutes, which is most of this session. Seeing one done properly teaches more
than a hundred half-finished ones. Say this out loud once, on slide
2, so nobody feels left out: they're watching, every prompt is on a slide, and
they can do it with their own file afterwards.

**Audience:** non-technical small business owners who have been made to feel
stupid by developer tools before. Some are on Claude for the first time this
week. The governing test for everything you say: does this make them feel calmer
and more capable, or further behind?

**Data is sample data, always.** A made-up business. Say so on slide 2 and don't
be cagey about it. Nothing on screen is anyone's real numbers, including yours.
It is an ordinary order export -- **45 days**, one row per order, a date, a
customer, a channel, what they paid, whether it came back -- plus a small ad
spend file. It is deliberately six weeks and ~4.5k rows rather than six months
and 13k -- a smaller file is faster for anyone re-running this themselves, and
the shorter window is where the capacity squeeze actually shows. If anyone asks:
yes, it is obviously generated, and that is fine, because the shape is what's
being taught.

**The one thing to have straight before you walk in:** the demo's finding is
that returns handling eats **74 of 80** available CS hours a week -- **93%** --
that **62%** of that load comes from paid search, and that a paid-search order
costs **13 minutes** of team time against an email order's **2.5** -- **5.2x**.
That asymmetry is the whole demo: the channel every surface metric says to fund
is the expensive one, and growing it 20% puts you into overtime while every
other channel stays under. If you remember nothing else, remember **93%** and
**13 against 2.5**.

**Every figure in these notes and on the slides is computed from
`sample-data/orders.csv`.** If you change the generator, re-derive them and
update both files -- the deck previously carried a set of numbers the data did
not produce, which would have contradicted the live build on stage.

**Assume radio silence, the whole way through.** Nobody is building along and
nobody is going to answer a question in chat. Every beat in this session has to
work with a silent room, and none of them ask the audience to do anything. The
one exception is Q&A at the end, where questions arrive in writing. Do not
build in pauses that need filling.

**Three things to say out loud that aren't on any slide:**
- On slide 3: "I ran this before we started -- it takes about fifteen minutes,
  so I'm not going to make you watch a progress bar." Say it once, plainly.
- On slide 8, before you open it: everything you are about to see came out of
  that one paragraph. Nothing else was typed.
- Invite chat questions early (slide 2 or 3) so Q&A has a backlog by the time
  you reach it.

**Timing skeleton (45 min):** 1 / 4 · 5 / 4 / 5 / 5 · 5 / 4 · 3 / 2 / 3 / 2 / 4.

Read that as: open (1, 2), **the prompt (3)**, three teaching slides (4, 5, 6),
the payoff (7, 8), then the close. Slide 7 explains the number, slide 8 opens
the screen and proves it; those two are the payoff and the only place
overrunning helps.

No clock runs underneath any of this -- nothing is built live -- so these are
teaching times, not cover times. Slide 6 is the one to compress if you run
long.

**The only failure case left is a missing file.** Confirm `dashboard.html` opens
in your browser before the session and have the tab already loaded. There is
nothing to debug live because nothing runs live. Budget zero minutes.

---

## Where we start

Three jobs, in order: set up the file, set expectations about watching, and
plant the thing that pays off on slide 8.

The plant is the "what is NOT in it" card. Say it slowly and then move on
without explaining it. Twenty minutes later that card is the reveal. Do not
name the constraint here; naming it now spends the payoff early. The card says
the limiting thing "only exists in the owner's head" -- that phrasing is the
whole session in one line, so read it exactly and let it sit.

Say the watching-not-building thing warmly and once. This audience is braced to
be told they're behind, and "you don't have to keep up today" is a relief, not a
disappointment. The heads-up box does the work: every prompt is on a slide.

If someone asks for the sample file in chat, say it's in the follow-up. Don't
break stride hunting for a link.

## The prompt

**Nothing is built live. This slide is the whole demonstration of the input.**
Everything on slide 8 came out of the paragraph on this screen, and since the
room will not watch it happen, this slide has to carry the proof that it really
is just a paragraph.

Open by disclosing it, once and without apology: "I ran this before we started
-- it takes about fifteen minutes, so I'm not going to make you watch a progress
bar." Then move on. Do not imply anything is running now.

Then read the prompt aloud, unhurried. That reading IS the teaching. The room
needs to hear that it is plain English -- no syntax, no settings, no column
names -- and that it is one paragraph a person could have dictated. Take your
time; you have no clock underneath you any more.

Three points off the left card:

1. You did not name the metric.
2. You did not name the columns.
3. You did not describe a layout.

Then the card on the right, which is the one that matters now: you handed over
**three facts that are in no system anywhere** -- two CS people, the 40-hour
ceiling, and how long a return actually takes. Say plainly that this is the
part no software could have done for you, at any price. Your ad platform knows
spend. Your store knows orders. Neither one knows how many people you employ or
what overtime does to your month.

Two more things in the prompt worth pointing at, in this order:

**"A screen I want to open every Monday, so build it to be re-run."** This is
not a one-off analysis of a quarterly budget question -- it is a standing view
of every channel and of how much of the team is left. Say that out loud,
because it is what makes the thing worth keeping. A one-time answer gets read
once and closed. This is the difference between asking a question and having an
instrument, and it is also what sets up slide 9: the file doesn't refresh
itself, but it was built to accept a fresh export.

**"Tell me whether that 40 minutes is what's really limiting me."** You are not
asking for a number, you are asking what your options cost. That is the
difference between a report and a decision tool, stated in the prompt itself.

Then close by pointing forward: everything in the next three slides is the
reason the prompt was worded this way, and then we open what it produced. A
room that doesn't know a payoff is coming will wonder where this is going.

**Do not open `dashboard.html` early**, however tempting -- not even a glance to
prove it exists. The reveal is worth more whole on slide 8 than dribbled out
here.

## Why reports never fit

The critique that was sold in the listing copy, so it has to land properly.
Three beats, and the third is the one that matters.

Built for everyone, so they fit no one. A learning curve before you get your
view. Their vocabulary, not yours. Most of the room has lived all three and has
never heard anyone say it out loud, so expect nodding here. That's the point:
you're naming a frustration they thought was their own fault for not being
"good with data."

Then the turn, which is the actual idea: the number they run on is usually
**computed** from two or three others, so no tool ships it. That's not a
criticism of the tools, it's a structural fact about tools built for everybody.

The small-note at the bottom is the one to say out loud verbatim: they have
exported a report and immediately started dividing one column by another. Do
NOT ask for a show of hands -- assume radio silence all session. Say it as a
statement of fact about them and move on; the recognition happens whether or
not anyone signals it.

Do NOT get into a specific tool's flaws. The moment you say "Google Analytics
is bad" you've lost the people who like it and taught nothing.

## Decision tool

The idea the whole session exists to teach, borrowed from Class 2 where it's the
highest-value beat. Slow down. This is a judgment lesson, not a software lesson.

The contrast cards do the work: a report states facts, a decision tool attaches a
verdict. Read the right-hand column out loud in order and let the last line land
on its own. "You're paying a full kitchen for a quiet room, close Tuesdays or
fill them" is a sentence an owner can act on. "You served 240 covers" is not.

**The example here is a restaurant on purpose, and it is NOT the demo's data.**
Keep it that way. The numbers on the screen you open on slide 8 must be the first
time the room sees the demo's figures, or the reveal lands as a repeat and
your "I haven't seen this output either" line stops being believable. If you
improvise a different example here, improvise one from a different business.

**The branch in the small-note is the most important thing on this slide for the
people who feel stuck.** Most owners cannot name the decisions they make, and
they will read that inability as a personal failing. Say plainly that it's
normal, and that the fix is to have Claude propose the metrics worth watching for
a business like theirs and then pick from the list. Choosing is much easier than
inventing. Do not let anyone leave this slide thinking "I don't know what I'd
track" is a reason they can't do this.

The invariant worth stating: whoever picks the metric, the screen has to explain
itself. A number nobody can interpret is not a decision tool.

## Numbers you build

**This is the listing's central promise, so it has to be taught explicitly and
not just implied.** The registration page says: "the number you actually run on
is usually computed from two or three sources, so no tool ever shows it."
Somebody in the room signed up for that sentence. This is where you deliver it.

It comes from Class 2, where it is called the pro move most people miss. If you
are running long, this is the slide to compress -- but it teaches the listing's
central promise, so compress it rather than cutting it.

**Slide 6 sets up the move. It does NOT do the sum.** That is deliberate and it
changed on 2026-09-08: slide 6 used to compute 112 x 40 = 74 hours, which meant
slide 7 opened by announcing the reveal *after* the number had already been
found. The reveal came before its own setup. Now slide 6 ends on the question
and slide 7 answers it.

Three beats here, and then stop:

1. **The count.** 112 returns last week. Every tool they own can show them that.
   Say plainly that on its own it tells you nothing -- you cannot do anything
   differently on Monday because you saw the number 112. Don't rush; the
   flatness is the setup.
2. **The half you supply.** Forty minutes to deal with one. Put your finger on
   that card. Nobody sold you that number and no system stores it -- you know it
   because you do the job.
3. **The move, stated but not performed.** Multiply one by the other and a
   number you can't act on becomes one you can. Say that it is the whole skill,
   and that no tool ships the result because half of it was never in a system.

**Then stop on the question and leave it hanging: "so what does 112 returns
actually cost me?"** Do not answer it. Do not say 74 hours, do not say 93%, do
not do the multiplication out loud. The next slide is the answer and it is the
one moment in the session where a number is supposed to land hard.

**Keep every word on this slide concrete.** An earlier version used invented
vocabulary -- "a count", "what it costs you", "the load" -- and it was opaque,
because none of those are things an owner can picture. If you find yourself
reaching for an abstraction here, use the number instead. This audience is
already braced to feel stupid; a made-up term is the fastest way to confirm it.

**Do not give away the asymmetry here.** No per-channel breakdown, no 13
minutes, no 5.2x. Slide 6 ends on the question. When slide 7 answers it with
93% and then splits those hours by channel, the reaction you want is "oh -- it's
not spread evenly," and naming it early spends that.

The small-note is homework they can do this week without anything new: ask
Claude to look at your raw columns and propose the numbers worth building, each
with the decision it drives. It generates, you choose. Same shape as the
metric-selection branch on slide 5 -- worth naming as the same move so it
registers as a pattern.

**What this slide is NOT.** Do not turn it into a lesson about iterating on the
build, first drafts being rough, or how to prompt. That is Class 2's build-loop
material, it is tool-specific, and here it would set the room up to expect the
slide-7 reveal to be a rough draft you then have to fix live. You are not
rebuilding anything on stage.

## The verdict

**The headline is "the number nothing else could have told me," and the wording
is load-bearing.** It read "the number it was always going to find" until
2026-09-08, which was wrong twice over: "it" had no referent on the slide, and
"always going to find" claims inevitability when the entire session argues that
no tool was ever going to find this. If you paraphrase this slide out loud, do
not reintroduce inevitability -- the point is that the finding was *unavailable*
to every tool they own, because half its input lives in the owner's head.

**The eyebrows on 5, 6 and 7 read as a sequence** -- "The idea", "The move",
"The answer" -- so slide 7's label is the payoff to the question slide 6 leaves
hanging. Slide 7's eyebrow used to say "The number", which just restated the
first two words of its own headline, and slide 6's said "Still running", which
was a build-status note rather than a topic and tied the slide to timing the
deck deliberately doesn't depend on. If you rewrite either headline, keep the
question/answer pairing.

Referents matter on this slide generally. "The screen" and "my screen" mean the
thing you built today; "every dashboard I own" means the tools they already pay
for. Keep those two straight when you talk over it, because the whole contrast
collapses if the room loses track of which one you mean.

**This comes BEFORE you open the screen, and that ordering is deliberate.** All
the teaching in this session happens before the reveal; nothing after slide 8 is
a lesson. So you explain the number here, in the abstract, and then the browser
confirms it. The room should reach slide 8 already knowing what they are looking
for.

Do not open the file during this slide, however tempting. The moment you switch
to the browser you have spent the reveal.

Point at the diagram in this order, physically: the 88 returns, then the 40
minutes, then the arrow, then 93%. The first number was a column in the file.
**The second one came out of your head** -- put your finger on that card and say
so. It is the same shape you drew abstractly on slide 6, now with real figures
in it, and saying "this is that" out loud is worth doing.

**Two beats on this slide, in order, and don't merge them.** First the 93% --
that is the answer to the question slide 6 left hanging, so let it land on its
own before you say anything else. Six hours of slack in a whole week is the
kind of number an owner feels in their stomach.

Then the split, which is the actual finding: **13 minutes against 2.5.** Say
both, slowly, and let the gap sit before you name the multiple. Two orders,
same shop, same week, and one costs you five times the team time of the other.
Nothing in any tool they own would have told them that, because the minutes are
theirs.

The claim to make is narrow and therefore airtight: not "no tool computed this"
but **"no tool could."** There is software that does cohort analysis on
channels. There is none that knows you employ two people and cannot afford
overtime.

Then the pair of cards. The left one concedes, genuinely, that every dashboard
metric was TRUE -- paid search really is the cheapest and really does bring the
most customers. You are not catching the tools in a lie. You are pointing out
they were answering a question you never asked. The right card is the verdict,
and it leaves two doors open: grow the channels that cost almost nothing to
serve (email has room for 64% growth against paid search's 12%), or attack the
33% return rate that makes paid search expensive in the first place. **Do not
pick one for them** -- the whole point is that the screen prices the options
and the owner chooses.

**The ceiling genuinely does bite now, so you may say so plainly.** At 93% there
are six spare hours in the whole week, and growing paid search 20% costs 83.6 --
overtime. That is real in the data; the verifier checks it. (An earlier 180-day
export put this at 74% with no squeeze at all, and the notes told you NOT to
claim a breach. That changed when the export was cut to 45 days on 2026-09-08.
If you ever regenerate the data, re-read `verify_deck_claims.py` output before
trusting either version of this paragraph.)

Tie back to slide 2's "what is not in it" card here, explicitly. That plant is
now twenty minutes old and closing it is satisfying.

Then the last line of the setup paragraph is your handoff to the reveal: "watch
what it does to the obvious answer." Say it, then advance.


## What got built

Open the real thing. Screen-share `dashboard.html` in the browser, not a
screenshot. **Do not say "I haven't seen this either"** -- you have, you ran it
beforehand, and the room already knows because you told them on slide 3. The
honest line is the better one: *everything here came out of that one paragraph.*

**This is the last slide before the close, and there is no teaching left after
it.** The room has already been told what the number is and why it matters --
slide 7 did that. This slide is confirmation: they see it on a real screen, in a
real browser, and it matches what you promised. That is a much stronger ending
than explaining something new.

Walk the four parts using the anatomy strip, in order. The strip on the slide is
the map; the browser is the territory. Go back and forth once so they can see
the mapping, then stay in the browser.

The order matters. Lead with the 93% and let the room register that 5.6 spare
hours is the whole margin, before you say which channel is spending it. Then the
channel table, then the hidden-cost section, then the growth room. If you name
paid search too early the rest of the screen is just confirmation.

**The live controls are the most important thing on the page, so save them for
last and actually use them.** The four boxes at the top -- minutes per return,
CS people, hours each, hourly wage -- are editable, and every figure below
re-reads. Change 40 to 35 on screen and let the room watch the numbers move.
That is the difference between a report and an instrument, demonstrated rather
than claimed, and it lands harder than any sentence you could say about it.
Change it back before you move on.

**Then answer the question the whole deck has been dodging: what happens when
the data changes?** This session sells a *standing* instrument, not one Monday's
finding, and until this moment the room has only ever seen one dataset produce
one verdict. So say plainly that none of the conclusions are written into the
page -- the villain channel, the one to grow, the whole narrative paragraph are
all computed from whatever file it is handed.

It is worth being able to say this with total confidence, because it was
actually tested (2026-09-08): feeding the same page a file where email had a
41% return rate and paid search 6% flipped the headline to **108% -- already
in overtime**, and rewrote the prose to *"email is eating 73% of your
customer-service team"*, recommending growth into paid search. Same file, same
code, opposite verdict. Nothing is hardcoded.

**If you want the strongest possible version of this beat, keep a second
`dashboard.html` built from an altered export and open it for fifteen seconds.**
Two tabs, opposite conclusions, no edits in between. That single comparison
proves "standing instrument" better than the rest of the session combined --
and it is the thing that makes the course's "always current" promise land as
obviously valuable rather than as a nice-to-have.

**This screen is bigger than "four things", and that is fine -- do not
apologise for it.** An earlier version of this slide defended the smallness of
the output; the real file has six sections and a control panel, so that defense
now reads as false modesty. What to say instead if someone looks overwhelmed:
every section answers one question an owner actually asks, and the top of the
page alone is enough for a Monday.

Do not tour the code. Nobody wants it and it re-triggers the fear the whole
session is draining.

**One honest snag, in case anyone is reading closely.** The page's own prose
says paid search is "eating 58% of your customer-service team". That is
46.4 hours against the 80-hour ceiling. The deck says 62%, which is the same
46.4 hours against the 74.4 hours of *return-handling load*. Both are correct
and they answer different questions. If nobody asks, say nothing. If someone
does, that one sentence is the answer, and it is a good look rather than a bad
one: you know your own numbers.

## What you own

**Lead with ownership, name the gap second, and stop there.** Do not explain how
the gap gets closed. Do not say "and in the course you'd connect a live source."
That converts a reason to enroll into a free tip, and slide 11 is ninety seconds
away and does that job properly.

**The order here changed on purpose, and it matters.** The listing sells this as
a feature they own -- "a dashboard you own and update by asking... it lives on
your computer, no subscription, no analyst." Somebody registered for that
sentence. If the first thing they hear is what it can't do, you have handed
their selling point back to them as a shortcoming. So: what they own first, said
warmly and meant, and the ceiling second.

The ownership half is genuinely strong, so sell it properly: no subscription, no
seat, nobody to ask, and it does not stop working if they cancel something. New
numbers, hand it the file, say refresh. **"Go and do it" is sincere** -- someone
who only ever does the free version should still be better off, and you should
mean that.

Then the ceiling, plainly and without embarrassment: you have to hand it the new
file. It is a real limit and the audience will respect you naming it before they
discover it. The last line on that card -- "that's the one thing standing between
this and a screen that's just always right" -- is doing the setup work, so read
it and then move on. Do not elaborate.

This is also the slide that protects the honesty of the whole session. The seam
between "a dashboard you refresh by asking" and "a dashboard that refreshes
itself" is the pitch. Blur it and you've given the class away; keep it sharp and
it sells itself.

## The real lesson

The spine. A teaching slide, not a pitch, and the pitch does not start here.

**Silence is the technique.** Three short paragraphs, big type, long pauses
between them. Do not fill the gaps. Read the last line, then stop talking for a
full two seconds before advancing.

The turn, and say it close to the slide wording because it is the thesis: **we
built a screen that watches every channel and every hour the team has, and
tells us each week where the business is actually being decided.** It is not a
report on last quarter and it is not a chart dump. It is an instrument you run
against.

Then the skill, stated as a method they can repeat: know what you are really
running against, and build the one view that keeps it in front of you. That is
what you did on slide 3, and it is why the prompt contained your headcount
instead of a chart type.

The line to land, in your own words: once you can do that, you stop taking
whatever screen you're given. That's the durable takeaway and it's true whether
or not anyone buys anything.

## What's next

Sets up the ask without making it. **Don't do the pitch twice** — the offer is
one slide away and doing it here spends it early and makes the offer slide feel
like repetition.

Read two rows across the table, not all six. The dashboard row is the obvious
one: "the dashboard class isn't about dashboards, it's about getting at your own
data." That phrasing is deliberately NOT printed on the slide, so it lands as
something you said rather than something they read. Pick one other and read it
the same way. That's enough for the shape to
register: every class builds one real thing and the point is always the skill
underneath it. They just lived a short version of exactly that.

The card on the right is where today's ceiling gets closed, and this is the only
place it should be closed: real numbers flowing in on their own, always current,
private URL with a password. **The refresh disappears.** That's the sentence.

Both doors are real. The YouTube version is the same material, not a teaser, and
saying so is what makes the paid ask land thirty seconds later. Routing someone
to the free version who would have been unhappy paying is a good outcome.

## The offer

**Two minutes, and this is the only hard sell in the session. Earn it by being
specific and then stop talking.**

Specifics only: the date, what's included, the code, the price. Ten founding
seats is ten seats — state it flatly. No countdown theater, no "these are going
fast." This audience detects that instantly and it would undo the trust the
session just built.

The strongest thing you can say is also the least salesy: they just watched the
smallest possible version of this and it worked.

Leave the QR up while you talk. Maven emails every registrant the recording
within a couple of days, so you can close soft without losing anybody. Do not
extend this slide to fill silence.

## Questions

Five minutes. Chat questions with emoji upvoting, most-upvoted first.

Land the homework card before you take the first question, and keep it small.
The middle step is the one that matters and the one nobody would think of on
their own: **write down the limit you are actually working against** -- people,
hours, cash, space. Everyone can do step one. Step two is the whole lesson, and
step three is just asking for it. Three steps, all doable this week, none
requiring anything they don't have.

Likely questions and short answers:

- **"Can I do this with my Stripe/Shopify/QuickBooks export?"** Yes, that's
  exactly the point. Any export with a date and some counts. What makes it
  yours isn't the export, it's the constraint you tell it about.
- **"What if my file is messy?"** Better. Say so. Messy is the normal case and
  Claude handles it; describe the mess rather than cleaning it first.
- **"How long does that take to build?"** About fifteen minutes for this one,
  and it varies. Say it plainly -- you already disclosed it on slide 3. Worth
  adding: you don't sit and watch it, you go and do something else, which is
  also why it wasn't worth doing live in front of them.
- **"Did you edit it afterwards?"** No. What they are looking at is what came
  back. If you ever DO tweak the file before a session, change this answer --
  do not let a rehearsed edit pass as a first pass.
- **"Does it update by itself?"** No, and that's slide 9. Fresh file, ask, it
  updates. The course makes the refresh disappear. Don't go further than that.
- **"Doesn't Triple Whale / Northbeam already do this?"** Worth being straight:
  they do the cohort half, and they cost more than this course and need to have
  been watching for 90 days. They do not do the capacity half, because they
  cannot know your headcount or your overtime problem. That's the honest line
  and it lands better than pretending the category doesn't exist.
- **"Where did the 40 minutes come from?"** The owner. That's the point. It's an
  estimate, and a rough estimate is enough here: the finding is a *ratio*
  between channels, so being off by five minutes moves both sides at once and
  paid search stays ~5x email either way.
- **"Do I need to be technical?"** No. Point back at slide 3: that prompt is a
  paragraph of plain English, and it's the whole skill.
- **"Which Claude plan?"** The desktop app on a paid plan, Code tab.
- **"Can I share the dashboard with my team?"** Not usefully as a local file,
  and that's the deploy-and-password material in the course. One sentence.
- **"Why not just use a spreadsheet?"** Fair, and if a spreadsheet already works
  for them they should keep it. The difference is you describe what you want
  once instead of maintaining formulas forever.

If it goes quiet, answer one of the likely questions above as though someone
had asked it -- "one that comes up every time is..." -- rather than waiting.
This room has been silent for forty minutes and will not suddenly start
talking; carrying it yourself is the plan, not the fallback.

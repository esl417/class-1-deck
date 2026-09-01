# Teaching notes — Lightning Lesson (Build a Dashboard That Thinks Like You)

Per-slide notes. `##` = slide label. Private.

**The shape of this session, and the thing to keep straight:** this is
**lecture and demonstration**. Nobody in the room builds along, and you should
never imply they should. The teaching is the spine; the demo is the proof.
The build kicks off on slide 4 (around minute 12) and runs underneath slides 5
and 6, which is roughly ten minutes of cover. You come back to it on slide 7.
Nothing in the teaching depends on the build finishing at a particular moment.

**Why nobody builds along:** the previous lightning lesson had attendees install
and run something themselves, and it worked because the run was fire-and-forget
on their machine. A dashboard build is conversational and every attendee's
session would diverge within ninety seconds. Watching one build done properly
teaches more than a hundred half-finished ones. Say this out loud once, on slide
2, so nobody feels left out: they're watching, every prompt is on a slide, and
they can do it with their own file afterwards.

**Audience:** non-technical small business owners who have been made to feel
stupid by developer tools before. Some are on Claude for the first time this
week. The governing test for everything you say: does this make them feel calmer
and more capable, or further behind?

**Data is sample data, always.** A made-up business. Say so on slide 2 and don't
be cagey about it. Nothing on screen is anyone's real numbers, including yours.

**Three things to say out loud that aren't on any slide:**
- As the build starts: "I'm not going to sit here watching a progress bar with
  you." That single line is what buys you slides 5 and 6.
- On slide 7, before you open it: you have not seen this output either. That is
  true and it is the most interesting thing about the demo.
- Invite chat questions early (slide 2 or 3) so Q&A has a backlog by the time
  you reach it.

**Timing skeleton (45 min):** 1 / 3 / 5 · 3 / 5 / 5 · 5 / 5 · 2 / 2 / 3 / 2 / 5.
Build starts end of slide 4. The only beat that reliably overruns is slide 6.

**The failure case, and the fallback:** if the build errors or produces something
unusable, do not debug live. Have a finished `dashboard.html` already on disk and
open that instead, saying plainly that you're opening one you made earlier. The
lesson is the thinking, not the demo's luck. Budget zero minutes for debugging.

---

## Where we start

Three jobs, in order: set up the file, set expectations about watching, and
plant the thing that pays off on slide 8.

The plant is the "what is NOT in it" card. Say it slowly and then move on
without explaining it. Twenty minutes later that card is the reveal. Do not
name the metric here; naming it now spends the payoff early.

Say the watching-not-building thing warmly and once. This audience is braced to
be told they're behind, and "you don't have to keep up today" is a relief, not a
disappointment. The heads-up box does the work: every prompt is on a slide.

If someone asks for the sample file in chat, say it's in the follow-up. Don't
break stride hunting for a link.

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
exported a report and immediately started dividing one column by another. Ask
for a show of hands if the room is warm. Almost everyone has done it.

Do NOT get into a specific tool's flaws. The moment you say "Google Analytics
is bad" you've lost the people who like it and taught nothing.

## Start the build

**This slide starts the clock. Type the prompt live, on screen, at real speed.**
Do not paste it silently. The typing IS the teaching — they need to see it's a
plain English paragraph, not a command.

Read it aloud as you type, then stop and make three points off the two cards:

1. You did not name the metric.
2. You did not name the columns.
3. You did not describe a layout.

Then the card on the right: you asked for a **decision**, not a chart. "Tell me
whether this is healthy and what to do about it." That's the whole method in one
sentence and it's why the prompt is worded the way it is.

Then hit go, and say the fire-and-forget line: it takes a few minutes, we are
not waiting on it, the next two slides are the reason the prompt was worded that
way. Be explicit that you'll come back to it. A room that doesn't know a payoff
is coming will spend slides 5 and 6 wondering what happened to the build.

If it finishes during slide 5 or 6, **do not interrupt to show it.** Let it sit.
The reveal is better whole, on slide 7, than dribbled out early.

## Decision tool

The idea the whole session exists to teach, borrowed from Class 2 where it's the
highest-value beat. Slow down. This is a judgment lesson, not a software lesson.

The contrast cards do the work: a report states facts, a decision tool attaches a
verdict. Read the right-hand column out loud in order and let the last line land
on its own. "You're paying a full kitchen for a quiet room, close Tuesdays or
fill them" is a sentence an owner can act on. "You served 240 covers" is not.

**The example here is a restaurant on purpose, and it is NOT the demo's data.**
Keep it that way. The numbers on the screen you open on slide 7 must be the first
time the room sees the demo's figures, or slide 8's reveal lands as a repeat and
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

## Your turn

**You are not lecturing here. You are running the room.** The slide is a
backdrop. This is the only engagement beat in a lecture-format session, so it
carries all the interaction weight that the previous lesson spread across three
moments. Protect it.

Shape, in order:

1. Ask the question once, and be precise that it's a *decision*, not a number.
   A decision is much easier to answer, which is exactly why it's worded that
   way. Everyone has a Monday decision. Not everyone has a metric.
2. Wait. Genuinely wait. The first ten seconds of silence feel long and are
   normal; people are typing. Don't rescue it by talking.
3. Read them out as they come, by name, and cluster out loud: "a lot of you are
   deciding where to spend." That moment is the point of the beat.
4. Take three and work them, briefly: for that decision, what would have to be
   on the screen? That's the backwards-build made concrete with the room's own
   material, and it's teaching you could not have scripted.

**Five minutes, hard cap.** This expands to fill whatever you give it. If the
build is still running you can afford a fourth answer, and that reads as
generosity rather than stalling. If the build is done, still finish the beat
properly. Don't cut the room off to get to the screen.

The card on the right is the takeaway to land before moving on: the decision
comes first, the dashboard is built backwards from it. Start from the data you
happen to have and you get a chart dump.

## What got built

Open the real thing. Screen-share the actual file in the browser, not a
screenshot. Say out loud that you haven't seen it either.

Then walk the four parts using the anatomy strip, in order, top to bottom. The
strip on the slide is the map; the browser is the territory. Go back and forth
once so they can see the mapping, then stay in the browser.

**Defend the smallness explicitly.** Four things is a choice, not a limitation,
and someone in the room is thinking "that's it?" Get ahead of it: a screen you
can read in three seconds is a screen you'll open on a Monday. Everything left
off was deliberate and any of it can be added later by asking. This also happens
to be why the build was quick, but lead with the design reason, not the speed.

Do not tour the code. Nobody wants it and it re-triggers the fear the whole
session is draining.

If the output is ugly, say so cheerfully and move on. First passes are rough,
that's expected, and the number is right even when the styling isn't. Do not
apologize for it and do not start fixing it live.

## The number

The payoff, and the promise from the listing copy made literal: the number you
run on is in none of your reports.

Point at the diagram in this order, physically: the two grey raw counts, then the
arrow, then the big teal one. Both grey numbers were columns in the file. The
teal one was not. Nobody exported it because no tool knew it mattered.

Then the pair of cards, which is the transferable distinction: a raw count says
what happened, a computed number says whether it's good and whether it's
improving. That is the line between reporting and deciding.

**The small-note is the thing they can actually take home,** so say it as a
recipe: ask Claude to propose the numbers worth building out of your raw ones,
each with a line saying what decision it drives, then you pick. It generates,
you choose. Same shape as the metric-selection branch on slide 5, and worth
naming as the same move so it registers as a pattern rather than two tips.

Tie back to slide 2's "what is not in it" card here, explicitly. That plant is
now twenty minutes old and closing it is satisfying.

## The limits

**Name the gap and stop there.** Do not explain how it gets closed. Do not say
"and in the course you'd connect a live source." That converts a reason to
enroll into a free tip, and slide 11 is ninety seconds away and does that job
properly.

The honest limit is in the headline, so let it do the work: it shows the day you
built it. Nothing in the file reaches out for new numbers. Feed it a fresh export
and ask, and it updates; leave it alone and it sits there.

Say this plainly and without embarrassment. It is a real limitation and the
audience will respect you naming it before they discover it. **Do not oversell
the limitation and do not undersell what they got** — the left-hand card is
genuinely useful and "go and do it" is sincere. Someone who only ever does the
free version should still be better off, and you should mean that.

This is also the slide that protects the honesty of the whole session. The seam
between "a dashboard you refresh by asking" and "a dashboard that refreshes
itself" is the pitch. Blur it and you've given the class away; keep it sharp and
it sells itself.

## The real lesson

The spine. A teaching slide, not a pitch, and the pitch does not start here.

**Silence is the technique.** Three short paragraphs, big type, long pauses
between them. Do not fill the gaps. Read the last line, then stop talking for a
full two seconds before advancing.

The turn: it was never about dashboards. What they watched was a number getting
built that no software would have handed over, because it only exists once
somebody decides it matters. That's the skill, and it transfers to anything they
measure.

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

Land the homework card before you take the first question, and keep it small:
export one file, ask for the one number, ask what decision it should change.
Three steps, all doable this week, none requiring anything they don't have.

Likely questions and short answers:

- **"Can I do this with my Stripe/Shopify/QuickBooks export?"** Yes, that's
  exactly the point. Any export with a date and some counts.
- **"What if my file is messy?"** Better. Say so. Messy is the normal case and
  Claude handles it; describe the mess rather than cleaning it first.
- **"Does it update by itself?"** No, and that's slide 9. Fresh file, ask, it
  updates. The course makes the refresh disappear. Don't go further than that.
- **"Do I need to be technical?"** No. Point back at slide 4: that prompt is a
  paragraph of plain English, and it's the whole skill.
- **"Which Claude plan?"** The desktop app on a paid plan, Code tab.
- **"Can I share the dashboard with my team?"** Not usefully as a local file,
  and that's the deploy-and-password material in the course. One sentence.
- **"Why not just use a spreadsheet?"** Fair, and if a spreadsheet already works
  for them they should keep it. The difference is you describe what you want
  once instead of maintaining formulas forever.

If it goes quiet, go back to the chat beat from slide 6 and answer one you
didn't get to. You will have more than you had time for.

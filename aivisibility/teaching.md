# Teaching notes — Lightning Lesson (Audit Your Website's AI Visibility)

Per-slide notes. `##` = slide label. Private.

**The shape of this session, and the thing to keep straight:** the teaching is the
spine, the audit is the proof and the sale. The `/seo geo` run starts around minute
12 and executes underneath everything in Section 2. It is NOT the centerpiece and
nothing waits on it. If it finishes early, great, jump to the results. If it's still
going at the end, the session still works and the report is waiting for them after.

**Audience:** non-technical small business owners who have been made to feel stupid
by developer tools before. Some are on Claude for the first time this week. The
governing test for everything you say: does this make them feel calmer and more
capable, or further behind?

**Two things to say out loud that aren't on any slide:**
- The report output carries a promo footer for the plugin author's Skool community.
  Pre-empt it once when results land: "the person who built this has a free
  community, that's his ask, not mine." Three seconds, prevents it reading as a
  bait-and-switch.
- Invite questions into the Zoom chat early (slide 6) so the Q&A has a backlog by
  the time you get there. Maven's format is chat questions with emoji upvoting.

---

## What you need

Open under a minute, per Maven's guidance. The entire job of this slide is draining
fear before anything happens. Say the list out loud and then say what's NOT on it —
the "what you do not need" card is the one that lands. Most of this audience has been
burned by a tutorial that said "just install X" and cost them an afternoon.

If someone types in chat that they don't have the app: point at the heads-up box, tell
them to grab it now, and move on without dwelling. Do not slow the room for stragglers;
the rescue is that nothing today depends on being ahead, and the recording covers them.

## Mentality

The load-bearing frame for the whole session, and the reason none of this needs them
to be technical. Teach it as a HABIT, not a concept: you don't look up the word, you
ask what it means. You don't decode the report, you ask which three things matter.

Do not rush this slide even though it looks simple. Everything downstream depends on
them believing it. The payoff is explicit and lands twenty minutes later on the results
slide, where they'll get a report full of vocabulary they don't know. Point forward to
that: "in about twenty minutes this is going to matter."

If a student says "I already use ChatGPT" — good, they have the habit half-formed. The
delta today is that they're about to give the AI a capability, not just a prompt.

## Which tab

The most likely silent failure in the entire session is someone doing the install in
the wrong tab. Say "Code tab" out loud, twice, and make sure your shared screen shows
the tab bar with Code selected.

The Cowork question WILL come up, either here or in Q&A, because Cowork is described
as being for business roles and research and this audit is obviously business research.
The honest answer, in this order:

1. Cowork works on Anthropic's computers and reaches into your files from outside.
   Code works directly on yours.
2. Today's toolkit includes a piece that has to run on your machine, so Cowork won't
   take it. (Verified empirically: the marketplace sync fails in Cowork.)
3. The useful rule of thumb: **Cowork for work you hand off. Code for capability you
   install.**

Do NOT get deeper than that. If someone presses, the real reason is that this plugin
registers a hook — code that fires automatically in the background — and Cowork
doesn't support those yet. That's a correct answer for one curious person, not
something to teach thirty.

The "don't let the name put you off" line is not a throwaway. A meaningful fraction
of this audience will hesitate to click a tab called Code. Say it warmly.

## What we're adding

This is the conceptual heart of the session and the thing that transfers. A skill is
not software; it's a professional handbook handed to a capable assistant who hasn't
worked in that field. That analogy does a lot of work — use it.

The GitHub explanation exists for one reason: the red warning is thirty seconds away
and they need context for it before it appears. Don't over-explain GitHub. "Like Google
Drive, but shared publicly" is enough, and it's doing double duty: it makes GitHub
familiar instead of intimidating, AND it plants the idea that anyone can read what's in
there, which is the exact reframe the red warning needs sixty seconds later.

## Add it

The riskiest ninety seconds of the session. Go slowly, and narrate your own clicks on
screen while they follow. Every step has its screenshot on the slide, so they can look
up at the projection and down at their own screen and match them.

1. The **+** in the chat box → **Plugins** → **Manage plugins**. This is the step people
   miss, because nothing about a plus sign suggests plugins live behind it. Point at it.
2. **Add** (top right) → **Add marketplace** → **Add from a repository**. Say "top right"
   out loud; the button is small and easy to miss on a laptop.
3. Paste and **Sync**.

The exact string is `AgriciDaniel/claude-seo` — note the capitalization, lowercase `i`
then capital `D`. If someone's sync fails, that's the first thing to check.

**The red warning:** get ahead of it. It's visible in the screenshot on this slide, so
say it before they read it. Two facts, in this order, and don't dress them up:
Anthropic didn't write this and can't vouch for it, which is why the warning exists and
why it's correct. And it's open source, so the code is public and checkable by anyone.

Do NOT frame the warning as a "price" or a "tradeoff." It isn't one, and the audience
will feel the sleight of hand. The reassurance is narrower and more honest: unverified
by Anthropic is not the same as unknowable.

The GitHub analogy from two slides ago is what makes that land, which is why it's
planted early: they already know it's the public-Drive-folder thing where anyone can
open it and read what's inside.

If someone still isn't comfortable, that's a legitimate position and you should say so.
They can watch you do it and run it after class. Do not pressure anyone through this
step.

**Step 4 is the one people don't expect.** After Sync, a **Claude seo** card appears,
and it has to be clicked, then install clicked inside it. People will assume Sync alone
did the job and sit there waiting for something to happen. Say it plainly. No restart
is needed either, because people will hover expecting one.

Then land the payoff out loud, since it isn't on the slide: Claude can do something now
that it couldn't do sixty seconds ago, and it persists. That's the whole point of the
session in one sentence, and it's worth two seconds of silence before the run.

## Run it

The run starts here, around minute 12. Three things to say clearly:

- Swap in their OWN domain. Say it twice; someone will type the example verbatim.
- It takes a few minutes. Start it and leave it alone.
- We are not waiting for it. Put questions in the chat while it works.

That last one is what buys you the whole teaching section without anyone feeling
stalled. Be explicit that nothing depends on their run finishing at a particular time.

If someone's run errors: have them ask Claude what went wrong, in the same window.
That's the Mentality slide paying off immediately and it's a better answer than
anything you could debug live.

**Say the pivot out loud as the run starts, because it's no longer on a slide.** Most
people's entire relationship with AI is a text box; they just went and found a
capability, handed it over, and pointed it at their own business. Remember that move,
because it isn't about websites. That's the seed of the close, so plant it lightly here
and let it pay off on the spine slide. Do NOT claim almost nobody has done this: it's
unprovable and this audience has good instincts for overselling.

## SEO + GEO

Teach it as one chain with two links, and let the structure do the correcting. The
slide deliberately does NOT open by arguing with "search is dead" — leading with the
myth makes people remember the myth. Describe how it actually works and the wrong idea
has nowhere to stand.

Hold the correction in reserve for the room. If someone says "I heard I can ignore
Google now," THEN say it plainly: showing up in ordinary search is the price of
admission to being in the AI's source pool. That's a live answer to a real question,
not a preemptive strike against something half of them never believed.

GEO and AEO are the same thing under different names. Say so once so nobody spends the
session wondering if they missed a distinction.

## The chain

Four steps, and the whole point is step three: most businesses break it without ever
knowing. That's what today's report measures, so this slide is the setup for reading
their results later.

Keep it fast. It's a visual, not a lecture.

## The foundation

An entire profession compressed honestly. The framing that makes it land: strip the
jargon and search is just trust.

Two levers only. Don't add a third even if asked — send them to the course instead.

The one hard rule worth emphasizing: write it yourself. Draft with AI, but the ideas
and voice must be theirs; thin AI-spun pages get caught and actively hurt them. This
audience is exactly the group most tempted to mass-generate pages, so say it plainly.

## What you control

The honesty slide, and the one that buys credibility for everything after it. Half of
what their report names will not be fixable on their website at all.

Real examples from the sample report, if you want them: Wikipedia presence, Reddit
mentions, reviews, listings. The hotel in the example scored 30 on ChatGPT and 28 on
Perplexity almost entirely for reasons that have nothing to do with their website.

The heads-up is the important part: this is why "just rebuild the website" is usually
the wrong answer, and saying so costs you a sale you didn't deserve. That's the move
that makes the genuinely constrained trust your recommendation later.

## Be the answer

The philosophical turn, and it's short on purpose. Twenty years of chasing a position
in a list of blue links is over; now something reads the web and answers in a sentence,
and you're in it or you're not.

The heads-up sets up the problem/solution pair that follows. Land it as a question they
haven't asked themselves: their site was built for a person with eyes and patience, and
that's not what's reading it now. Don't answer it here. The next slide does.

## The problem

Explicitly framed as PROBLEM, paired with the next slide as SOLUTION. This is the "why
does AI cite some sites and not others" answer, and it's the one that makes the dual web
idea feel necessary rather than clever.

The key insight to deliver clearly: it has almost nothing to do with how good their
business is.

**Make the right-hand card physical.** Everything beautiful on their site — the hero
video, the booking widget, the menus — is built out of code, and that code is what an
AI opens. Thousands of lines of it, and their actual words are buried somewhere inside.
If you want the demo, right-click any page and choose View Page Source: that wall of
markup is what's being read, and the sentences a customer sees are a tiny fraction of
it. Deliver it as a fact about how the web is built, never as a criticism of their site.

Then the second half, which is the part people miss: even after it digs the words out,
there usually isn't much there. Marketing copy is short, spread across pages, and
written to sound good rather than to answer a question. Expensive to reach, thin when
you arrive.

The line that lands: the businesses getting quoted aren't better, they're cheaper to
read. Let that sit for a beat.

## The solution

The payoff. Something sits in front of the site and reads who's asking. Humans and
Google go straight through, untouched. AI gets a clean readable version at the same
address. Name it out loud as **the dual web**, and use that name for the rest of the
session; it's the term the course uses. Customers never see it.

Keep it at the concept level. This is NOT an implementation course and you are not
teaching them to build it today. If someone asks how, that's the course — say so
warmly and move on.

The warning at the bottom is doing real work: there's a right and wrong way, and doing
it carelessly gets you penalized by Google. That's honest, it's why so few businesses
have done it, and it's the credibility behind the advantage claim two slides later.
Don't explain the mechanism (canonicals, cloaking rules). The existence of a real
danger is the point; the details are the curriculum.

## Your results

**You are not lecturing here. You are running the room.** The slide is a backdrop, not
content. Do not read it aloud and do not walk through an example report on your screen.

**Nobody chats with Claude during this beat.** They read, they post one thing to the
chat, and you teach off what comes back. With twenty people, sending everyone into their
own private Claude conversation is twenty separate experiences, no shared attention, and
nothing for you to do. The chat is what makes this work at this room size: they read
privately, they post publicly, one person's finding becomes everyone's lesson. The
talking-to-Claude part is real and valuable, but it's homework, and the slide now says so.

Five minutes, hard cap. The shape:

1. Give the instruction once: top of the report, find the overall score, find your
   lowest category. That's it — no reading comprehension required yet.
2. **"Put your lowest category in the chat."** One or two words from each person. Low
   effort, and now you have twenty data points on screen.
3. Read the chat back and cluster it out loud: "okay, a lot of you are low on X." That
   moment is the point of the whole beat — twenty people stop feeling alone with a bad
   number, and it's teaching you could not have scripted in advance.
4. Take two or three specific ones live, by name, and answer them for the room.

Answer individuals by name. Someone's specific finding, answered live, is worth more
than any general point you could make, and it's the thing they'll tell other people
about afterward.

Expect and handle these:

- **"Mine says something I don't understand."** Expected, and say so — nobody
  understands every line. That's exactly what the after-class conversation is for.
- **"Mine scored badly."** Reframe immediately: a low score is a to-do list, and it's
  measuring readiness, not the quality of their business.
- **"Mine isn't done yet."** Fine, it'll be waiting for them. Nothing after this depends
  on having it.
- **A finding about something off their website** (reviews, listings, no Wikipedia):
  that's the "on your site vs around your site" split from earlier appearing in their
  own results. Name it when it comes up rather than teaching it again.

Land the homework before you click on, and land it broad — not as a task list. Go back
to it on your own time, ask it anything, it will explain any of this in plain English.
The one steer worth giving them: ask what they can actually fix on their own site.
That's slide 11 doing its job — it keeps them off the off-site stuff they can't move and
pointed at the half they control.

Say the promo-footer line here: the person who built this has a free community, that's
his ask, not mine.

Watch the clock. This can expand to fill whatever you give it, and the close still
needs its time.

## The ceiling

The honest limit, and the handcuffs. It can tell them whether they CAN be quoted, not
whether they ARE. That needs live data plugged in behind it.

**Don't tell them their report says this.** The sample report spelled the limitation out
because that run was deliberately made without any data integrations; a given student's
report may word it differently or not name it at all. The claim on this slide is about
what the tool can reach without live data, which IS true for everyone in the room, since
nobody has a data source connected. Keep it there and it holds for every case.

Do not oversell this as a limitation, and do not undersell what they got. What they
have for free is genuinely useful and they should go do it. What they don't have is
market context: actual citations, rankings, competitors.

**Name the gap and stop there.** Do not explain how it gets closed, and do not tell them
that connecting a data source is the same move they already made. That's the course, and
handing it over here converts a reason to enroll into a free tip. Let the ceiling sit as
a real ceiling; the close is where the door gets pointed at.

If someone asks in Q&A how you'd get the missing data, that's a genuine question and you
answer it honestly: it takes connecting a live data source, and that's what the course
covers, and it's open now. Don't pitch it here; the offer slide is two minutes away.

## The real lesson

The spine of the whole session. Slow down and mean it. Big type, three short paragraphs,
long pauses between them. Silence is the technique on this slide.

**The one thing they should walk out believing:** you can install an expert. Today it
was an SEO expert, added in four clicks, and it went and examined their real business.
That's a concrete thing that happened forty minutes ago, not an abstraction, which is
exactly why it's the takeaway.

Then the turn: the SEO was never the point. The skill is knowing that when somebody has
written down how to do a job properly, you can hand that to Claude and put it to work.

**Be careful what you promise here, and this is checked.** The official plugin
marketplace today is overwhelmingly developer tools and vendor integrations (Stripe,
Intercom, Salesforce). There is NOT a ready-made bookkeeping or hiring or contracts
plugin waiting for a small business owner. Do not list those as if they're sitting there
to be installed; anyone who goes looking will find nothing and the whole close curdles.

What IS true and safe to say: the mechanism is general. New skills appear constantly,
anyone can write one, and the four-click move they just learned is how any of them gets
added. If someone asks what else is available, be honest that the good ones today skew
technical and marketing, and that this is early.

## What's next

QR slide is gone; this is a links slide now, because everyone gets a copy of the deck
and links survive where a scanned code doesn't. Leave it up through the Q&A.

**Lead with the promise, not the slide.** The headline is the course's promise: you run
your whole business this way. Keep the razor in mind on anything you improvise here —
THEY are the subject of the verb and AI is the instrument. Never "AI runs it for you"
(that's the agent-course pitch) and never builder or engineer language.

**Then say the trojan horse out loud. It's the reason the classes are built this way.**
Every class builds one real thing, and the point is always the skill underneath it. They
just lived a short version: they came for a website audit and left knowing how to install
an expert. The table shows that, so read a couple of rows across rather than listing all
six.

The rows worth saying out loud: the dashboard class isn't about dashboards, it's about
getting at your own data. The automation class isn't about a morning briefing, it's
about work happening without you. Same shape as today.

**The course is live and enrolling, so this slide sets up the ask rather than making it.**
Name the two doors, keep it short, and move to the offer slide, which is where the actual
sell happens. Don't do the pitch twice.

Both doors are genuinely real, and say so. The free YouTube version is the same material,
not a teaser. Routing someone there who'd be unhappy paying is a good outcome, and that
honesty is what makes the paid ask land thirty seconds later.

Maven emails every registrant the recording 48 hours after the lesson with a link to the
course, so anyone who drops off still gets a second touch. That means you can close soft
here without losing them.

## The offer

**Two minutes, and this is the only hard sell in the session. Earn it by being specific
and then stop talking.**

The facts, all verified against the live course page:

- **Run Your Whole Business with AI**, six weeks, Sept 29 to Nov 3
- 11 live sessions, 6 lessons, 6 projects
- 2 to 4 hours a week live, plus project time
- $1,795, and **FOUNDING400 takes it to $1,395**
- **10 founding seats at that price**
- Lifetime access to recordings, 3 months of StratEngine AI Professional, Maven guarantee

**The scarcity is real, so state it flatly and do not dress it up.** Ten seats is ten
seats. No countdown theater, no "spots are going fast." This audience detects that
instantly and it would undo the trust the whole session just built.

The "your competitors are not doing this yet" callout is a technical advantage, not
scarcity — it moved here from a cut slide. Their competitors aren't doing it because
almost nobody teaches it and the penalty for getting it wrong is real. Say the last line
honestly: that gap is temporary. No urgency theater, no fake deadline, same as above.

Leave the QR up through the Q&A. People scan during questions, not during the pitch.

Say the September 29 date out loud. Attendees hearing this on Aug 25 have about five
weeks, and some will assume a launch that far out means they can decide later.

The strongest thing you can say here is the least salesy: they just did the smallest
version of this and it worked. The course is the same move applied to the whole business.

## Questions

Five minutes. Chat questions with emoji upvoting; take the most-upvoted first.

Likely questions and short answers:

- **"Why Code and not Cowork?"** See the Which tab notes. Short version: Cowork works
  on Anthropic's computers, Code works on yours, this toolkit needs yours.
- **"Is this safe? What was that red warning?"** The warning was accurate: Anthropic
  didn't write it and can't vouch for it. It's open source, so the code is public and
  checkable. That warning appears for anything not made by Anthropic, which is most of
  what you'd ever want to add.
- **"My run failed / is still going."** Ask Claude in the same window what happened.
  It'll be waiting for them regardless.
- **"Do I need to know what schema is?"** No. Ask Claude to explain it when you hit it.
- **"Can it fix the things it found?"** Yes, and that's the natural next step. Ask it
  to work through the list with them, highest impact first.

The "tonight, if you do nothing else" card is the real close. Three actions, all small,
all doable the same evening. The re-run in a month is the retention loop.

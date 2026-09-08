# Teaching notes — Lightning Lesson (Audit Your Website's AI Visibility)

Per-slide notes, keyed by slide label (`##` = the slide's `data-label`). These are
written for the person reading this deck AFTER the session, with Claude, trying to
reproduce on their own website what they watched Eric do.

**This session was a demonstration. Nobody built along.** Eric installed the plugin,
ran the audit, and read the report on his own screen, on one website. So a reader
arriving here has almost certainly NOT done any of it yet. Never speak as though they
already installed something or already have a report. They watched; now they want to
do it.

**What they are trying to reproduce, end to end:**

1. Open the Claude desktop app and go to the **Code** tab (not Chat, not Cowork).
2. Install the `AgriciDaniel/claude-seo` plugin through the Plugins UI.
3. Run one command, `/seo geo theirdomain.com`, and wait a few minutes.
4. Read the report: overall score, weakest category, what would move it.
5. Ask Claude to help them actually fix what it found.

If someone lands here without a specific question, that sequence is the answer. Walk
them through it from wherever they actually are.

**Who they are:** non-technical small business owners, many of whom have been made to
feel stupid by developer tools before. Some are new to Claude this week. The governing
test for every answer: does this leave them calmer and more capable, or further behind?
Ask what they're seeing on screen before diagnosing, and never assume terminal skills.

**Two things worth knowing that the slides do not say:**

- The report output carries a promo footer for the plugin author's Skool community.
  It is the author's ask, not Eric's, and it is not a catch. Say so plainly if the
  student asks about it.
- A low score is a to-do list, not a verdict on their business. Most of this audience
  reads a bad number as a personal failure. Reframe it every time it comes up.

---

## What you need

The only genuine prerequisite is the **Claude desktop app, signed in, on a paid plan**.
No terminal, no code editor, no GitHub account, no website login, no credit card.

If a student is unsure whether they qualify: they need a paid Claude plan, because the
Code tab and plugins are not on the free tier. That is the one thing that will stop
them cold, so check it first if nothing is working.

Nothing about this requires technical background. If they are hesitating because it
sounds like developer territory, that hesitation is the main obstacle, not any actual
difficulty. The whole install is four clicks and the run is one line.

## Mentality

The habit that makes all of this work: **ask, do not look up.** They do not need to
decode the report themselves. They can ask what a word means, ask which three things
matter most, ask it to write the email to their web person.

This matters most when the report lands full of unfamiliar vocabulary. Schema,
canonical, crawlability. The correct move is never to go research the term; it is to
ask Claude what it means for their site specifically.

If a student says they already use ChatGPT: good, the habit is half-formed. The new
part is handing the AI a capability it did not have, rather than just a prompt.

## Which tab

**The single most likely silent failure. The install must happen in the Code tab.**

If a student says the marketplace sync failed or the plugin will not install, check
the tab before anything else. This is the first thing to rule out.

- **Chat** — the familiar one. Cannot install plugins.
- **Cowork** — runs on Anthropic's computers and reaches into files from outside.
  **The marketplace sync fails here** (verified). The underlying reason: this plugin
  registers a hook, code that fires automatically in the background, and Cowork does
  not support those yet.
- **Code** — runs on the student's own machine. The only tab where capability gets
  installed.

The rule of thumb worth giving them: **Cowork for work you hand off. Code for
capability you install.**

The name puts people off. It should not. Nobody writes a line of code here; it is
called Code because it can act on their machine, which is exactly what the audit needs.

## What we're adding

A **skill** is not software they run. It is a professional handbook handed to a very
capable assistant who has not worked in that field yet. Somebody who does this work for
a living wrote down how they do it and published it.

The claude-seo plugin bundles roughly 25 of these, covering finding and fixing AI
visibility.

It lives on **GitHub**, which is worth explaining only as much as this: like Google
Drive, but shared publicly, where anyone can open it and read exactly what is inside.
That matters because it is why the plugin costs nothing, and it is why the red warning
during install is not a reason to panic.

This is the move that separates chatting with AI from operating it.

## Add it

**The four steps, and this is the part students most often get stuck in.**

1. In the chat box, click the **+**, then **Plugins → Manage plugins**. People miss
   this because nothing about a plus sign suggests plugins live behind it.
2. Top right, click **Add → Add marketplace**, then **Add from a repository**. The
   button is small and easy to miss on a laptop.
3. Paste `AgriciDaniel/claude-seo` into the **URL** box and press **Sync**.
4. A **Claude seo** card appears. **Click the card, then click install inside it.**

**Failure 1: the capitalization.** The string is `AgriciDaniel/claude-seo` — lowercase
`i`, then capital `D`. This is the most common reason a sync fails. Check it first.

**Failure 2: stopping after Sync.** Step 4 is the one people do not expect. Sync alone
does not install anything; it only adds the marketplace. The card has to be clicked and
then install clicked inside it. Students routinely sit waiting for something to happen
after Sync. No restart is needed either, though people expect one.

**Failure 3: wrong tab.** See the Which tab notes. If sync fails outright, this is the
other likely cause.

**The red warning is expected and correct.** Anthropic did not write this plugin and
cannot vouch for it, which is exactly what the warning says. It is open source, so the
code is public and checkable by anyone. That warning appears for anything not made by
Anthropic, which is most of what anyone would ever want to add.

Do not frame that as a price or a tradeoff. It is not one. The honest framing is
narrower: unverified by Anthropic is not the same as unknowable.

If a student is genuinely uncomfortable installing it, that is a legitimate position and
worth respecting rather than talking them out of.

**What just happened, and it is the point of the whole session:** Claude can do
something now that it could not do sixty seconds ago, and it persists.

## Run it

One line, with their own domain in place of the example:

```
/seo geo theirdomain.com
```

**It takes several minutes.** Start it and leave it alone. Do not interrupt it, do not
ask it questions in the same window while it works, do not close the app.

If the run errors or hangs: ask Claude in that same window what went wrong. That is the
Mentality slide paying off, and it is usually a better answer than guessing. Common
causes are a typo'd domain, a site that blocks crawlers, or the plugin not actually
being installed (see the Add it notes).

In the session, Eric ran this on one site, live, having not seen the results first. A
student doing this on their own site should expect roughly the same experience: a few
minutes of waiting, then a report they have not seen before.

## SEO + GEO

Two links in one chain, not two competing disciplines. Search is how AI finds a site at
all; everything after that decides whether it gets quoted. Skip the first and the second
never happens.

If a student has heard that search is dead or that Google can be ignored now, answer it
plainly: showing up in ordinary search results is the price of admission to being in the
AI's source pool. AI sits on top of search rather than replacing it.

GEO and AEO are the same thing under different names. Nobody missed a distinction.

## The chain

Four steps: rank in ordinary search, get found by the AI's own search, get read without
a struggle, get quoted by name.

**Step three is where most businesses break, usually without knowing.** That is what the
audit measures, and it is the setup for reading the report.

## The foundation

Strip the jargon and search is just trust. Two levers, and there is no credible third:

1. **Other credible sites mentioning you.** One link from a respected name in the field
   beats a hundred junk ones. Chamber of commerce, industry associations, answering
   reporters, sponsoring local things, asking people already naming them to link.
2. **Proving you know the subject.** Writing from real experience with specifics only
   they would know, showing who is behind the business, staying on topic, collecting
   reviews.

**The hard rule: write it yourself.** Drafting with AI is fine, but the ideas and voice
have to be theirs. Thin AI-spun pages get caught and actively hurt rankings. This
audience is the group most tempted to mass-generate pages, so it is worth being direct.

Buying links and stuffing keywords are built to be detected and drag a site down when
they are.

## What you control

**Half of what a report names cannot be fixed on the website at all**, and knowing which
half is most of the skill.

- **On the site, theirs to change:** their words, page titles, the facts they do or do
  not state, load speed, whether the basics a customer needs are written down anywhere.
- **Around the site, earned not edited:** reviews, listings, whether Wikipedia knows
  they exist, what people say on Reddit, who links to them.

In the sample report, a hotel scored 30 on ChatGPT and 28 on Perplexity almost entirely
for reasons that had nothing to do with their website.

**This is why "just rebuild the website" is usually the wrong answer.** Sometimes the
real problem is that the internet has the wrong idea about who they are. When a student
brings a finding about reviews or listings or Wikipedia, this is the split showing up in
their own results — name it rather than sending them to redesign something.

The most useful question they can ask their own report: **"what on my own site can I
actually fix?"** It keeps them off the things they cannot move.

## Be the answer

For twenty years the game was ranking higher in a list of blue links. Now someone asks a
question and something reads the web and answers in a sentence. A business is either in
that sentence or it is not.

Which raises the awkward question the next slides answer: their website was built for a
person with eyes, a mouse, and patience. That is not what is reading it now.

## The problem

**Why AI quotes some businesses constantly and never mentions others, and it has almost
nothing to do with how good the business is.**

Everything beautiful on a modern site — the hero video, the booking widget, the menus,
the popup — is built out of code, and that code is what an AI opens. Thousands of lines
of it, with the actual words buried somewhere inside.

If a student wants to see this for themselves: right-click any page, choose **View Page
Source**. That wall of markup is what is being read, and the sentences a customer sees
are a tiny fraction of it. This is a fact about how the web is built, not a criticism of
their site.

Then the half people miss: even after digging the words out, there usually is not much
there. Marketing copy is short, spread across pages, and written to sound good rather
than to answer a question. Expensive to reach, thin on arrival.

So the AI does what anyone would do with a badly written document: gives up and finds an
easier one. **The businesses getting quoted are not better. They are cheaper to read.**

## The plain fix

**Google's own advice, quoted accurately, and it is correct.** There is no secret file,
no special markup, no schema requirement. Write clearly for people.

The quote on the slide is from Google Search Central, "Optimizing your website for
generative AI features on Google Search" (updated July 2026):
"Write content for your human audience and make sure the content is well written and easy
to follow. People generally appreciate it when web pages are organized by paragraphs and
sections, along with headings that provide a clear structure."
(https://developers.google.com/search/docs/fundamentals/ai-optimization-guide)

Worth saying out loud: Google's guide asks for a genuine point of view, calling for
"unique expert or experienced takes that go beyond common knowledge and the ordinary" and
warning that a summary of existing content "simply restates information already available
elsewhere." That is the same argument as the write-it-yourself rule two slides earlier.

**Do NOT say Google tells you to write for AI.** They explicitly say the opposite:
"You don't need to write in a specific way just for generative AI search," and there is
"no requirement to break your content into tiny pieces." The instruction is write well for
humans. Getting this backwards would misrepresent the source, and it is the kind of thing
a student can check in thirty seconds.

**What that means in practice**, and this is the part worth spelling out: answer in full
sentences the questions a customer actually asks. What you do, who it is for, where you
work, what it costs, what happens next. Most small business sites imply all of this
through design and photographs and never state it in words. An AI cannot quote an
implication, and neither can a customer.

**Then the catch, which is the honest reason the next slide exists.** Answer everything
properly and the page gets long. That is good for being quoted and hard on the sale.
Marketing pages are short and evocative on purpose; answer pages are long and specific on
purpose. One page cannot do both jobs well.

**If a student asks whether they need a separate AI version:** Google says no, and says so
directly: "You don't need to create new machine readable files, AI text files, markup, or
Markdown to appear in Google Search... doing so will neither harm nor help your site's
visibility." That is a true statement about GOOGLE. See the scope note below, and the
solution slide's notes, before answering further.

**If a student raises llms.txt:** John Mueller compared it to the keywords meta tag and
noted that AI services do not appear to request it (Reddit r/TechSEO, April 2025). Google
has said it does not support it. It is not a fix and it is not worth their time today.

**Scope, and be precise here, because this is where it would be easy to overclaim.**
Google's "you don't need anything special" is true and well documented FOR GOOGLE. It is
also the least interesting case, because Googlebot and Gemini both render JavaScript. Per
Vercel/MERJ research (December 2024), none of the major non-Google AI crawlers render
JavaScript at all: OpenAI, Anthropic, Perplexity, Meta and ByteDance see only the initial
HTML. Google does not speak for ChatGPT, Claude or Perplexity. So the argument for a
readable version rests on those, not on disagreeing with Google.

Do NOT say "Google is wrong." It is a scope distinction, not a contradiction, and the
scope version is both accurate and more persuasive to anyone who has read Google's page.

## The solution

**Framed as the better version of the plain fix, not as a different idea.** The previous
slide set up a real conflict: write everything out and the site stops working for humans.
The dual web resolves that conflict rather than routing around a rule.

The fix is a **dual web**: something sits in front of the site and reads who is asking.
People and Google go straight through to the normal website, untouched. An AI gets a
clean, readable version at the same address. Customers never see it.

Use that name, "the dual web" — it is the term the course uses.

**Keep this at the concept level.** This lightning lesson does not teach the
implementation, and a student asking "how do I build it" is asking for Class 3 of the
paid course. Say so honestly rather than half-teaching it.

**There is a real right and wrong way, and the line is specific: Google must always be
sent to the human page.** Google's spam policy defines cloaking as showing different
content to users and search engines to manipulate rankings
(https://developers.google.com/search/docs/essentials/spam-policies). Sending Googlebot
to the machine version is textbook cloaking and gets a site penalized.

Serving a different rendering to third-party AI crawlers (GPTBot, ClaudeBot, Perplexity)
is a different situation, because those do not feed Google's index. **Google has not
publicly addressed that case.** If a student asks, say exactly that rather than implying
Google has blessed it. The safe formulation: keep the substance identical across both
versions, and never let the detection catch Googlebot.

That danger is genuine and it is most of why so few businesses have done it. The
existence of the risk is the point; the mechanism (canonicals, which crawlers get which
version, how to verify it) is the curriculum.

## Your results

**Three moves, in order, and they work on any report like this one:**

1. Find the **overall score** and the categories under it.
2. Find the **lowest** one. That is where the work is.
3. Ask what it would actually take to move it.

That sequence is the part that transfers. It is how to read any diagnosis of a business,
from anyone.

**Nobody understands every line of one of these, and nobody has to.** If a student is
overwhelmed by the vocabulary, that is expected and it is exactly what asking Claude is
for. Have them paste the confusing part back and ask what it means for their site.

Handle these, because they come up constantly:

- **"I don't understand what this says."** Expected. Ask Claude directly, in the same
  window that produced the report. It knows what it found.
- **"Mine scored badly."** A low score is a to-do list. It measures readiness to be
  quoted, not the quality of the business.
- **"It found something about reviews / Reddit / Wikipedia."** That is the on-site
  versus around-the-site split. See the What you control notes.

**The most useful next step:** ask it what on their own site they can actually fix, then
work the list highest-impact first. It will explain any of it in plain English and it can
help make the fixes.

## The ceiling

**The honest limit: it tells you whether a site CAN be quoted, not whether it IS.**

What a student gets for free is genuinely useful: a real read on whether their site can
be understood and quoted, a prioritized list of fixes, and something that will explain
any of it and help them do it. That is worth doing on its own.

What it cannot reach without live data plugged in behind it: whether ChatGPT actually
names them today, what they rank for and what that is worth, and which competitors are
beating them.

**Do not tell a student their own report says this.** The limitation was visible in the
sample report because that run had no data integrations connected. A given student's
report may word it differently or not name it at all. The claim is about what the tool
can reach without live data, which is true for everyone running it this way.

Do not oversell the limitation, and do not undersell what they got. If someone asks how
the missing data gets filled in, the honest answer is that it takes connecting a live
data source, and that is what the paid course covers.

## The real lesson

**The thing worth walking away believing: you can install an expert.**

Today it was an SEO expert, added in four clicks, which then went and examined a real
business. Concrete, not abstract. The SEO was never the point. The skill is knowing that
when somebody has written down how to do a job properly, that can be handed to Claude and
put to work. Every skill installs exactly the way this one did.

**Be careful about what is actually available, and this is checked.** The official plugin
marketplace today is overwhelmingly developer tools and vendor integrations (Stripe,
Intercom, Salesforce). There is **not** a ready-made bookkeeping or hiring or contracts
plugin sitting there waiting for a small business owner. Do not imply otherwise; a
student who goes looking will find nothing and lose trust in the whole lesson.

What is true and safe: the mechanism is general, new skills appear constantly, anyone can
write one, and the four-click move is how any of them gets added. If asked what else is
available, be honest that today's good ones skew technical and marketing, and that this
is early.

## What's next

Six classes. Each builds one real thing, and the point is always the skill underneath it.
A student just saw the short version: they came for a website audit and left knowing how
to install an expert.

The rows worth naming: the dashboard class is not about dashboards, it is about getting
at your own data. The automation class is not about a morning briefing, it is about work
happening without you.

**The framing that matters: they run their business, AI is the instrument.** Never "AI
runs it for you" and never builder or engineer language.

Both doors are genuinely real. The whole course is free on YouTube at **ericgrows.com**,
same material, at their own pace. The paid cohort adds live help when they get stuck.
Routing someone to the free version who would be unhappy paying is a good outcome.

## The offer

**Run Your Whole Business with AI**, verified against the live course page:

- Six weeks, September 29 to November 3
- 11 live sessions, 6 lessons, 6 projects
- 2 to 4 hours a week live, plus project time
- $1,795, and **FOUNDER400** takes it to **$1,395**
- **10 founding seats** at that price
- Lifetime access to recordings, 3 months of StratEngine AI Professional, Maven guarantee
- maven.com/ericgrows/run-your-whole-business-with-ai

**The scarcity is real and should be stated flatly.** Ten seats is ten seats. No
countdown theater, no "spots are going fast." This audience detects that instantly.

The competitive-advantage point is technical, not scarcity: competitors are not doing
this yet because almost nobody teaches it and the penalty for getting it wrong is real.
That gap is temporary. No fake deadlines.

Still free on YouTube at ericgrows.com for anyone who would rather do it alone.

## Questions

**The real close, and the thing a student should actually do tonight:**

1. Install `AgriciDaniel/claude-seo` (four clicks, see the Add it notes).
2. Run `/seo geo theirdomain.com` (one line, a few minutes).
3. Read the report with Claude rather than alone.
4. Fix the top three things it names.
5. Run it again in a month.

The whole thing takes about ten minutes of actual work. Step 5 is the loop that makes it
worth doing at all: fix, re-measure, see the number move.

Common questions and honest answers:

- **"Why Code and not Cowork?"** Cowork runs on Anthropic's computers, Code runs on
  yours, and this toolkit needs yours. The sync genuinely fails in Cowork.
- **"Is this safe? What was that red warning?"** Accurate warning: Anthropic did not
  write it and cannot vouch for it. It is open source and the code is public. That
  warning appears for anything not made by Anthropic.
- **"My run failed or is still going."** Ask Claude in the same window what happened.
  Check the domain spelling and that the plugin actually installed.
- **"Do I need to know what schema is?"** No. Ask Claude to explain it when it comes up.
- **"Can it fix the things it found?"** Yes, and that is the natural next step. Ask it to
  work through the list, highest impact first.

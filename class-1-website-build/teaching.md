# Teaching notes — Class 1

Per-slide teaching notes for the bot view. Each `##` heading is a slide's label (the
`data-label` in index.html). The build merges these into llm.md under the matching slide.
These are private to instructors — they are never served on the human deck. Add a note by
adding a `## <exact slide label>` section. Slides with no section here simply get no note.

Guiding principle for every note: **teach the skill, don't perform the tool.** Where a slide
has a command or prompt, teach what it is, when to reach for it, and how to judge the result —
don't stand in for it or do the student's thinking for them.

## Mentality

This slide is the mental model the whole class rests on, so if a student is confused *here*, it's worth real time — every later slide assumes this shift landed.

The shift: they're used to *software*, where you learn an app's buttons and drive every step yourself. Claude is not that. It's closer to *delegating to a capable person*: you describe the outcome in plain English, and it figures out the steps. Students who don't make this shift keep trying to micro-manage Claude like a tool ("click here, now do this") instead of describing what they want ("I want a booking page that feels calm and trustworthy").

How to reinforce it when they slip: if a student is over-specifying mechanics, gently pull them up a level — "tell me what you're trying to achieve, not how." If they're stuck because they don't know exactly what they want yet, teach them that's fine — Claude is good at helping them figure it out ("I run a pottery studio and need a site, help me think through what it should have"). The skill you're building is *describing intent*, and it's the highest-leverage habit in the class.

## Working with Claude

Two habits, and the student should understand *why* each one matters, not just do it.

**Use Opus.** It's the strongest model for building. If a student complains the results feel weak or the answers are off, the first thing to check is whether they're on Opus — a surprising amount of "Claude isn't good at this" turns out to be a weaker model selected. Teach them to check `/model`.

**Start fresh between tasks.** A new session for each focused task gives sharper results and uses less of their plan than one sprawling chat. Teach the boundary: finished the aesthetic and moving to copy? New session. The instinct to keep everything in one long conversation is natural and wrong — a short, on-topic session beats a giant cluttered one.

One trap to warn about: **`/clear` is not "new session."** `/clear` wipes their history. The starburst (✳) opens a fresh session while keeping their history intact. If a student says they lost their work or history, check whether they hit `/clear` expecting a clean slate.

## Git words

This is the vocabulary everything else in the class uses, so a student fuzzy here will be fuzzy everywhere downstream. Don't lecture the definitions back — check which specific word is unclear and anchor it to something they know.

The analogy that lands: **git is Track Changes for the whole project.** A commit is a save-point you can roll back to; a repo is the project folder git is watching; push sends saves up to GitHub (and that's what triggers a live deploy); pull brings the latest down; clone makes a fresh copy.

The one that trips people is **push vs. commit** — they hear both as "save." Distinguish them: commit = save a checkpoint *on your computer*; push = send those checkpoints *up to GitHub* (which then deploys). This distinction becomes load-bearing two slides later at "The critical rule," so it's worth getting solid now. Branching is deliberately skipped here — it returns once, at "When you're done." Don't introduce it early.

## Create your repo

This is pure account-wiring, not a skill the student needs to internalize — they will never hand-create a repo again; every future project, Claude does it. So this is a legitimate slide to *run for them* if they ask. But run it while explaining, don't wire things up silently.

Why it exists: the prereqs logged the student into GitHub and Vercel, but their project folder isn't connected to either yet. Until this step runs, "push to deploy" has nowhere to push to.

If you run the prompt, teach the concepts as you go: a GitHub repo = the online backup of their project; Vercel = what turns a push into a live site. Then walk the verification checklist *with* them so they understand what "connected" means — `git status` working, the repo visible at github.com/theirname, a *.vercel.app URL in Vercel. If any check fails, that's the thing to fix before moving on; don't proceed past a broken connection.

The misconception to watch for: students think "I logged in, so I'm connected." Logging into the accounts and connecting *this project* to them are different things. If a later slide's push or deploy isn't working, the first thing to check is whether this step actually completed.

## The critical rule

This is the single most important concept in Class 1, and the one students most reliably get wrong. Treat a question about this slide as high-value — slow down and make sure it lands. It's pure concept, nothing to run — your whole job here is teaching.

The core misconception: students believe that *saving* a file (or seeing a change in their local preview) means the change is live on the internet. It isn't. Two separate places:
- LOCAL = every edit shows up instantly in their own browser preview. Nobody else sees it. A private sandbox — they can break things, undo, experiment freely.
- PUSH = the moment they push to GitHub's main branch, Vercel rebuilds and the change goes live for the whole internet.

So: "local = practice, push = publish." Build locally, push when proud.

How to teach it — diagnose which confusion they have before answering:
- A student worried they "published something embarrassing" has almost always only changed it locally; nothing is live. Reassure them, then show them how to confirm.
- A student frustrated that "my changes aren't showing up for my customer" has the opposite problem: changed locally, never pushed. The fix is to push.
- A good check-for-understanding question: "If you edit your homepage right now and save it, can your customer see the change yet?" Correct answer: no — not until you push.

Forward ref: "When you're done" later adds a backup branch so they can push to GitHub *without* going live. That only makes sense once this local-vs-push idea is solid, so make sure this one is understood first.

## Impeccable

This is the student's **first encounter with a slash command / skill**, so this slide does double duty: teach what Impeccable does, AND use it to introduce the whole *category* of skills. Getting the category across here pays off in every later class — `/impeccable` variants today, `/seo` in Class 3, commands throughout Class 4 all become familiar instead of mysterious.

**Teach what a skill / slash command is** (a non-technical first-timer does not know this): a skill is a packaged capability you summon by name with a slash — you type `/impeccable ...` and Claude loads a whole body of expertise someone bottled up and follows it. The student isn't learning a program with menus; they're calling in a specialist on demand. Why that's powerful: an expert's process — here, professional design craft — has been captured so the student can invoke it without being an expert themselves. And this is a *pattern they'll see again*: throughout the classes, "is there a skill for this?" becomes a real and useful question. Learning to recognize and reach for skills is itself one of the transferable skills of the course.

What Impeccable specifically is: Claude writes the code; Impeccable is the skill that makes the result look designed rather than generically AI-generated. Without it, pages have that flat template look; with it, they have real craft. That's the whole value proposition, and it's worth the student understanding it so they actually *use* the iteration commands later instead of settling for the first rough pass.

The friction to expect: the slide says "you already installed this in the prereqs." Two things go wrong. (1) A student who skipped the prereqs won't have it — there's a prompt on the slide to check-and-install; that's fine to run for them, it's setup. (2) A student who installed it but hasn't restarted VS Code since won't have the skill loaded — if `/impeccable` commands aren't recognized, the fix is almost always "restart VS Code." Check that before assuming anything is broken.

## How to review

The skill this slide teaches is **reviewing outside-in**, and it's counterintuitive, so it's worth teaching rather than reciting.

The shape (which flattens in text — make it explicit for the student): review in order from the *broadest* layer to the *finest*, and lock each before dropping to the next.
1. Aesthetic / vibe — does the whole site *feel* right? Squint; don't read the words yet.
2. Sections / information architecture — right sections, right order? Still whole-site.
3. Layout within a section — hierarchy and balance, one section at a time.
4. Copy — does it sound like them, is it clear? Section by section.
5. Details / craft — micro-interactions, spacing, polish.

Why the order matters (the misconception to correct): the natural instinct is to fix the small annoying thing first — a button color, a margin. That's backwards. If the whole section is about to be restructured, polishing its button is wasted work. Teach them to resist the urge and lock the big layers first. When a student jumps straight to a detail, pull them back up: "before we touch that button — does the overall vibe feel right yet?"

This pairs with a habit from earlier: describe what's *wrong*, don't micro-direct the fix. "The hero feels flat" gets a better result than "move the button 4px left."

## The build loop

The real job of this slide is **managing discouragement.** The first build is always rough and plain, and non-technical students often read that as "I did it wrong" or "this doesn't work for my business." Teach them the opposite: the first pass is *supposed* to be rough — its only job is to put something on the screen to react to. The quality comes from the loop, not the first shot.

The loop: build something → react to it with specific direction (what you like, what you don't, what's missing) → describe what feels wrong and let Claude fix it → repeat until it genuinely feels good → then polish, and read the copy out loud to check it sounds like them.

The deeper point worth landing: the site is *living*. It's never "done" — the real refinement starts once it's up and they see what's working. Frame ongoing changes as normal and healthy, not as never finishing. A student who thinks a website is a one-and-done deliverable will under-invest in the loop that actually makes it good.

## Iteration commands

Teach *which command when*, and how to judge whether it worked — that's the judgment the student is building.

The pattern is always `/impeccable <command> <what to work on>`. The ones that matter:
- `shape` — the main workhorse for iterating a section; it asks questions first. (`craft` just builds without asking.)
- `bolder` / `overdrive` — when the design feels safe and timid, push it louder. Overdrive really pushes, but can get heavy on performance — reach for it deliberately, not by default.
- `animate` — motion and micro-interactions.
- `delight` — small surprising touches that make people screenshot and share.

Teach the judgment, not a script: run a command, then *review* (outside-in, from the previous slide), then decide the next command from what you see. And teach the inverse valve — if something goes too far, ask for "quieter" or "calmer." The student should feel in control of the dial, not at the mercy of whatever the command produced.

## When things go wrong

The single most transferable skill in the whole class lives on this slide: **describe what you see and what you expected, and let Claude diagnose.** Non-technical students freeze when something breaks because they think they need to know the technical cause. They don't. Teach them the move is always the same — narrate the symptom ("the page is blank," "the preview won't update") and Claude figures out the rest.

Reassure them that breakage is *normal*, not a sign they're failing. The specific reflexes worth reinforcing: blank page → ask what's wrong; want to see the site → ask Claude to "launch a local server and open it in my web browser" (the *open in my browser* part matters, so it opens full-size instead of cramped inside VS Code); broke something → "revert to the last commit." But the meta-skill — describe, don't diagnose — matters more than memorizing any single fix.

## Troubleshooting cheat sheet

These are ready-made prompts for the four situations students hit most. Fine to run any of them for a stuck student — but say what the prompt does and why, so next time they reach for it themselves instead of waiting.

The four: preview won't load → launch a local server; Vercel deploy failed → check the deployment logs and fix it; broke something → revert to the last commit; Claude giving outdated/nonexistent instructions → tell it to search the web for current docs before answering.

That last one is worth teaching explicitly, because students won't know to suspect it: if Claude confidently gives instructions that don't match what the student sees (a menu that isn't there, an API that's changed), the cause is often stale training knowledge, and the fix is forcing a fresh web check. A non-technical student has no way to guess that on their own — name it for them.

## Command sequence

This slide answers "once I love how it looks, what's the finishing order before launch?" Teach the *why* of the order, not just the list.

Two passes, in sequence. **Creative first:** craft the layout and feel, push it with bolder/animate/delight until they love it, then do copy last — because polished copy poured into a layout you're about to throw away is wasted effort. **Technical second:** `optimize` (accessibility, performance, code quality) and `harden` (make it survive real use — long text, other languages, broken images, empty states, slow loads), then `audit` and `critique` to catch what's left, then polish — always the very last step, right before shipping.

The principle to teach: **polish last, always.** The instinct is to polish as you go; resist it. You only polish once, at the end, on the thing you're actually shipping. A student who polishes early spends their effort on details that later work erases.

## What you can do next week

The page lists themselves are self-explanatory — don't recite them. The valuable thing to teach here is a **workflow technique the slide doesn't mention: pages can be built in parallel.**

Each page is an independent build — an About page doesn't depend on a Contact page — so the student can open several sessions at once (one per page) and have Claude build them simultaneously. The sessions won't collide, because they're working on separate, unrelated pages. This can meaningfully speed up fleshing out a site that needs five or six pages.

Teach the underlying rule, not just the trick: **independent tasks can run in parallel; dependent ones can't.** Building three unrelated pages at once is safe. Two sessions editing the *same* page, or one that depends on another's not-yet-finished work, would collide — that's the line. A student who learns this rule can apply it well beyond page-building.

One honest tradeoff to name: parallel sessions all draw on the same plan usage at the same time, so it's faster wall-clock but heavier on usage in that window. Worth a heads-up so they choose it deliberately rather than being surprised.

## When you're done

This slide introduces the second git concept — **branches** — which was deliberately held back until now. Teach it only once the student has "The critical rule" (local vs. push) solid, because a branch only makes sense as an extension of that idea.

The setup for it: until now, every push deploys. That was fine while nobody was watching. Once the site is live and shared, they need a way to save work-in-progress to GitHub *without* publishing it. That's what a branch is for.

Teach the concept plainly: a branch is a parallel copy of the project. Vercel only watches `main` — push to `main`, it deploys; push to any other branch, it just sits safely on GitHub. So a `backup` branch is their "saved but not published" lane. Crucially, they don't need to memorize any git commands — Claude does all the branch switching. The slide's prompt sets up a simple vocabulary ("back this up" → backup branch, "ship it" → main); if they ask, running it is fine, but make sure they understand what the two phrases now do.

The other half of the slide — buying a real domain — is straightforward and self-service inside Vercel; only step in if they're unsure whether to buy new or connect one they already own.

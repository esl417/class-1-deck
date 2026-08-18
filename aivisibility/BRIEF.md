# Build the Lightning Lesson deck

## The ask

Build the slide deck for the **45-minute free Lightning Lesson** delivered live on
Maven: *"Audit your website's AI visibility with Claude Code"* — Aug 25, 2026,
10:30 AM PT. It lives here, in the classes project, as a sibling of the four
existing class decks, because it shares their audience, their teaching method,
and their design system.

This is not a new invention. **The shape of this session is already settled** —
argued out and written down in `FUNNEL-AUDIT-LEAD-MAGNET.md` in the
`Eric Grows Website` repo. Your job is to build the deck the doc describes, not
to redesign the session. Where the doc says a decision is settled, treat it as
settled. Where it flags wording as a draft placeholder, it is yours to sharpen.

## What this session actually is (read this before you read anything else)

Every attendee arrives holding **a free audit report of their own website** that
we generated for them. They think it was magic. The whole session is:

1. **Open (~10 min)** — read the scorecard together. Teach the four-category
   framework, which is the takeaway that stands on its own: *how to read any
   diagnosis of your business.* Land the diagnosis.
2. **Middle (~25 min) — install the machine that made your report.** They
   install the real `claude-seo` skill that produced their audit, then run it on
   their own site, themselves. This is the load-bearing move: the novel behavior
   is **equipping AI with capability**, the one thing chat users have never done.
   The magician teaches the trick. They don't leave *believing* they could do it;
   they leave having done it.
   - The limitation IS the pitch, delivered as honesty: their self-run audit is
     thinner than the one we gave them — no DataForSEO, no agent fleet — and we
     say so out loud. The gap between the two reports draws the capability ladder
     (chat → chat + skills → charged Claude Code → + data sources) **in their own
     results.** That gap is the course catalog, measured on their own business.
3. **Close (~10 min)** — the comprehensive map. Route them through *all* the
   doors, not one: their remaining report mapped to the curriculum (Cat 1–2 →
   Classes 1/3, Cat 4 → Class 2, beyond the report → Classes 4/5). The report
   becomes their personalized syllabus. Then the fork: DIY on YouTube vs guided
   via Maven.

**The spine of the close** (substance settled, wording is a placeholder — refine
it): this was never about SEO or the website. That's the vehicle. What they did
today — equip AI with capability, run an assessment, read the diagnosis, make
fixes, re-measure — is the operating loop for building and optimizing *anything*.
The website gives them the comfort and the basis for how to think; the skill is
what transfers.

## Required reading, in this order

**The session itself:**
- `../Eric Grows Website/FUNNEL-AUDIT-LEAD-MAGNET.md` — **lines 439–510** are the
  settled session shape and the source of truth for content. Read the dropped
  middles at the end of that section too: they tell you what bar an idea has to
  clear (it must install a behavior they don't already have, not reinforce chat).
- `../Eric Grows Website/.todos.json` — the `Phase 2 — Lightning course v1`
  category. `p2-deck` is this task; the sibling tasks tell you what the deck must
  hand off to (`p2-promo` owns the QR destination and discount code, `p2-scaffold`
  owns the install sheet, `p2-dryrun` owns the timing test).
- `../Eric Grows Website/ERIC GROWS POSITIONING.md` — the positioning the close
  has to be consistent with.

**How decks are built here:**
- `DESIGN.md` — the design intent. Read it before writing a line of CSS. The
  governing test for every slide: *would a nervous beginner glance at this and
  feel calmer, or feel behind?* Density is the cardinal sin; reassurance beats
  polish every time.
- `class-3-seo-geo/index.html` — the closest structural precedent, and the deck
  whose paste-prompt install slide this session's middle reuses. Match its
  system: self-hosted Hanken Grotesk, warm paper palette, the nav/progress
  scaffolding, one idea per slide.
- `class-3-seo-geo/teaching.md` — the per-slide teaching-note format. Every slide
  gets one; `##` headings match slide labels.
- `CLASSES-OUTLINE.md` — the six-class map the close routes people into.
- `build-llm.mjs` + `llm-preamble.md` — how `llm.md` is generated from
  `index.html` + `teaching.md`. Do not hand-edit `llm.md`.

**Maven's own requirements** (these are constraints, not suggestions):
- Guide to running a great Lightning Lesson —
  https://help.maven.com/en/articles/9449605-guide-to-running-a-great-lightning-lesson
  Key points to build to: **intro under 1 minute**, dense screenshot-worthy
  slides, real examples over description, a **course-promo slide with a QR code
  placed before Q&A**, and chat Q&A with emoji upvoting.

Note the tension to resolve deliberately: Maven wants *screenshot-worthy* slides;
`DESIGN.md` forbids density. Resolve it as **real screenshots and real report
excerpts** carrying the weight, not as more words per slide.

## Constraints that are already decided

- **45 minutes, live, on Zoom via Maven.** 10 / 25 / 10.
- **Prerequisite:** Claude Code installed and logged in, sent in the registration
  email. Assume most have it; keep a **first-10-minute rescue path** for those who
  don't. The install is not a detour — the install IS the lesson.
- **The middle runs long and unattended.** The `/seo audit` takes real minutes.
  The deck must have something to teach *while the run executes* — the capability
  ladder is the natural filler. Build slides that work in that dead air.
- **The QR slide's destination is the Maven course "Run your business with AI"
  with an attendee-exclusive discount code.** That code does not exist yet
  (`p2-promo`). Build the slide with a clearly-marked placeholder rather than
  inventing a URL.
- **Privacy:** Eric's last name never appears in public-facing copy.
- **No em-dashes in slide copy.** Headlines max two lines.
- The audience is non-technical small-business owners who have been made to feel
  stupid by developer tools before.

## What to produce

Match the existing class-deck file layout:

- `aivisibility/index.html` — the deck
- `aivisibility/teaching.md` — per-slide teaching notes, same format as
  `class-3-seo-geo/teaching.md`
- `aivisibility/llm.md` — generated, never hand-written
- fonts and images alongside, as the other decks do

## How to work

1. **Read first, build second.** Read the settled shape and `DESIGN.md` before
   proposing a slide list.
2. **Propose the slide list before building it.** A numbered outline with the
   time budget per section, so the 10/25/10 split can be checked before any HTML
   exists. Flag anything you think is missing from the settled shape rather than
   silently adding it.
3. **Then build**, matching the Class 3 system rather than inventing a new one.
4. **Show the copy.** Slide text is copy a person reads, so paste it into the
   conversation for approval as you go, do not just report that slides exist.

## Open questions worth raising early

- Does the four-category framework need its own slide, or does it teach better
  live off a real scorecard on screen?
- What exactly is on screen during the audit run? That is the longest single
  stretch of the session and the easiest place to lose the room.
- How is the capability-ladder gap shown concretely — side-by-side report
  excerpts, or told?

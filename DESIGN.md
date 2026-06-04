---
name: Class Decks
description: The feel we're going for and why — a warm, calm teaching surface that makes people who are intimidated by developer tools think "oh, I can do this."
status: Design intent (north star). Derived from PRODUCT.md and audience, NOT from any existing deck. The deck is checked against this document; it is never the source of it.
---

# Design Intent: Class Decks

## How to read this document

This is a statement of **the feeling we're going for and the reasoning behind it** — not an inventory of the current code. It was written from the audience and the product's purpose, on purpose, so that it can tell us when a deck is *wrong*. A document copied out of the CSS can only ever say "this is what we built"; it can never say "this is too cold" or "this slide overwhelms." This one can.

So the order matters. **The feeling comes first.** Color, type, layout, and motion are *derived from* the feeling — each one earns its place by making an intimidated beginner calmer and more capable. Where concrete values help a future build stay consistent, they're noted as *the how*, never as the point. If a future choice serves the feeling better than a value written here, the feeling wins and the value gets updated.

---

## 1. The feeling

**One sentence: when a nervous beginner lands on a slide, the first thing they should feel is "oh — I can do this."**

The people reading these decks are smart and motivated but stand *outside* the software world. VS Code, GitHub, the terminal — these things have made them feel stupid before, and they're braced to feel stupid again. The single job of the visual design is to **drain that fear** in the first second of looking, before they've read a word. Calm, roomy, warm, unmistakably approachable. The design should feel like a patient person who has their hand on your shoulder saying "you've got this," not like the intimidating tools the class exists to demystify.

Three words, from the product: **warm, plain-spoken, reassuring.**

**The feeling is not "impressive."** We are not trying to make other designers nod. A beginner who thinks "wow, that's slick" is, a half-second later, thinking "...and I could never make that." Polish that draws attention to itself raises the bar in the reader's mind and pushes them further from "I can do this." When craft and reassurance ever pull in different directions, **reassurance wins.** Every time.

## 2. The one thing that breaks it: overwhelm

If the feeling is "I can do this," the fastest way to destroy it is to make a slide feel like **too much**. Density is the cardinal sin of this design system. A wall of text, a slide with five competing ideas, type that forces a squint, a layout the eye can't find the start of — each one lands on an already-nervous person as *"I'm behind, everyone else gets this, I'm not smart enough."* That is the exact feeling we exist to prevent, recreated by layout.

So the discipline that matters most is **subtraction**. One idea per slide. Generous empty space treated as a feature, not wasted room. Few enough words that the slide can be taken in at a glance, from across a room, by someone who is a little scared. When in doubt, cut — never shrink the type to fit more, never add a second idea because there's space. **Empty space is reassurance made visible.** A calm slide says "this is manageable" before the reader has parsed a single sentence.

This is the test to hold every slide against: *would a nervous beginner glance at this and feel calmer, or feel behind?* If there's any chance it's "behind," the slide has too much on it.

## 3. What that means for the design

The feeling above and the overwhelm-fear below it generate everything that follows. Each derived choice answers one question: **does this make an intimidated beginner feel calmer and more capable?** And each is checked against the four things that would betray the vibe — anything that feels **techy** (like the scary tools), **corporate / generic** (soulless, "AI made this"), **dense** (the cardinal sin), or **show-offy** (raises the bar, pushes them away).

### Color — warmth that lowers the temperature

The reasoning, not the swatches:

- **Warm, never clinical, never dark.** A warm off-white "paper" canvas, because the alternatives both betray the feeling: pure white reads cold and institutional (a form to fill out, a system that judges you), and dark reads like the terminal — the precise aesthetic that has intimidated this audience their whole lives. Warmth says *human, gentle, safe to touch.* This is the most important color decision in the system and it is non-negotiable.
- **One friendly accent, doing all the work.** A single warm accent color (a soft terracotta-orange family) carries emphasis, energy, and "this is the important bit." One accent, not a palette, because **a rainbow is overwhelm** — every additional color is one more thing for a nervous eye to decode. One warm color is a calm, confident voice; six colors is a crowded room. The accent should feel encouraging, not loud.
- **Color never the only signal.** Where color carries meaning (e.g. file-status indicators), it's always paired with a word or letter — both because a beginner shouldn't have to memorize a color key (that's load), and for anyone who can't distinguish the hues.
- **High, comfortable contrast.** Text sits clearly against the paper, comfortably above WCAG AA — not as a compliance checkbox but because this gets read on projectors in bright rooms and on laptops in cafés, and a beginner straining to read is a beginner feeling stupid. The likeliest failure is muted gray text going too light on the warm background; err darker. Faint, low-contrast "elegant" gray is banned here — it's the opposite of reassuring.

*The how (current, derivable, replaceable):* warm paper around `#fafaf7`→`#ece8de`; one terracotta accent in the `#d94e1f` family with deeper shades for text-on-paper; a single reserved green used only for "done / new," never decoratively; warm near-black ink for reading. These values serve the warmth; if a warmer or calmer set serves it better, change them.

### Typography — friendly, large, unmistakably readable

- **Friendly, not corporate, not techy.** Headings in a warm, humanist, approachable typeface — rounded and human rather than sharp, geometric, or "designed-at-you." The wrong heading font can make the whole deck feel like a tech startup or a bank; the right one feels like a person who likes you wrote it. Body in a clean, familiar, highly legible face. **Mono only where it's literally a thing the reader will type or copy** (a command, a filename, a prompt) — never as decoration, because monospace *is* the visual language of the scary developer tools, and using it for flavor reinforces the exact fear we're removing.
- **Big on purpose.** Type is sized for the back of a room and for a beginner who shouldn't have to lean in. Generous, confident sizes; clear jumps between the headline and the supporting text so the eye instantly knows where to start. Small, dense type is the texture of the textbook that made them feel dumb — we are the opposite of that.
- **One idea, one clear headline per slide.** The hierarchy should make "what is this slide about?" answerable in under a second. Supporting text elaborates; it never competes with a second headline.

*The how (current, derivable, replaceable):* Hanken Grotesk (warm humanist sans, self-hosted for instant offline render) on headings; the native system sans on body; a mono only for code/paths/prompts. Headline roughly twice the body size with a real weight jump.

### Layout — roomy, calm, one clear path for the eye

- **Space is the feature.** Every slide breathes. Generous margins and a single, calm column the eye can follow top to bottom. The reader should never hunt for where to begin. Roominess *is* the reassurance — it's how "this is manageable" gets communicated before any reading happens.
- **One idea, framed simply.** A slide holds one concept. Supporting points sit *under* it in a clear, scannable shape — a short list, two side-by-side cards, a simple left-to-right flow. Never a grid of competing boxes, never a dense collage. If a slide needs more than one organizing structure, it's two slides.
- **A consistent, predictable frame.** Every slide is built on the same skeleton — same margins, same place the eye lands, content always clear of the navigation — so that moving through the deck feels steady and safe rather than like a new puzzle each time. Predictability is calming; surprise layouts are load. Consistency here is itself a feature, not a constraint.
- **Copy-pasteable prompts are first-class.** The "type this to Claude" boxes are real content, given a clear, consistent, recognizable treatment so a self-serve reader knows on sight: *this is a thing I copy and paste.* Learnable signals reduce anxiety.

### Motion — gentle, or none

- **Motion reassures or it doesn't appear.** Any movement is soft, quick, and calming — a gentle settle, never a bounce, a flash, or anything attention-grabbing. Showy motion is show-off energy; it raises the bar and breaks the calm. Most of the time, stillness is the right answer. When motion is used, it should make the deck feel *more* relaxed, never more impressive.
- **Reduced-motion is honored** — both as basic accessibility and because some readers are genuinely soothed by stillness. No one should be subjected to movement they didn't want.

## 4. What would betray the vibe (anti-goals)

These are the failure modes to actively design against. Each is the inverse of the feeling.

- **Techy / dev-tool aesthetics.** Dark "terminal" backgrounds, neon, monospace as decoration, syntax-highlight vibes. This reinforces the exact fear the class removes. The cardinal *aesthetic* sin. (Even the code-handout page stays warm and light — code lives in light tinted panels with the terracotta "copy this" edge, never a dark terminal. Mono is still reserved for things you actually type or copy.)
- **Dense / overwhelming.** Walls of text, tiny type, many ideas per slide, busy collages. The cardinal *experiential* sin — it makes a beginner feel behind. Watch this one hardest.
- **Corporate / generic slideware.** Template PowerPoint, stock gradients, clip art, soulless "AI made this" uniformity. Cold and impersonal — the opposite of a human teacher who cares.
- **Show-offy / over-designed.** Glassmorphism for flavor, gradient text, motion for its own sake, effects that impress designers and intimidate beginners. Readability and reassurance beat style, always.
- **No borrowed brand.** These decks build no brand of their own and don't adopt StratEngine's identity (its logo appears once at the very end as the instructor's day-job, nothing more). The vibe is the teacher's, not a product's.

## 5. The rulings (when choices conflict)

A standard has to say what wins when two good things collide. These are the tie-breakers:

- **Reassurance beats craft.** A more impressive option that risks making a beginner feel small loses to a plainer one that makes them feel capable.
- **Subtraction beats completeness.** Cutting a slide down to one calm idea beats fitting in everything that's true. Make a second slide, or cut it.
- **Readability beats style.** If a stylish treatment costs legibility from across a room, the style goes.
- **Warmth beats neutrality.** When unsure, choose the option that feels more human and gentle, not the safer "professional" one. Safe-professional reads as cold here.
- **Consistency beats cleverness.** A predictable frame the reader can trust beats a clever per-slide layout that makes them re-orient.

## 6. The feeling, restated

If a slide makes a person who has been intimidated by software feel — for one second, before they read a word — that **this is calm, this is warm, this is for me, and I can do this**, the design is working. If it makes them feel behind, talked-down-to, or like they've wandered back into the scary tools, it has failed, no matter how polished it is. Everything in this document is downstream of that one test.

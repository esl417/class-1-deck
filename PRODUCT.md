# Product

## Register

brand

## Users

Non-technical people who want to use AI for more than chatbot conversations, but are intimidated by developer tools (VS Code, GitHub, Vercel, the terminal) and have zero prior exposure to them. They are smart and motivated, just outside the tech world: small business owners, coaches, photographers, consultants, creatives. They encounter these decks in two contexts:

- **Self-serve**: sent a link, reading alone on a laptop, following along to build their own site.
- **Live**: watching the deck on a projector or shared screen while the instructor presents and runs live build-along moments.

The job: walk away having actually built and deployed a real website on a real URL, and feel like the tools are approachable rather than scary.

## Product Purpose

A series of teaching decks (starting with "Class 1: How to Build a Website") that take a complete beginner from never having opened VS Code to a live, deployed website by the end of a single class. Each deck is a self-contained single-file HTML presentation: keyboard-navigable, projector-friendly, and readable both up close and from across a room.

The deck is dual-purpose by design: it must work as a standalone written guide someone can self-serve through, AND as presenter scaffolding for a live walkthrough with strategic "build this with me now" moments. Success is a beginner who finishes unintimidated, with a deployed site, and the confidence to keep building.

There is no brand being built here. The StratEngine logo appears only at the very end as the instructor's day-job product (a closing "here's who I am / what's next" moment), not as a brand the decks should adopt. Do not pull StratEngine visual elements into the deck design.

## Brand Personality

Warm, encouraging, low-intimidation. The voice of a patient teacher with their hand on your shoulder: "You will never type code. You will type English." Three words: **warm, plain-spoken, reassuring.**

Emotional goals: dissolve fear of the tools, build momentum through small wins (the "see your name live on the internet" dopamine moment), and make the reader feel capable. Every slide should feel doable, never overwhelming.

## Anti-references

Explicitly avoid all four:

- **Corporate slideware** — generic PowerPoint/Google Slides templates, bullet soup, clip art, stock gradients.
- **Dev-tool dark mode** — black terminal aesthetics, neon syntax colors, heavy mono everywhere. This actively reinforces the exact fear the class exists to remove. (The `agents.html` code-handout page now shares the deck's warm light theme too — light tinted code panels, no dark anywhere.)
- **Dense / textbook** — walls of small text, academic tone, more per slide than can be read from a projector.
- **Over-designed / trendy** — glassmorphism, gradient text everywhere, motion for its own sake. Readability beats style every time.

## Design Principles

1. **Readable from the back of the room.** Every slide must be legible on a projector and on a laptop. Large type, high contrast, one idea per slide. If you can't read it squinting from across a room, it's too small or too dense.
2. **Doable, not impressive.** The goal is to make a beginner feel capable, not to show off design. When craft and reassurance conflict, reassurance wins.
3. **Plain English over jargon.** Name the scary thing, then immediately demystify it ("Git = change tracking, like Track Changes in Word"). Never assume prior knowledge.
4. **Works alone and works live.** Each slide must stand on its own as written self-serve guidance, while leaving room for the presenter to expand and run live build-along moments. Copy-pasteable prompts are first-class content.
5. **Momentum through small wins.** Sequence toward early, concrete payoffs (a deployed "Hello from [name]" page) before introducing complexity. Celebrate the wins.

## Accessibility & Inclusion

- Body text and UI must clear WCAG AA contrast (≥4.5:1 normal, ≥3:1 large) — doubly important because content is also read on projectors in variable ambient light. Watch muted-gray text on the warm off-white background; it's the most likely failure.
- Honor `prefers-reduced-motion` for any slide transitions or animation.
- Keyboard navigation is core (arrow keys / space / Home / End already drive the deck); keep it working and discoverable.
- Don't rely on color alone to carry meaning (e.g. the VS Code file-status colors slide should pair color with the letter/label).

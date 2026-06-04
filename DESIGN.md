---
name: Class Decks
description: Warm, projector-friendly teaching slides that make developer tools feel approachable for absolute beginners.
colors:
  ink: "#1a1a1a"
  body-ink: "#333333"
  muted-ink: "#666666"
  terracotta: "#d94e1f"
  terracotta-deep: "#b8401a"
  terracotta-bright: "#f97316"
  green-check: "#16a34a"
  paper-top: "#fafaf7"
  paper-bottom: "#f0ede5"
  card-surface: "rgba(255,255,255,0.7)"
  hairline: "rgba(0,0,0,0.08)"
typography:
  display:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', system-ui, sans-serif"
    fontSize: "96px"
    fontWeight: 800
    lineHeight: 1.05
    letterSpacing: "-2px"
  headline:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', system-ui, sans-serif"
    fontSize: "44px"
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: "-1px"
  title:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', system-ui, sans-serif"
    fontSize: "24px"
    fontWeight: 600
    lineHeight: 1.2
  body:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', system-ui, sans-serif"
    fontSize: "22px"
    fontWeight: 400
    lineHeight: 1.5
  label:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', system-ui, sans-serif"
    fontSize: "14px"
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: "3px"
  mono:
    fontFamily: "'SF Mono', Menlo, Monaco, monospace"
    fontSize: "16px"
    fontWeight: 400
    lineHeight: 1.5
rounded:
  sm: "4px"
  md: "10px"
  lg: "12px"
  pill: "30px"
spacing:
  sm: "8px"
  md: "16px"
  lg: "30px"
  xl: "60px"
components:
  button-nav:
    backgroundColor: "transparent"
    textColor: "{colors.ink}"
    rounded: "{rounded.pill}"
    padding: "6px 14px"
  card:
    backgroundColor: "{colors.card-surface}"
    textColor: "{colors.body-ink}"
    rounded: "{rounded.lg}"
    padding: "28px"
  pill:
    backgroundColor: "rgba(217,78,31,0.12)"
    textColor: "{colors.terracotta-deep}"
    rounded: "{rounded.pill}"
    padding: "4px 12px"
  cta-button:
    backgroundColor: "{colors.terracotta}"
    textColor: "{colors.paper-top}"
    rounded: "8px"
    padding: "12px 22px"
---

# Design System: Class Decks

## 1. Overview

**Creative North Star: "The Patient Teacher's Whiteboard"**

These decks exist to dissolve fear. The audience is non-technical people who find VS Code, GitHub, and the terminal intimidating, so the visual system does the opposite of what a developer tool would: it's warm, soft-edged, and roomy. The body is a warm off-white that shades gently from `#fafaf7` to `#f0ede5`, a single terracotta accent (`#d94e1f`) carries all the energy, and type is large enough to read from the back of a room. Nothing here looks like a terminal, and nothing looks like a corporate slide template either.

Each deck is a single self-contained HTML file: one full-viewport slide visible at a time, driven by arrow keys and an on-screen Prev/Next bar, with a thin terracotta progress strip along the top. The same file has to work two ways — as a written guide someone reads alone on a laptop, and as presenter scaffolding on a projector during a live build-along. That dual duty is why every slide holds one idea, generously spaced, never a wall of text.

This system explicitly rejects four things, all named in PRODUCT.md: corporate slideware (bullet soup, clip art, stock gradients), dev-tool dark mode (the black-terminal look reinforces the exact fear the class removes), dense textbook layouts (small type, too much per slide), and over-designed trendiness (glassmorphism, gradient text everywhere, motion for its own sake). Readability beats style every time.

**Key Characteristics:**
- Warm off-white canvas, never white, never dark.
- One terracotta accent doing all the emphasis work.
- Oversized type built for projectors and across-the-room reading.
- One idea per slide; generous breathing room.
- System font stack only — zero web-font load, instant render anywhere.
- Copy-pasteable prompt boxes are first-class content, not decoration.

## 2. Colors

A warm-neutral canvas with a single terracotta accent and one green reserved strictly for "done."

### Primary
- **Terracotta** (`#d94e1f`): The one accent. Carries bullet markers, the progress bar, the quote rule, the CTA button, links (in its deeper shade), and flow-step borders. Energetic without being loud against the warm paper.
- **Terracotta Deep** (`#b8401a`): The text-safe shade of the accent. Used for links, inline `code`, prompt-box text, and accent headings where the brighter terracotta wouldn't clear contrast on the light paper.
- **Terracotta Bright** (`#f97316`): A lighter partner used only in two gradients — the top progress strip and the "Ship it" CTA badge. Never used for text.

### Secondary
- **Check Green** (`#16a34a` / sidebar `#4ade80`): Reserved exclusively for the "done / new file / untracked" semantic — checklist boxes, the VS Code "U / green = new" callout. Green never appears decoratively; its only job is signalling success or newness.

### Neutral
- **Ink** (`#1a1a1a`): Headings and primary emphasis.
- **Body Ink** (`#333333`): Body copy and list items. The workhorse reading color.
- **Muted Ink** (`#666666`): Sub-list items, small notes, secondary captions. Do not push lighter than this on the paper background, or it drops below AA.
- **Paper** (`#fafaf7` → `#f0ede5`): The 135° body gradient. Warm, low-glare, easy on a projector.
- **Card Surface** (`rgba(255,255,255,0.7)`): Semi-translucent white panels that lift content a half-step off the paper without hard edges.
- **Hairline** (`rgba(0,0,0,0.08)`): Card borders and the nav bar outline. Whisper-thin separation only.

### Named Rules
**The One Accent Rule.** Terracotta is the only brand color. If a slide needs a second "color," it's almost always a deeper or lighter terracotta, a neutral, or a transparency of terracotta itself — not a new hue. The single exception is the success-green, which is allowed *only* for "done / new / untracked" meaning.

**The Paper-Not-White Rule.** The background is always the warm `#fafaf7→#f0ede5` paper, never pure white and never dark. Pure white reads clinical; dark reads like the terminal we're trying to make un-scary.

## 3. Typography

**Display / Body / Label Font:** The native system stack — `-apple-system, BlinkMacSystemFont, "Segoe UI", system-ui, sans-serif`.
**Mono Font:** `"SF Mono", Menlo, Monaco, monospace`, used only for `code`, file paths, URLs, and prompt boxes.

**Character:** One humanist system sans, working entirely through scale and weight, plus a mono for anything the reader might type or copy. The choice is deliberate: no web fonts means the deck renders instantly and identically on any machine or projector, and the familiar system face feels approachable rather than "designed at" the reader. Hierarchy comes from a strong size jump and heavy display weights, not from font variety.

### Hierarchy
- **Display** (800, 96px on title/closing slides, `-2px` tracking, line-height 1.05): Title-slide and end-slide hero statements only. Currently rendered with a subtle dark `#1a1a1a→#555` clip gradient on the title — see the Don'ts; new slides should prefer solid ink.
- **Headline / h2** (700, 44px, `-1px`, line-height 1.1): The single big idea on each content slide. One per slide.
- **Title / h3** (600, 24px): Sub-section headers within a slide; often set in terracotta-deep.
- **Body / p, li** (400, 22px, line-height 1.5, max ~1100px wide): The reading size. Large on purpose so it survives projection. Sub-list items step down to 18px and muted ink.
- **Label / eyebrow** (400, 14px, uppercase, `3px` tracking, muted): One short kicker per slide naming the section's theme.
- **Mono** (16px): Inline `code`, file paths, URLs, and the larger prompt boxes.

### Named Rules
**The Read-From-The-Back Rule.** Body copy never drops below 18px, and the main idea is 44px+. If a slide needs smaller text to fit, the slide has too much on it — cut content, don't shrink type.

**The One-Idea Rule.** Each slide carries exactly one h2-level idea. Supporting lists, cards, and prompts elaborate it; they never introduce a competing headline.

## 4. Elevation

Mostly flat, with feather-light shadows used only to lift translucent surfaces a half-step off the paper. There is no deep, dramatic elevation anywhere; depth is suggested, never asserted. The warm paper plus translucent white cards already create gentle layering, so shadows stay soft and diffuse.

### Shadow Vocabulary
- **Card lift** (`box-shadow: 0 1px 3px rgba(0,0,0,0.04)`): The default for cards and prompt boxes. Barely-there separation.
- **Image lift** (`box-shadow: 0 6px 24px rgba(0,0,0,0.12)`): For the example screenshots on the title slide, which need to read as physical objects.
- **Nav float** (`box-shadow: 0 4px 12px rgba(0,0,0,0.08)` + `backdrop-filter: blur(10px)`): The one intentional glass moment — the floating bottom nav bar, which sits over slide content and needs to detach from it.
- **CTA glow** (`box-shadow: 0 8px 24px rgba(217,78,31,0.35)`): A colored shadow under the terracotta "Ship it" badge, the single place the deck lets the accent throw light.

### Named Rules
**The Half-Step Rule.** Shadows lift a surface at most a half-step off the paper. The default card shadow is `0 1px 3px rgba(0,0,0,0.04)` — if a shadow is darker or larger than the image-lift value, it's too heavy for this deck.

## 5. Components

### Buttons
- **Shape:** Pill (`30px` radius) for nav controls; soft rectangle (`8px`) for the CTA.
- **Nav buttons:** Transparent with a `1px rgba(0,0,0,0.15)` border, ink text, `6px 14px` padding. Hover fills with `rgba(0,0,0,0.05)`. Live inside the floating bottom nav bar.
- **CTA button** (closing slide): Solid terracotta (`#d94e1f`), paper-white text, `12px 22px`, 700 weight, soft terracotta shadow. The one "press me" affordance in the deck.
- **"Ship it" badge:** A non-interactive emphasis block — terracotta→bright gradient, white uppercase text, heavy CTA glow. Used once, as the payoff at the end of the command-sequence slide.

### Chips / Pills
- **Style:** `rgba(217,78,31,0.12)` background, terracotta-deep text, fully rounded, `4px 12px`, 500 weight. Used inline to tag agent names and short keywords (`code-reviewer`, `security-reviewer`).
- **Label badge:** The solid-terracotta inline `.label` ("PREVIEW", "DEPLOY", "UNDO") — white text on terracotta, `4px` radius, 700 weight — flags categories in the troubleshooting cheat sheet.

### Cards / Containers
- **Corner Style:** `12px` radius (lg).
- **Background:** Translucent white `rgba(255,255,255,0.7)`; accent cards tint with `rgba(217,78,31,0.05–0.06)` and a faint terracotta border.
- **Shadow Strategy:** Card-lift only (`0 1px 3px rgba(0,0,0,0.04)`). See Elevation.
- **Border:** `1px rgba(0,0,0,0.08)` hairline.
- **Internal Padding:** `28px`.
- **Card headings** are set in terracotta-deep.

### Prompt Box (signature component)
The most important custom component: a white panel for copy-pasteable Claude prompts. White background, `1px #e5e0d5` border with a `4px` terracotta left edge, `6px` radius, mono type in terracotta-deep, `16px 20px` padding, card-lift shadow. This is the one deliberate exception to the side-stripe ban: the colored left edge marks "this is a thing you copy and paste" and is a recurring, learnable signal across the deck. (New non-prompt callouts should NOT borrow the left-stripe; it belongs to prompt boxes.)

### Navigation
- **Style:** A floating pill bar fixed bottom-center — translucent white, `blur(10px)` backdrop, hairline border, nav-float shadow. Holds Prev / counter / Next.
- **Progress:** A `3px` terracotta→bright gradient strip fixed to the top edge, width tracking deck position.
- **Keyboard:** Arrow keys / space / PageUp-Down advance; Home / End jump to first / last. Keyboard nav is core and must keep working.

### Flow Steps
Horizontal "You talk → Claude edits → GitHub saves → Vercel publishes" chips: `rgba(217,78,31,0.10)` fill, terracotta border, `10px` radius, separated by large terracotta `→` arrows. Used to show pipelines.

## 6. Do's and Don'ts

### Do:
- **Do** keep the warm paper background (`#fafaf7→#f0ede5`) on every slide. Warm, low-glare, projector-safe.
- **Do** hold to one terracotta accent. Reach for a deeper/lighter terracotta or a transparency before introducing any new hue.
- **Do** set body copy at 22px and the main idea at 44px+. Assume a projector at the back of a room.
- **Do** keep one h2-level idea per slide; let lists, cards, and prompts support it.
- **Do** use the prompt-box component for anything the reader should copy and paste into Claude — it's the deck's "type this" signal.
- **Do** reserve green strictly for "done / new / untracked" meaning, and always pair it with a letter or label, never color alone.
- **Do** keep everything in one self-contained HTML file with the system font stack — instant render, works offline, identical on any machine.
- **Do** keep keyboard navigation and the `prefers-reduced-motion` path working; the deck is driven by arrow keys.

### Don't:
- **Don't** ship corporate slideware — no bullet soup, clip art, or stock gradients. (PRODUCT.md anti-reference.)
- **Don't** use dev-tool dark mode for the decks — no black terminal backgrounds or neon syntax colors. It reinforces the exact fear the class removes. (`agents.html`'s dark theme is a deliberate code-handout exception, not the deck direction.) (PRODUCT.md anti-reference.)
- **Don't** make slides dense or textbook-like — no walls of small text, nothing that can't be read from a projector. (PRODUCT.md anti-reference.)
- **Don't** over-design — no glassmorphism beyond the single nav bar, no gradient text on new slides, no motion for its own sake. (PRODUCT.md anti-reference.)
- **Don't** push body or note text lighter than muted ink `#666666` on the paper; lighter gray drops below AA contrast, and this content gets read on projectors in variable light.
- **Don't** add the terracotta left-stripe to anything other than the prompt box — that stripe is the prompt box's identity.
- **Don't** pull StratEngine brand elements into the deck. The logo appears once at the end as the instructor's day-job product, not as a brand the decks adopt.

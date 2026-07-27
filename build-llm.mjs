#!/usr/bin/env node
/**
 * build-llm.mjs — assembles the "bot view" of each class deck.
 *
 * For every deck listed in DECKS, this reads the deck's index.html, pulls each
 * slide's human-visible content PLUS an optional inline teaching note, and emits
 * a single llm.md next to the deck. That llm.md is what Claude fetches when a
 * student pastes the deck link (a User-Agent rewrite in vercel.json points AI
 * bots at it; humans and Google still get index.html).
 *
 * Source of truth is index.html. Slide content is never authored twice — it is
 * extracted live from the deck on every build. index.html is NEVER modified and
 * carries no private notes, so it stays safe to serve to humans as-is.
 *
 * The teaching notes are authored separately in each deck's teaching.md, one `##`
 * section per slide, keyed by the slide's label (its data-label in index.html).
 * The build matches notes to slides by label and warns about any note whose label
 * matches no slide (the drift catch — e.g. after a label is renamed).
 *
 * Zero dependencies. Run: node build-llm.mjs
 */

import { readFile, writeFile } from 'node:fs/promises';
import { dirname, join } from 'node:path';
import { fileURLToPath } from 'node:url';

const ROOT = dirname(fileURLToPath(import.meta.url));

// The shared teaching contract, prepended verbatim to EVERY deck's llm.md —
// who the student is, the arc, teach-first house rules. Written once; edit it here
// to change the teaching stance across all decks at once.
const PREAMBLE_FILE = 'llm-preamble.md';

// Each deck gets a bot view. `title` names the class; `standing` is the one thing
// that genuinely differs per deck — what the student already has when they arrive.
// Everything universal lives in the shared preamble, NOT here.
const DECKS = [
  {
    dir: 'class-1-website-build',
    title: 'Class 1: How to Build a Website',
    standing:
      'This is the first class. Assume the student has nothing built yet — by the ' +
      'end of it they will have a live website on a real URL. Their tools were ' +
      'installed and logged in during a separate prereqs session.',
  },
];

// ---- tiny HTML helpers (no DOM lib; the decks are hand-authored, regular HTML) ----

/** Strip a leading "cat -n"-style nothing; decode the few entities the decks use. */
function decodeEntities(s) {
  return s
    .replace(/&amp;/g, '&')
    .replace(/&lt;/g, '<')
    .replace(/&gt;/g, '>')
    .replace(/&quot;/g, '"')
    .replace(/&#39;/g, "'")
    .replace(/&nbsp;/g, ' ');
}

/**
 * Turn one slide's inner HTML into readable plain text that PRESERVES structure
 * a bot needs: headings, list items, prompt boxes (marked as executable prompts),
 * and the eyebrow/label. Layout-only wrappers are flattened. This is what grounds
 * Claude in exactly what the student is looking at.
 */
function slideToText(inner) {
  let out = inner;

  // Remove the slide-num marker (it carries the label, handled by the caller).
  out = out.replace(/<div class="slide-num"[^>]*>[\s\S]*?<\/div>/gi, '');

  // Prompt boxes are the load-bearing "type this" component — mark them so the bot
  // knows this is an executable prompt it can run (or adapt) for the student.
  out = out.replace(
    /<div class="prompt-box"[^>]*>([\s\S]*?)<\/div>/gi,
    (_, p) => `\n\n[PROMPT — the exact text the student would paste; you can run or adapt this for their project]\n> ${textOf(p)}\n\n`
  );

  // Eyebrow = the slide's kicker/section label.
  out = out.replace(/<div class="eyebrow"[^>]*>([\s\S]*?)<\/div>/gi, (_, p) => `\n_${textOf(p)}_\n`);

  // Headings.
  out = out.replace(/<h1[^>]*>([\s\S]*?)<\/h1>/gi, (_, p) => `\n\n# ${textOf(p)}\n`);
  out = out.replace(/<h2[^>]*>([\s\S]*?)<\/h2>/gi, (_, p) => `\n\n## ${textOf(p)}\n`);
  out = out.replace(/<h3[^>]*>([\s\S]*?)<\/h3>/gi, (_, p) => `\n\n### ${textOf(p)}\n`);

  // Quote block.
  out = out.replace(/<div class="quote"[^>]*>([\s\S]*?)<\/div>/gi, (_, p) => `\n\n> ${textOf(p)}\n`);

  // List items → bullets (drops the CSS arrow/checkbox; keeps the text).
  out = out.replace(/<li[^>]*>([\s\S]*?)<\/li>/gi, (_, p) => `\n- ${textOf(p)}`);

  // Paragraphs.
  out = out.replace(/<p[^>]*>([\s\S]*?)<\/p>/gi, (_, p) => `\n\n${textOf(p)}\n`);

  // Anything left: strip remaining tags, then decode ONCE, collapse whitespace.
  return tidy(decodeEntities(out.replace(/<[^>]+>/g, ' ')).replace(/[ \t]+/g, ' '));
}

/** Inline text for intermediate passes: strip tags, collapse spaces, but do NOT
 *  decode entities yet. Decoding is deferred to the single final pass in
 *  slideToText, so an escaped &lt;command&gt; survives every intermediate tag-strip
 *  and only becomes <command> at the very end (never re-stripped as a tag). */
function textOf(html) {
  return html.replace(/<[^>]+>/g, ' ').replace(/[ \t]+/g, ' ').trim();
}

function tidy(s) {
  return s
    .replace(/\n{3,}/g, '\n\n')
    .replace(/[ \t]+\n/g, '\n')
    .trim();
}

/**
 * Parse a deck's teaching.md into a Map of { slideLabel -> note text }.
 * Each note is a `## <label>` section; its body runs until the next `##` or EOF.
 * The file's own leading intro paragraph (before the first `##`) is ignored.
 */
function parseTeaching(md) {
  const notes = new Map();
  const sections = md.split(/^##\s+/m).slice(1); // drop the intro before first ##
  for (const sec of sections) {
    const nl = sec.indexOf('\n');
    const label = (nl === -1 ? sec : sec.slice(0, nl)).trim();
    const body = (nl === -1 ? '' : sec.slice(nl + 1)).trim();
    if (label) notes.set(label, body);
  }
  return notes;
}

/** Read a slide's data-label (its human-readable name) from the slide-num div. */
function labelOf(inner) {
  const m = inner.match(/<div class="slide-num"[^>]*data-label="([^"]*)"/i);
  return m ? decodeEntities(m[1]).trim() : '';
}

/** Split the deck body into <section class="slide ...">...</section> blocks. */
function extractSlides(html) {
  const slides = [];
  const re = /<section class="slide[^"]*"[^>]*>([\s\S]*?)<\/section>/gi;
  let m;
  while ((m = re.exec(html)) !== null) slides.push(m[1]);
  return slides;
}

async function buildDeck(deck, preamble) {
  const indexPath = join(ROOT, deck.dir, 'index.html');
  const html = await readFile(indexPath, 'utf8');
  const slides = extractSlides(html);

  // Teaching notes are authored separately, keyed by slide label.
  let notes = new Map();
  try {
    notes = parseTeaching(await readFile(join(ROOT, deck.dir, 'teaching.md'), 'utf8'));
  } catch {
    // No teaching.md — deck emits content only.
  }
  const usedNoteLabels = new Set();

  const parts = [];
  // Generated-file banner: llm.md is build output, never hand-edited.
  parts.push(
    `<!-- GENERATED by build-llm.mjs from index.html + llm-preamble.md — do not edit by hand. -->`
  );
  parts.push(`\n# ${deck.title} — the bot view of this deck\n`);
  if (preamble) parts.push(preamble);
  if (deck.standing) {
    parts.push(`\n## Where this student is right now\n`);
    parts.push(deck.standing);
  }
  parts.push('\n\n---\n');

  slides.forEach((inner, i) => {
    const n = i + 1;
    const label = labelOf(inner);
    const heading = label ? `${n} · ${label}` : `${n}`;
    const content = slideToText(inner);
    const teaching = label && notes.has(label) ? notes.get(label) : null;
    if (teaching) usedNoteLabels.add(label);

    parts.push(`\n## Slide ${heading}\n`);
    parts.push('\n**What the student sees on this slide:**\n');
    parts.push(content ? content : '_(title / transition slide — no body copy)_');
    if (teaching) {
      parts.push('\n\n**Teaching this slide (context the student cannot see — use it to teach, don\'t just recite):**\n');
      parts.push(teaching);
    }
    parts.push('\n');
  });

  const md = tidy(parts.join('\n')) + '\n';
  const outPath = join(ROOT, deck.dir, 'llm.md');
  await writeFile(outPath, md, 'utf8');

  // Drift catch: any note whose label matched no slide is orphaned (likely a
  // renamed or deleted slide). Surface it loudly so it gets fixed.
  const orphans = [...notes.keys()].filter((l) => !usedNoteLabels.has(l));
  console.log(`✓ ${deck.dir}/llm.md — ${slides.length} slides, ${usedNoteLabels.size} with teaching notes`);
  for (const o of orphans) {
    console.warn(`  ! teaching.md note "${o}" matches no slide label in this deck — check for a renamed/removed slide`);
  }
}

let preamble = '';
try {
  preamble = (await readFile(join(ROOT, PREAMBLE_FILE), 'utf8')).trim();
} catch {
  console.warn(`! ${PREAMBLE_FILE} not found — building slides only, no shared preamble.`);
}

for (const deck of DECKS) {
  await buildDeck(deck, preamble);
}

#!/usr/bin/env node
/**
 * build-llm.mjs — assembles the "bot view" of each class deck.
 *
 * For every deck listed in DECKS, this reads the deck's index.html, pulls each
 * slide's human-visible content PLUS its teaching note, and emits a single llm.md
 * next to the deck. That llm.md is what Claude fetches when a student pastes the
 * deck link: a Cloudflare Worker (infra/worker.js) sniffs the User-Agent and does
 * a pass-through fetch of llm.md for AI crawlers, while humans and Google/Bing get
 * the normal index.html at the same URL. (A vercel.json rewrite CANNOT do this —
 * Vercel's filesystem precedence serves index.html before rewrites run — which is
 * why the swap lives in the Worker. See ARCHITECTURE.md, section 2.)
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
 * Full system + how to author/add decks: ARCHITECTURE.md at the repo root.
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
  {
    dir: 'class-1-website-build',
    file: 'prereqs.html',
    out: 'prereqs-llm.md',
    teaching: 'prereqs-teaching.md',
    title: 'Class 1 Prerequisites & Setup',
    standing:
      'This is the BEFORE-CLASS setup deck. The student is installing tools and ' +
      'creating accounts for the first time — they likely have NOTHING working yet, ' +
      'or are mid-setup with something broken. Most often you are being consulted ' +
      'because an install, login, or terminal command did not work. Your job is to ' +
      'get them unstuck without making it worse: read the actual error, fix the real ' +
      'cause, and keep them moving. Assume zero technical background and a fair amount ' +
      'of setup fatigue — this part is a slog and they know it.',
  },
  {
    dir: 'class-2-dashboard-build',
    title: 'Class 2: How to Build a Dashboard',
    standing:
      'The student has completed Class 1 (a live website) and the Class 2 prereqs ' +
      '(Google Analytics connected read-only, an empty Supabase database connected). ' +
      'Today they build a data pipeline (GA → Supabase, scheduled) and a private ' +
      'dashboard on top of it. Two things reliably trip people: (1) they try to ' +
      'design the dashboard before the data pipeline is proven — the deck insists ' +
      'data-first; (2) their analytics may be empty (tag installed late), in which ' +
      'case they build on the sample-data kit instead. Verify data actually landed ' +
      'before trusting anything.',
  },
  {
    dir: 'class-2-dashboard-build',
    file: 'prereqs.html',
    out: 'prereqs-llm.md',
    teaching: 'prereqs-teaching.md',
    title: 'Class 2 Prerequisites & Setup',
    standing:
      'BEFORE-CLASS setup for the dashboard class. Three setup jobs: install a ' +
      'Google Analytics tag on their site (needs ~7 days of data before class), ' +
      'connect Claude read-only to that analytics, and create a free Supabase ' +
      'database + connect Claude to it. You are usually consulted because one of ' +
      'these broke. The single biggest gotcha is the Supabase MCP RESTART: Claude ' +
      'Code must restart mid-setup, and the student must return to the SAME chat via ' +
      'the history (clock) icon, not start a new one. Also: analytics data can take ' +
      'up to ~48h to appear — empty ≠ broken. Read the actual error, fix the real ' +
      'cause, reassure through the slog.',
  },
  {
    dir: 'class-3-seo-geo',
    title: 'Class 3: SEO + GEO (getting found by search and AI)',
    standing:
      'The student has a live site (Class 1) and a dashboard (Class 2), and the ' +
      'Class 3 prereqs done (domain on Cloudflare, Claude armed with Cloudflare ' +
      'skills + logged in). Today they build the dual-web setup: a clean AI-only ' +
      'version of their site plus a Cloudflare Worker that serves it to AI crawlers ' +
      'while humans and Google get the normal site. This is a plan-mode build driven ' +
      'by one big prompt. The cloaking-safety rule is load-bearing: Google/Bing MUST ' +
      'get the human page, never the bot version. Known gotchas: Cloudflare blocks ' +
      'AI crawlers by default (AI Crawl Control), and the Worker must bind by ROUTE ' +
      'not custom_domain.',
  },
  {
    dir: 'class-3-seo-geo',
    file: 'prereqs.html',
    out: 'prereqs-llm.md',
    teaching: 'prereqs-teaching.md',
    title: 'Class 3 Prerequisites & Setup',
    standing:
      'BEFORE-CLASS setup for the SEO+GEO class. Two jobs: move their domain onto ' +
      'Cloudflare (up to a day to go Active — needs ~7 days lead time), and arm ' +
      'Claude with Cloudflare skills + a logged-in terminal. You are usually ' +
      'consulted because the domain move stalled or the login broke. The #1 known ' +
      'gotcha: right after moving to Cloudflare a site can break into a redirect ' +
      'loop or SSL error — the fix is almost always setting Cloudflare SSL/TLS mode ' +
      'to Full (strict). Also: the Cloudflare setup has a Claude Code RESTART where ' +
      'the student must resume the SAME chat via the history icon (same as Class 2). ' +
      'Path A owns a domain (flip nameservers); Path B buys one inside Cloudflare ' +
      '(instant, no wait).',
  },
  {
    dir: 'aivisibility',
    title: "Lightning Lesson: Audit Your Website's AI Visibility with Claude Code",
    standing:
      'A FREE 45-minute standalone Maven lightning lesson, not part of the paid ' +
      'series. Assume the attendee has NOTHING installed except the Claude desktop ' +
      'app on a paid plan. No terminal, no VS Code, no GitHub, no repo, no website ' +
      'project. They install the claude-seo plugin entirely through the desktop ' +
      "Plugins UI (Add marketplace -> Add from a repository -> AgriciDaniel/claude-seo " +
      '-> Sync -> install; no restart needed) and run ONE command, `/seo geo ' +
      'yourdomain.com`, against their own site. Two gotchas dominate: (1) it MUST be ' +
      'the Code tab, not Chat or Cowork, because the plugin fails to sync in Cowork; ' +
      '(2) a red "not made by Anthropic" warning appears during install and is ' +
      'expected and correct. The run takes several minutes and nothing waits on it. ' +
      'The teaching (SEO vs GEO, what you control vs what you do not, being the ' +
      'answer, the readable-twin idea) is the spine; the audit is the proof. Close ' +
      'routes to a WAITLIST for a course opening early October, not to enrollment.',
  },
  {
    dir: 'class-4-automations',
    title: 'Class 4: Automations',
    standing:
      'The student has completed Classes 1-3 (live site, dashboard, dual-web). ' +
      'Today they build a "morning briefing" — a Python script on their own ' +
      'computer that reads a few sources (email/calendar/tasks/Slack/etc, all ' +
      'read-only), asks Claude to judge what matters, and writes one brief, on a ' +
      'schedule. NEW territory this class: API keys and .env files. The critical ' +
      'safety rule: secrets go in .env (never in the Claude chat, never to GitHub ' +
      'via .gitignore) — the student pastes the real key into the .env file ' +
      'themselves. Also teach the deterministic-vs-judgment split (do everything ' +
      'possible with fixed rules, call Claude only for the "what matters" step) and ' +
      'the laptop catch-up check (a missed scheduled run fires on next wake).',
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
  // A deck usually is <dir>/index.html → <dir>/llm.md with notes in <dir>/teaching.md.
  // A secondary deck in the same folder (e.g. prereqs) overrides file/out/teaching.
  const srcFile = deck.file || 'index.html';
  const outFile = deck.out || 'llm.md';
  const teachingFile = deck.teaching || 'teaching.md';

  const indexPath = join(ROOT, deck.dir, srcFile);
  const html = await readFile(indexPath, 'utf8');
  const slides = extractSlides(html);

  // Teaching notes are authored separately, keyed by slide label.
  let notes = new Map();
  try {
    notes = parseTeaching(await readFile(join(ROOT, deck.dir, teachingFile), 'utf8'));
  } catch {
    // No teaching file — deck emits content only.
  }
  const usedNoteLabels = new Set();

  const parts = [];
  // Generated-file banner: this is build output, never hand-edited.
  parts.push(
    `<!-- GENERATED by build-llm.mjs from ${srcFile} + ${teachingFile} + llm-preamble.md — do not edit by hand. -->`
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
  const outPath = join(ROOT, deck.dir, outFile);
  await writeFile(outPath, md, 'utf8');

  // Drift catch: any note whose label matched no slide is orphaned (likely a
  // renamed or deleted slide). Surface it loudly so it gets fixed.
  const orphans = [...notes.keys()].filter((l) => !usedNoteLabels.has(l));
  console.log(`✓ ${deck.dir}/${outFile} — ${slides.length} slides, ${usedNoteLabels.size} with teaching notes`);
  for (const o of orphans) {
    console.warn(`  ! ${teachingFile} note "${o}" matches no slide label in this deck — check for a renamed/removed slide`);
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

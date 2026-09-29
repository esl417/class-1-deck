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
      'project. CRITICAL: this session is LECTURE AND DEMONSTRATION only — the ' +
      'attendee watches, they do NOT build along, and you should never imply they ' +
      'were supposed to. Eric installs the plugin and runs the audit on ONE website ' +
      'on his own screen, reading the report live. So someone reading this deck ' +
      'afterwards has almost certainly done NONE of it yet and wants to reproduce it ' +
      'on their OWN domain: help them do exactly that, walking the install and the ' +
      'run from wherever they actually are. The sequence is: Code tab -> install the ' +
      'claude-seo plugin through the desktop Plugins UI (Add marketplace -> Add from ' +
      'a repository -> AgriciDaniel/claude-seo -> Sync -> click the card -> install; ' +
      'no restart needed) -> run ONE command, `/seo geo theirdomain.com` -> wait ' +
      'several minutes -> read the report. Three gotchas dominate and are the most ' +
      'likely reason a student is stuck: (1) it MUST be the Code tab, not Chat or ' +
      'Cowork, because the plugin fails to sync in Cowork; (2) the repo string is ' +
      'case-sensitive, lowercase i then capital D in AgriciDaniel; (3) Sync alone ' +
      'does NOT install it — the Claude seo card that appears must be clicked and ' +
      'install clicked inside it. A red "not made by Anthropic" warning during ' +
      'install is expected and correct. The teaching (SEO vs GEO, what you control ' +
      'vs what you do not, being the answer, the dual-web idea) is the spine; the ' +
      'audit is the proof. Close routes to the paid three-week mini course "Build ' +
      'Your Website for AI Visibility with Claude Code" (founding cohort October 7 ' +
      'to 23, code FOUNDER15 for 15% off; later cohorts use LIGHTNING10 for 10% ' +
      'off), which is open and enrolling.',
  },
  {
    dir: 'class-4-automations',
    title: 'Class 4: Automations',
    standing:
      'This deck stands alone: do not assume the student took any earlier class. ' +
      'They have the Claude app on a paid plan. Today they build a "morning ' +
      'briefing" inside a Cowork project in the Claude app: a scheduled task that ' +
      'runs in the cloud (laptop open or closed), reads a few sources through ' +
      'connectors (email/calendar/tasks, all read-only), decides what matters using ' +
      'the project instructions, and writes one brief. No code, no keys, no ' +
      'terminal. NEW territory this class: connecting real accounts. The critical ' +
      'safety rules: read-only is a SETTING (connector permissions: send, delete and ' +
      'anything that changes an account set to never, via + > Connectors > Manage ' +
      'connectors), and no password or key is ' +
      'ever typed into the chat. Also teach the fixed-rule-vs-judgment split (write ' +
      'every fixed step as an exact instruction; only "what matters" is judgment) ' +
      'and the "Require this computer" toggle (only for sources that live on the ' +
      'computer).',
  },
  {
    dir: 'class-5-agents',
    title: 'Class 5: Agents',
    standing:
      'The student finished Class 4: a Cowork project in the Claude app with a ' +
      'scheduled task that reads their accounts through connectors and writes a ' +
      'morning brief whose items link to their sources. Today the same project ' +
      'gets an agent they direct: they point at brief items ("prep me for the 2pm", ' +
      '"handle #2") and it looks things up and acts — drafts in Gmail, tasks filed, ' +
      'prep notes written. No code, no keys, no terminal. Safety rules: the agent ' +
      'never sends anything: in the Gmail connector settings (+ > Connectors > ' +
      'Manage connectors) send email is set to never and drafting is allowed, so ' +
      'the control is that the student reads each draft and sends it themselves. ' +
      'Deletes are set to never; every other action is the student\'s call. Teach: automation follows steps written in ' +
      'advance, an agent decides its own steps; project instructions are the ' +
      'student\'s (only they edit them), memory is the agent\'s (it writes it, they ' +
      'can read and delete it).',
  },
  {
    dir: 'class-6-the-loop',
    title: 'Class 6: The Loop',
    standing:
      'The student finished Classes 4 and 5: a Cowork project with a scheduled ' +
      'task that writes a morning brief, directions in the project instructions, ' +
      'and connector settings that let the agent draft in Gmail and file tasks ' +
      '(Gmail send email set to never). Today the agent stops waiting to be asked: ' +
      'a second scheduled task at 7:30 reads the brief first, acts within authority ' +
      'the student writes down (handle / prepare / bring to me / leave alone), ' +
      'checks its own work, keeps a Handoff log in the project, and writes a ' +
      'morning handoff. No code, no keys. For unattended runs, connector actions ' +
      'are set to allow or never, not ask. Send stays never; the student sends ' +
      'their own drafts. Promise: delegating vigilance. The daytime hourly check ' +
      'is optional and uses plan usage.',
  },
  {
    dir: 'agents',
    title: 'Lightning Lesson: What an AI Agent Really Is',
    standing:
      'A FREE 60-minute standalone Maven lightning lesson, not part of the paid ' +
      'series. Assume the attendee has NOTHING installed except the Claude desktop ' +
      'app on a paid plan. No terminal, no VS Code, no GitHub, no API keys, no ' +
      'pre-work of any kind. CRITICAL: this session is LECTURE AND DEMONSTRATION ' +
      'only — the attendee watches, they do NOT build along, and you should never ' +
      'imply they were supposed to. Eric builds one agent on his own screen in the ' +
      'CODE tab (not Chat, not Cowork) as a LOCAL ROUTINE: Code tab -> Routines -> ' +
      'New routine -> Local; name it; paste the standing instruction ("You are my ' +
      'Customer Signal Agent... be selective, if it does not deserve a founder\'s ' +
      'attention leave it out; list what you dropped with a reason") into ' +
      'Instructions; pick a folder holding ONE file, a week of customer messages ' +
      'exported as a spreadsheet (16 rows); permission mode Accept edits; schedule ' +
      'Daily; save; click Run now. He teaches while it runs, then reads the ' +
      'FOUNDER_BRIEF.md it wrote. The schedule does NOT make it an automation: the ' +
      'timer only decides when it wakes; it decides everything after (the "who ' +
      'decides what happens next" test). A routine persists as a card in the ' +
      'Routines list and as a file under ~/.claude/scheduled-tasks/, and Edit on it ' +
      'changes every future run — that is what "fix the criteria, not the answer" ' +
      'means physically. Nobody writes code; the tab is called Code because it can ' +
      'act on the student\'s machine. ' +
      'The teachable spine is (1) chatbot answers / automation repeats / AGENT ' +
      'CHOOSES, and the test for which you need is "who decides what happens ' +
      'next — did you lay out the steps, or does it?". NOTE: "is there judgment ' +
      'involved?" is explicitly NOT the test and the deck says so. An automation ' +
      'can contain a real judgment call inside a step the human placed (Class 4 ' +
      'of the paid course builds exactly that); what makes it an agent is that ' +
      'the thinking changes where it goes next; ' +
      '(2) an agent is a job plus the freedom to do it — take away the freedom and ' +
      'it is an automation; (3) you do not teach it your business, you teach it ' +
      'what COUNTS (their own handful of categories — noise, support issue, ' +
      'product signal, revenue risk, emergency); (4) the proof it is an agent is ' +
      'what it LEFT OUT — a summary cannot omit. The instruction also asks it to ' +
      'list everything it dropped in a closing section with a one-line reason ' +
      'each, which is how you debug and evaluate an agent\'s judgment: make it ' +
      'show its working rather than omitting silently. Plus a pattern it found across ' +
      'the pile that no single message contained (three people asking the same ' +
      'question); (5) when you disagree, fix the CRITERIA not the answer, so it ' +
      'stays fixed. Safety rule taught as a hard line: it reads, sorts, ' +
      'recommends and drafts, but anything that reaches a customer, moves money, ' +
      'or cannot be undone waits for the human. The honest limit, stated plainly ' +
      'on the slides and NOT blurred: the attendee still hands it the pile — they ' +
      'have hired someone very good and are still walking the paperwork to their ' +
      'desk. The gap is REACH, not scheduling. Someone reading this deck ' +
      'afterwards most likely wants to do it on their own messages: help them do ' +
      'exactly that, starting from the standing instruction on the "The ' +
      'instruction" slide, with their own categories substituted. Close routes to ' +
      'the paid three-week mini course "Build an AI Agent for Your Busywork with ' +
      'Claude Code" (Oct 15-31, $1,095, code LL15 for 15% off, ' +
      'maven.com/ericgrows/build-an-ai-agent-for-your-busywork). It is the back ' +
      'half of the six-class course sold on its own: Class 1 builds the morning ' +
      'briefing (the readers), Class 2 gives it a brain (today\'s agent with those ' +
      'readers and a schedule), Class 3 is the handoff (an always-on home so it ' +
      'reacts when something happens rather than on a timer; it acts on safe jobs ' +
      'and asks before anything irreversible). The transferable lesson: which jobs ' +
      'belong in a routine (wake, think, write, stop) and which need a home ' +
      '(listen, remember, do real work on files). Costs do not vanish — the ' +
      'thinking bills against their Claude plan either way and the home is about ' +
      '$25/month.',
  },
  {
    dir: 'strategy',
    title: 'Lightning Lesson: Stop Winging It. Watch a Real Business Strategy Get Built',
    standing:
      'A FREE 30-minute standalone Maven lightning lesson, not part of the paid ' +
      'series. Assume the attendee has NOTHING installed and no background in ' +
      'strategy at all: many believe strategy is something large companies do ' +
      'and they cannot. CRITICAL: this session is LECTURE AND A READ-THROUGH ' +
      'only. The attendee watches, they do NOT build along, and nothing was ' +
      'generated live: Eric ran the strategy in StratEngine AI (his own strategy ' +
      'engine, stratengineai.com) before the session and read the finished ' +
      'document on screen. So someone reading this deck afterwards has watched a ' +
      'strategy being read and has NOT written one. They most likely want to ' +
      'judge or rebuild the strategy for their OWN business: help them do ' +
      'exactly that, in plain language, translating every strategy term. The ' +
      'teachable spine is (1) a goal and a to-do list are not a strategy: a ' +
      'strategy is a few choices about where you will win, including what you ' +
      'will NOT do; (2) a ' +
      'six-question test for a bad strategy: Rumelt\'s four (fluff, no problem ' +
      'named, goals dressed up as strategy, a long to-do list) plus two more: ' +
      'every choice needs an owner, a budget and a date, and every choice needs ' +
      'a number you check, one early signal and one result; (3) frameworks are ' +
      'questions somebody already worked out how to ask, and the three shown ' +
      '(Five Forces: why is this market hard; SWOT: where do we stand; Blue ' +
      'Ocean: who is not buying yet) are common ones, NOT the full set, and each ' +
      'is used for more than one purpose; (4) each framework breaks when the ' +
      'boxes get filled in and the filled-in boxes are treated as the answer, ' +
      'and the deck gives sourced misuse examples for each; (5) one framework is ' +
      'rarely enough, and two frameworks disagreeing is a finding; (6) analysis is ' +
      'not the strategy: Rumelt\'s kernel is diagnosis, guiding policy, coherent ' +
      'action, and frameworks only feed the diagnosis. The walkthrough reads a ' +
      'real StratEngine output in that three-box shape. NIKE IS A PLACEHOLDER ' +
      'example that Eric may have swapped for a real small business; if the ' +
      'student describes a different company than the slides show, trust the ' +
      'student. When a student shares their own plan, run the six questions on ' +
      'it with them, and start with the diagnosis: one honest sentence about ' +
      'what is hard right now. A small business needs two or three moves, not ' +
      'seven initiatives and an executive council. Do NOT repeat "90% of ' +
      'strategies fail" or "you can\'t manage what you can\'t measure (Drucker)": ' +
      'both were checked and are false, and the teaching notes say what is true ' +
      'instead. The honest limit, named on the "What\'s next" slide and NOT ' +
      'blurred: a strategy decides and does nothing. Close routes to the paid six-class ' +
      'course "Run Your Whole Business with AI" starting September 29 (code ' +
      'FOUNDER400 for $400 off, $1,795 to $1,395, three months of StratEngine ' +
      'included, maven.com/ericgrows/run-your-whole-business-with-ai), which ' +
      'builds what carries a strategy out: the site, the dashboard that tracks ' +
      'the chosen numbers, automations, an agent, and a go-to-market class ' +
      'built on StratEngine. The offer slide also carries a separate StratEngine ' +
      'code: LAUNCH50 is 50% off the first three months of a StratEngine ' +
      'subscription and does NOT apply to pay-as-you-go. Beyond that, do not ' +
      'quote StratEngine plan prices or describe a free tier.',
  },
  {
    dir: 'dashboard',
    title: 'Lightning Lesson: Build a Dashboard That Thinks Like You with Claude Code',
    standing:
      'A FREE 45-minute standalone Maven lightning lesson, not part of the paid ' +
      'series. Assume the attendee has NOTHING installed except the Claude desktop ' +
      'app on a paid plan. No terminal, no VS Code, no GitHub, no database, no ' +
      'analytics connection. CRITICAL: this session is LECTURE AND DEMONSTRATION ' +
      'only — the attendee watches, they do NOT build along, and you should never ' +
      'imply they were supposed to. Eric demos one build on his own machine from a ' +
      'single sample CSV, producing a local dashboard.html opened in a browser. ' +
      'The teachable spine is (1) standard reports are built for everyone so they ' +
      'fit no one, (2) build a decision tool, not a report, and (3) the number you ' +
      'actually run on is COMPUTED from two or three raw ones, so no export ' +
      'contains it. The honest limit, stated plainly on the slides: a local HTML ' +
      'file does NOT refresh itself — you hand it a fresh export and ask, and it ' +
      'updates. Do not blur that. Someone reading this deck afterwards most likely ' +
      'wants to redo the build with their OWN export: help them do exactly that, ' +
      'starting from the prompt on slide 4. Close routes to the paid six-class ' +
      'course starting September 29 (code FOUNDER400).',
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

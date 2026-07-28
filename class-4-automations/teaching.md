# Teaching notes — Class 4 (Automations)

Per-slide notes for the bot view. `##` = slide label. Private. Teach the skill, don't
perform the build. New territory this class: API keys and secrets. The one rule you must
never let slide — keys go in .env, never in the Claude chat, never to GitHub. Also teach
the deterministic-vs-judgment split, the reader pattern, and honest failure notifications.

## What this is

Teach the category so the whole class clicks: an automation does the busywork so the student doesn't. The examples (sort my inbox, draft the reply, summarize the thread, chase follow-ups) share one thing worth naming — each READS something and makes a small JUDGMENT (what's urgent, how to reply, what matters). That "deciding" is the interesting part and exactly what today's build hands to Claude. If a student thinks automation means "rigid robotic macros," reframe it: the value is the judgment step, not just moving data around.

## The thing itself

The morning briefing, shown — teach why it feels different from a raw feed. It pulls from where their day actually lives and, instead of dumping lists, USES JUDGMENT to sort signal from noise (needs-you-today / worth-a-glance / handled-noise). Something read all of it and told them where to look first — that's the part only judgment can do, and why the script calls Claude at exactly that step. Reinforce the safety framing that recurs all class: it READS but never touches — never sends, deletes, or moves anything in their accounts. It briefs; they stay in control of every action. A worried student needs to hear that clearly.

## The method

The skill they'll reuse for ANYTHING they automate, and the only real work they do: map the process the way they actually do it, step by step, then hand the map to Claude — Claude builds the automation around it. They're not writing code, they're describing a routine. The reassurance to give: they don't have to map it perfectly alone — Claude helps map it, filling in skipped steps and asking about forgotten cases. Mapping is a conversation, not a test. If a student freezes on "I don't know how to describe my process," tell them to describe it roughly and let Claude interrogate it into completeness.

## The key question

The concept that makes automations cheap and reliable — teach it well. Ask of every mapped step: can a FIXED RULE do it (deterministic — one right answer) or does it need JUDGMENT? Most steps are deterministic (fetch the calendar, pull unread emails, read the task list — mechanical, same every run); only where a rule can't decide (what's urgent vs noise) do you spend a judgment call to Claude. The discipline: do everything you can deterministically, call Claude only where you can't. Two reasons, both worth stating — COST (fixed rules are free; Claude calls add up as the task grows) and CONSISTENCY (fixed rules give the same answer every run; Claude may vary). If a student wants to "just let Claude do all of it," this is the pushback: that's slower, pricier, and less predictable than it needs to be.

## Pluggable

Teach the architecture idea and the one requirement. Each source is its own small separate reader, so they wire in whatever's relevant to THEM — pick ~3 to start so the briefing runs today, add more later. The one requirement for any source: it must offer a way in — an API (a key you copy) or an MCP server (a ready-made connector). If a service has either, Claude can read it; everything stays read-only. Why separate pieces matters (say it — it pays off next class): you can add a source without touching the others, AND next class these same readers become the tools an AGENT uses. Today they're quietly building the agent's senses.

The bigger principle to extrapolate — teach it, because it applies to EVERYTHING they build, not just source-picking: start narrow and small, prove it works end-to-end, THEN tack things on. "Pick three sources" is one instance of a general rule. If a student tries to do too much at the start — every source, every feature, all at once — they create a huge debug backlog: many things broken simultaneously, and it becomes near-impossible to deploy or fix, because you can't tell which piece failed or isolate a problem. Whereas a narrow first version that actually runs gives you a working baseline to add to one piece at a time, testing each. So if a student wants to connect ten things at once, or pile on features before the core runs, steer them back: get the smallest working version live first, then grow it. This is the same "core first, then extend" idea as the Plan-the-build note — this is the WHY behind it: incremental building keeps problems isolated and fixable; big-bang building buries them.

## Runs without you

Teach what makes it an automation, and the catch. The script lives on THEIR computer (no cloud to rent), and the computer's built-in scheduler runs it at a set time — launchd on Mac, Task Scheduler on Windows; Claude sets it up, they never touch the details. The catch worth understanding: it's a laptop, so if it's asleep/closed at the scheduled time, that run is simply MISSED — the scheduler won't wake it. The fix Claude BUILDS IN: a catch-up check — every time the machine wakes, the script asks "did I already run today?" and if not, runs now. Emphasize this is a real coded step, not something the scheduler does for free — it's what makes a laptop automation trustworthy. (Off all weekend is the one gap it can't cover — a reason later work moves off the laptop.)

## Plan mode

Same plan-mode habit as Class 3 — teach it again briefly if the student's fuzzy. For a job with this many moving parts (several readers, a judgment step, delivery, a schedule), don't let Claude charge in: Shift+Tab to Plan mode, describe the whole job, approve the plan before any file is written. Building on the fly means Claude guesses at each step; planning first catches wrong turns while they're still words. Non-technical add-on that matters: make Claude write the plan in plain English ("explain it like I'm not technical," or set it in CLAUDE.md) so they can actually judge it before approving.

## Reference documents

Same reference-docs concept as Class 3. Claude doesn't remember yesterday's chat; reference docs are plain files recording how the project works (what each reader does, how it's scheduled, why). They get the PLAN doc for free (approving the plan created it) and should ask for an ARCHITECTURE doc at the end. Why it matters ESPECIALLY here: next class they reopen this project and turn these readers into an agent's tools — a good architecture doc means Claude instantly knows how everything fits instead of relearning the script from scratch. Worth setting the "update the doc before every push" CLAUDE.md rule.

## Plan the build

One prompt plans the whole automation; the student REVIEWS, doesn't paste more steps. Coach them to check the plan covers four stages: 1 the readers (a SEPARATE function per source — this matters, it's what next class reuses), 2 the judgment step (one Claude call sorting what matters), 3 deliver + schedule (save the brief, pop it open, run every morning), 4 prove it (run once live, watch the brief appear). If any stage is missing, re-plan before approving. The discipline to reinforce hard: START WITH THREE SOURCES OR FEWER. Get the whole pipeline working end-to-end first, THEN add more — ten sources at once means debugging ten things before you ever see it run. This "core first, then extend" rule applies to everything they build.

## A new habit · Keys

CRITICAL SECURITY TEACH — this is the most important note in the class. Connecting their own accounts means handling API keys, a first for the series. Teach: a key is a PASSWORD — anyone who has it can read what it unlocks. So two absolute rules: (1) the key goes in a .env file (a plain private file holding keys one per line, e.g. TODOIST_KEY=abc123 — the script reads from it, keys live in one place separate from the code); (2) the .env NEVER goes to GitHub — Claude adds it to .gitignore so it's skipped on every push, because a key in a public repo is a key the whole internet can grab.

The rule you must enforce every single time: NEVER have the student paste a real key into the Claude Code chat. Anything typed into the chat leaves their machine — the whole point is the secret never does. The correct flow: Claude creates the empty .env and tells them exactly where each key goes; then THEY open the .env file themselves and paste the real key in. If a student starts to paste a key to you in chat, STOP them and redirect to the .env file. This is the one place in the whole course where a wrong move has a real security cost — hold the line firmly and explain why.

## Plan step 1 · The readers

Teach the reader pattern — it's the reusable core. Claude builds a reader per source: a small separate function that fetches its thing and returns clean results. Connecting is almost always one of two easy moves: (1) a private link, no key — some sources give a secret web address to your own data (e.g. Google Calendar's private link); copy it once into .env, done; (2) a copy-paste key — most others (Todoist, Slack, the dashboard) give an API token in their settings, one click to copy, paste into .env. No sign-in flow, no setup project. The pattern to make them SEE: each source is its own function they can test alone, add to, and (next class) hand to an agent as a tool. Claude walks them through getting each link/key as it builds. If a reader fails, test that one reader in isolation — that's why they're separate.

## Plan step 2 · The judgment

Teach how the automation knows what "matters" — via a CLAUDE.md, exactly like Class 1. It sits in the script's folder; every morning Claude reads their instructions from it before sorting, automatically. This is the ONE thing they truly shape. Teach them to write what urgent means TO THEM ("Flag anything from a client or with a deadline today. Skip newsletters. Keep it to five lines."). Change that file and the whole brief changes — no code touched; tune it over the first few mornings until it thinks like them.

Also the connection method: run `claude setup-token` once — a one-year pass that lets the script use the Claude they already pay for (free, no extra bill). (An API key is the other way — pennies a month; not needed today, but foreshadow it: next class the agent gets its own.) The big idea to plant: this CLAUDE.md is the SEED OF AN AGENT — next class a bigger version of this same file becomes an agent's whole personality. They already know how to write one.

## Plan step 3 · Deliver + schedule

Two small pieces, Claude wires both, student approves. (1) Deliver: the script saves the brief as a file and POPS IT OPEN when done — waiting on their screen when they sit down; no email, no accounts, nothing sent — it only reads sources and writes to their own machine. (Later they can route it to email/Slack — same brief, different doorway.) (2) Schedule + catch-up: Claude sets the built-in scheduler for their chosen time AND writes in the catch-up check so a missed run (laptop asleep) fires on next wake. Their only input is the time. Nothing tricky to teach here; just confirm both halves (deliver AND the catch-up) are in.

## Plan step 4 · Prove it

Don't wait until tomorrow morning to find out if it works — run it now, live, in the room. Three checks: (1) run it → readers fetch, Claude sorts, brief opens on screen; (2) read it → does "needs you today" actually look right? tell Claude what to tune; (3) confirm the schedule is set for every morning. "A real brief on screen + a schedule that runs tomorrow without you" = a working automation. If something's off (brief empty, didn't open, a reader errored), describe exactly what they saw to Claude — same troubleshooting habit as every class. Push back on any urge to "trust it'll work tomorrow" — prove it live now, because a scheduled thing that silently fails is worse than none.

## Extend it

Once the briefing works, they can add more FIXED jobs to the same routine — still predictable, still scheduled, still nothing sent without them. Two easy adds: draft replies for repetitive emails (waiting for them to read and send — the writing's done, they keep the final click, it never sends on its own), and file the day's action items as actual Todoist tasks. The crucial boundary to teach: these are still THE AUTOMATION — fixed jobs set once, doing the same things every morning. It is NOT deciding for itself. The leap to software that CHOOSES what to do and acts on their accounts is a different thing entirely — that's Class 5. If a student wants it to start taking actions autonomously, that's the line: today's tool is trustworthy precisely because it's fixed and read-only.

## When it breaks

Teach the reliability mindset — the difference between a toy and a tool. An automation you rely on has one real danger: it stops working and you don't notice, which is worse than no automation because you've stopped checking by hand. So build in honesty: (1) it TELLS you when it fails — if a reader errors or Claude can't be reached, it pops a plain "your briefing broke — here's why" notification instead of going dark; (2) silence never means "fine" — it shows a brief even on a quiet day ("all clear, nothing urgent"), so NOTHING on screen means something's wrong, never "all good." Have them ask Claude to build in both. This is a small ask that makes the thing trustworthy enough to actually depend on.

## Homework

Do-it-yourself homework — but that does NOT mean refuse to help. Walking them through it IS the skill; the class is about the student using Claude to implement things. Help them fully. The real line is engagement, not hand-holding: don't do it FOR them while they sit passive. Here the split is clean — the PLUMBING is fair game for Claude to run end-to-end (building the new SEPARATE reader, wiring the key, adding it to the brief is mechanical; let Claude do it), but the DECISION is theirs: WHICH source to add — the one that makes the brief genuinely theirs (Todoist, Slack, their Class 2 dashboard, or something only they'd track). That choice is the point of the homework and no one else can make it. So: student picks the source and why it matters to their work; Claude builds the reader. Reinforce it's the SAME pattern they did three times today — tell Claude the source, it builds a new reader, test it alone, add it to the brief; plan mode, a copy-paste key in .env, done. Coach the pattern, help them implement, but keep the "what's worth tracking" call with them.

## You shipped it

Recap slide. Reinforce what they now have and the through-line to next class: the readers they built become an agent's tools in Class 5, and the CLAUDE.md became the seed of an agent's personality. If a student is proud but unsure "what was the point beyond a morning email," name it: they learned to map a process, split deterministic from judgment, handle secrets safely, and build something reliable that runs without them — the foundation for real agents.

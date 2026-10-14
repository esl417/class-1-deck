# Teaching notes — Advanced Class 3 Prerequisites

Per-slide notes for the bot view of the Advanced Class 3 PREREQS deck, adapted from the
website course's Class 1 prereqs. Each `##` heading is a slide's label (its data-label in prereqs.html).
Kept private — never served on the human deck. The student is on the Advanced track: they
built in Claude Managed Agents in Classes 1 and 2 but may never have used Claude Code, a
terminal, or GitHub. Class 3 installs OpenClaw with Claude Code in Claude's desktop app, so
this setup covers the desktop app, git, Node.js, GitHub, and the ant CLI only (no Vercel, no
Impeccable). If they already did the website course setup (before the course moved to the desktop app), they need
the Claude desktop app and Project folder slides, then the install prompt (for the ant CLI),
the login prompt, and the Terminal check.

These notes are **recovery-focused**, not concept-focused. A student reading prereqs is
setting up for the first time; when they consult you, it's usually because an install,
login, or terminal command didn't work. Default posture: read the actual error, fix the
real cause, keep them moving, and reassure — this stage is a slog and they know it.

## Before we start

Nothing technical here — it's a morale slide ("this part is a drag, you only do it once"). The teaching value is emotional, not procedural: if a student reaches you here they may be dreading the setup. Match the slide's honesty. Confirm that yes, this part is tedious and one-time, that scrolling terminal text is normal, and that you'll handle the heavy lifting. Don't oversell it as easy — validate that it's a slog, then get them moving.

## Overview

Two tools, not three: Claude Code (in Claude's desktop app) and GitHub. Vercel is not part of Class 3 (hosting in the cloud is explained at the end of class, with nothing to set up now). If the student already completed the website course prereqs, most of it is installed, but they set it up before the course moved to the desktop app: they do the Claude desktop app and Project folder slides, then the install prompt (it adds only the missing ant CLI), the login prompt, and the Terminal check. Agents, CLAUDE.md and permissions carry over.

## Claude desktop app

Two failure modes here, both common:

1. **They're in the Chat tab, not Code.** The desktop app opens on Chat, which can't touch files on their computer. If Claude says it can't see or edit their files, check that they clicked the **Code** tab.

2. **Free Claude account.** This needs a PAID plan (Pro or Max) — the free account will not work, and the failure is confusing because sign-in appears to succeed but the Code tab won't work. If a student is signed in but Code won't function, verify they're on a paid plan at claude.ai before debugging anything else. This is the single most common "it just won't work" cause at this step.

## Project folder

The one real stuck-point: **Select folder → make a NEW folder, then open it.** Students routinely skip creating a fresh folder and instead pick their Desktop, their Documents, or nothing at all — then everything downstream (the repo, the agent's files) is a mess. If a student seems lost about "where their project is," check this first: is the session open on a dedicated, empty folder? If not, have them start a new session (⌘N / Ctrl+N) on a fresh folder before anything else.

Also: they should switch to Opus (click the model name next to the Send button — it may say Sonnet — and pick Opus). If their answers later feel weak, this is worth re-checking.

## Prerequisites

This is the biggest failure surface in the entire prereqs deck — one prompt installs git, Node.js (current LTS; OpenClaw runs on it), the GitHub CLI, and Anthropic's ant CLI (Mac: `brew install anthropics/tap/ant`; in class Claude uses it to download the Class 2 agent from the Console as files), across Mac or Windows. When a student consults you here, something in that chain broke. Approach:

**Read the actual error — don't guess.** Have them paste exactly what the terminal shows. The fix depends entirely on which tool failed and why.

**The one thing only the student can do: type their Mac password.** When an install needs `sudo`, the terminal waits for their Mac password, and the screen stays completely blank as they type — no dots, no stars. Non-technical students think it's frozen or broken. It isn't. Tell them: type your password blind and press Enter. This trips up almost everyone.

**Scrolling text is an install working, not an error.** Reassure them they never need to read it — that's your job. Panic at scrolling output is common and misplaced.

**Failures are usually order/dependency issues.** On Mac, Homebrew must exist before the rest; on Windows, winget (App Installer) must exist and Git for Windows is required (Claude Code runs commands through Bash). If one tool failed, install the missing dependency first, then retry that one tool — don't restart the whole prompt.

When something fails, the move is: fix that one thing, then continue from where it stopped — not start over.

## What GitHub is

Concept slide — teach it if asked, don't drill it. The analogy on the slide is the right one: GitHub is Google Drive / Dropbox for code — a cloud backup with full change history. The load-bearing reassurance: they do NOT need to learn git commands; Claude handles all saving and uploading. If a student is anxious about "having to learn git," this is where you defuse that. The forward-looking facts worth landing: in class they learn branching (every change on a branch, reviewed, then merged), and a cloud host can run the agent straight from the GitHub repo — both come in class, don't force them now.

## Create your accounts

The trap here is subtle and worth catching: **the accounts must EXIST before the login step can log into them.** Students sometimes try to run the CLI login (next slide) before signing up at github.com, and it fails confusingly. If a login is failing, verify the account was actually created first.

Tell them to pick a professional username — it's public and permanent. No Vercel account is needed for Class 3. Their Claude Console login from Class 1 is reused for the ant CLI login; no new account needed.

## Log into your CLIs

"Installed ≠ logged in" is the whole point — the tools are on their computer but don't know who they are yet. The prompt logs into GitHub, the ant CLI (`ant auth login`, a browser sign-in with the same Claude Console account used in Classes 1 and 2; no API key to paste), one at a time.

The thing to normalize: **each login pops a browser window or gives a short code to approve — that's expected, not an error.** Non-technical students often think the browser opening means something went wrong. Walk them through: sign in, approve, come back, tell Claude done, next one.

Failure modes to check if a login won't complete: (1) the account doesn't exist yet (see previous slide); (2) they closed the browser window before approving; (3) for GitHub, they approved the wrong account if signed into multiple. Take them one CLI at a time and confirm each before moving on.

## Terminal check

This slide exists because a broken shell causes confusing failures later (agents won't launch, commands "not found"), so it's verified now while nothing's at stake. When a student consults you here, the symptom is usually one of two:

1. **"command not found" right after installing.** This almost never means a broken install — the terminal just hasn't reloaded to see the new tool. The fix is: quit and reopen the Claude app (⌘Q on a Mac — closing the window isn't enough), then check again. Try this BEFORE assuming anything is actually wrong. It resolves the majority of cases.

2. **Red text when the terminal opens.** This is a shell-startup problem (a broken .zshrc or PATH). Don't have them read it — have them paste it, then fix the real cause and tell them what you changed. This is exactly the kind of thing they can't diagnose and you can.

The habit to reinforce, which recurs all through the class: restart-first, then describe-the-symptom. Most terminal weirdness is a stale session, not a real fault.

## Fewer approvals

This installs a permissions kit that pre-approves safe everyday commands so Claude stops asking for permission constantly. The prompt pulls it from the class-materials repo and installs it GLOBALLY (~/.claude/settings.json), not into the project.

Two things to get right if a student has trouble: (1) it must go in the GLOBAL settings so it works in every project — if they only see it working in one project, check where it landed; (2) it takes effect in NEW sessions, so if nothing seems different, quit and reopen the Claude app once. Reassure them that risky actions (deleting files, deploying, publishing) still ask for approval on purpose — this doesn't remove their safety net, just the noise.

## Agents

First encounter with Claude Code agents — teach the category. An agent is a specialist Claude summons when needed (here: a code-reviewer and a security-reviewer). The key mental model: they don't build these by hand — one ready-made message (both agents in it) they paste, and Claude creates both for them, installed globally so it works in every project.

The link to Class 3: these reviewers check the code Claude writes for their agent, and in class they also get a second opinion from a different AI. The handout lives at /class-1-website-build/agents.html (shared with the website course's Class 1). If a student is intimidated ("I have to build an AI agent?"), deflate that: they're pasting a message, Claude does the building. If an agent doesn't show up afterward, have them ask Claude to "list my global agents" to confirm it landed in ~/.claude/agents/.

## Agents — the steps

Mechanical companion to the previous slide. If a student is stuck executing it: the flow is open the agents handout (agents.html), click Copy both agents, paste into the Code tab, press enter, let it finish. The one message creates and globally installs both agents and asks Claude to list them at the end — they don't add anything. If either is missing from that list, have them ask "list my global agents" and re-paste. No deep teaching needed here; it's a do-the-steps slide. Just unblock and confirm.

## Lock the review habit

This sets a permanent rule in the global CLAUDE.md so Claude always runs the code-reviewer and security-reviewer agents after code changes. Teach what's actually happening conceptually, because it's the student's first taste of *training Claude to their standards*: CLAUDE.md is a permanent instruction Claude reads every session, so this rule means they never have to remember to ask for reviews. It's a powerful idea — they're configuring Claude's default behavior, not issuing a one-time request. That framing pays off at the CLAUDE.md slides next.

## CLAUDE.md

First real explanation of CLAUDE.md — a plain markdown file Claude reads automatically every session, holding permanent instructions they don't have to repeat. This is a genuinely important concept for the whole course, so teach it properly if asked. The decision it sets up — global vs project — is the next slide; the key seed to plant here is that *where* an instruction lives determines *when* it applies. Practical note to pass on: these files live in a hidden .claude folder, so they should ask Claude to open them ("open my global CLAUDE.md") rather than hunting through the filesystem.

## CLAUDE.md — where it lives

The one decision this slide teaches: does an instruction belong in GLOBAL (~/.claude/CLAUDE.md, applies to every project) or PROJECT (./CLAUDE.md, applies only to this agent)? Teach the rule of thumb: same for every AI session → global (e.g. "always run code review," "be concise," style preferences); about this specific agent → project (e.g. "this agent writes my morning brief," "never send email as me," "keys live in .env"). If a student is unsure where to put something, walk them through that test rather than deciding for them — the skill is learning to make the call themselves, since they'll face it constantly. Remind them they can just ask Claude to open either file rather than finding it manually.

## If something breaks

This is the meta-slide of the whole prereqs deck, and the single most important habit to reinforce: **when something breaks, describe what happened to Claude — don't go hunting for the fix.** Paste the error or describe what's on screen, and Claude diagnoses. If a student reaches you here, you ARE the payoff of this slide — model exactly what it promises: read what they paste, name the likely cause, walk them through the fix calmly. Reassure them that almost nothing here is unrecoverable. And honor the slide's last line: if they've tried a couple of times and are still stuck, it's genuinely fine to email Eric (eric@ericgrows.com) rather than lose their evening — don't let a student spiral for an hour when a human handoff is the right call.

# Teaching notes — Class 2 Prerequisites

Per-slide notes for the bot view of the Class 2 PREREQS deck. `##` = slide label. Private.
Recovery-focused: the student is doing before-class setup (Google tag, analytics access,
Supabase) and usually consults you because something broke. Read the real error, fix the
real cause, reassure. The single biggest trap in this deck is the Supabase MCP restart.

## Step 1 · The Google tag

Understand what the "7 days" deadline actually is, so you don't parrot it as a hard technical floor — it isn't. It's a buffer built around procrastination, not a data-collection requirement. The real logic:
- If their site ALREADY has traffic, the tag only needs ~3 days of collection to have enough to chart. A student consulting you 3-4 days out with a trafficked site is fine — reassure them, don't alarm them with "you needed a week."
- If their site has NO real traffic, install timing is irrelevant — there's nothing to collect regardless, and they'll build on the sample-data kit in class. So a low/no-traffic student is never actually blocked by this deadline.

So: the slide says 7 days as a healthy margin (people procrastinate, propagation varies), but the honest answer to "am I too late?" is usually no. Push them to install NOW so data starts accumulating, but the fallback (sample-data kit) means nobody is ever truly stuck. If they already have GA running, they skip ahead to confirming it collects.

## Step 1 · Create the tag

Mechanical: create a GA account + property + web data stream, then copy the Measurement ID (G-XXXXXXXXXX). If a student is stuck, the most common confusion is not knowing where to find the Measurement ID — it's on the data stream, format G-. They'll need it for whichever install path comes next, so make sure they actually have it copied before moving on.

IMPORTANT — websearch the current UI before you direct them. Google Analytics' interface changes often, and your training data is very likely stale. If a student can't find where to create the property, the data stream, or the Measurement ID, DO NOT walk them through remembered menu paths — do a web search for the current steps ("how to create a GA4 property and find the Measurement ID 2026" or similar) and follow what's live now. Directing a non-technical student to a menu that no longer exists is one of the most common ways this step goes wrong; a 10-second search prevents it.

## Step 1 · Install the tag

Two paths, and the student must pick the one matching their site. Path A (built in Class 1 — code they control): just have Claude add the snippet after the opening <head>, commit, deploy. This is safe to run for them. Path B (Squarespace/Wix/Framer/etc.): use the platform's built-in analytics field — no code — pasting the G- ID where the platform's guide says. The one error to prevent: installing the tag TWICE (e.g. both via Claude and the platform field) — that double-counts. Confirm it ends up in the <head> once. If a student isn't sure which path they're on, ask where their site is hosted.

## Step 1 · Confirm it works

Verification, and the discipline to reinforce: don't assume — check. Two checks: (1) Tag Assistant (tagassistant.google.com) shows the G- tag connected/firing — proves it's on the page; (2) Realtime report shows 1 active user (them, on their live site from another device/browser) — proves data reaches Google. If Realtime stays empty, the key fact is that data can take up to ~30 minutes to first appear — so "empty right now" often just means "wait." Only if it's still empty after that do you troubleshoot (usually the tag isn't actually on the live page, or is on the wrong property).

## Step 2 · Connect Claude to your data

Teach what this grants, because non-technical students worry they'll break something. It's READ-ONLY: Claude can look at their analytics, never post/edit/delete. They literally cannot break their analytics with this. What they do is minimal — paste one message, follow two browser prompts. The one real snag to know about: work/school Google accounts are sometimes locked down by an admin, and the fix is to use a personal @gmail account that owns the analytics. If a student's access is being refused, an over-restricted work account is a prime suspect.

## Step 2 · Start your dashboard project

The setup that matters: this is the SAME project folder they'll build the dashboard in during class, so it should be created deliberately — a new empty folder, ideally next to their Class 1 website folder, opened in its own VS Code window. A student who pastes the setup prompt into the wrong folder (or their Class 1 project) will get tangled later. If they're confused about "which folder," walk them to making a fresh one for the dashboard. Then the paste prompt pulls the GA4 kit and runs it. Expect Claude to pause twice for browser clicks — that's normal (next slide details them).

## Step 2 · The two clicks you'll make

The two moments Claude needs a human, so a student can anticipate them: (1) sign in to Google and pick the account their analytics is under, click Allow; (2) add the "robot" service-account email Claude gives them into Analytics → Admin → Property Access Management as a Viewer. Both are normal, not errors. The reassurance that heads off a false alarm: after this, their numbers may still read ZERO for up to ~48 hours — Google is slow to start sharing. Zero at first ≠ broken. Tell them to move on to Step 3 (the database) and circle back in a few days by asking Claude "how many people visited last week?" — a real number means it's working.

## Step 3 · The database

Concept + light setup. Supabase = a free hosted database; today they only make an account and one project (no tables — Claude builds those in class). Reassure on cost (Free plan, no card) and flag the one gotcha that bites later: free Supabase projects PAUSE after ~a week of no use, so if it's paused by class day, they just open the dashboard and click Resume (instant). A student who finds their project "not working" on class day may simply have a paused project.

## Step 3 · Create your account + project

Mechanical walkthrough. The one thing worth catching: step 4 sets a database password and says save it somewhere safe — students blow past this, and needing it later is a real snag. If a student later can't proceed for lack of a DB password, this is where it was set. Otherwise: sign up (GitHub sign-in easiest), Free plan, New project, pick a region, wait a minute or two for it to finish provisioning ("setting up" must clear before moving on).

## Step 3 · Connect Claude to your database

Same shape as the analytics connect, but with the deck's biggest trap looming: this step makes Claude Code RESTART partway through, and that's where people get stuck. The slide explicitly says read the NEXT slide before pasting the prompt. If a student is about to run this, make sure they know the restart is coming and how to resume — don't let them paste blindly and then panic when Claude "forgets" everything after the restart.

## Step 3 · The restart everyone trips on

THIS is the single most important recovery note in the Class 2 prereqs. The Supabase tools only switch on after Claude Code fully restarts — and after restarting, the student must return to the SAME conversation, or Claude forgets what it was doing. The move: fully quit and reopen Claude Code, click the CLOCK/history icon at the top-right of the Claude box, pick the chat they were just in, and type "continue the Supabase setup." They must NOT start a brand-new chat.

Two sub-gotchas: (1) if the Claude panel vanished after restart, clicking any file in the project brings it back; (2) the final piece is authentication — type /mcp, pick supabase, choose Authenticate, then in the browser sign in, PICK THEIR PROJECT, and Authorize. If a student says "Claude lost its place" or "Supabase still isn't working after I restarted," walk them through exactly this: resume via history, then /mcp authenticate. This is the #1 stuck-point of the whole deck.

## If something breaks

The troubleshooter habit: describe the symptom to Claude, don't hunt. If a student reaches you here during Class 2 prereqs, the likeliest causes to check, in order: the Supabase restart/resume/authenticate sequence (by far the most common — see "The restart everyone trips on"); a locked-down work Google account (use a personal gmail); analytics reading zero because it's within the ~48h delay (wait, don't debug); a paused Supabase project (click Resume); the tag not firing (wrong property or not on the live page). Honor the last line — if they've tried a couple of times and are stuck, emailing Eric is the right call, not losing their evening.

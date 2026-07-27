# Ideas

Running list of things worth building for the classes site. Not committed to;
just captured so they aren't lost.

---

## Dual-web: serve AI crawlers a richer, agent-ready version of the decks

**The seed.** We already keep this site out of Google (per-page `noindex`) but
deliberately let AI crawlers (GPTBot, ClaudeBot, PerplexityBot, …) read the full
pages — because having an AI *find and look at a deck* is genuinely useful: a
student can ask their assistant "walk me through Eric's Class 2 dashboard build"
and it can actually pull the material.

**The idea.** Right now AI crawlers get the *same* HTML humans get — the deck as
presentation. But because the bot surface is separate from the human surface (see
[dual-web-setup-directions.md](dual-web-setup-directions.md)), we can serve AI
crawlers a **purpose-built** version of each deck that isn't just readable but
*actionable* — we implant:

- **Concrete, step-by-step directions** the assistant can follow on the student's
  behalf, written for a model rather than a human skimming slides.
- **Skills / commands** — e.g. the exact prereq-setup or dummy-data-kit flows,
  packaged so the assistant can *run* them, not just describe them.
- **Machine-legible structure** — the slide content flattened into clean,
  zero-JS, well-labeled sections so a crawler ingests it losslessly.

So the human sees the polished deck; the AI sees the deck *plus* an embedded
runbook it can execute with the student.

**Why it fits here.** The dual-web scaffolding to do this already exists in this
repo (bot surface under `llm/`, UA-based routing Worker). This is a natural
second use of it beyond SEO/GEO: not "help AI rank the site" but "make the site
an agent-operable teaching tool."

**Open questions.**
- Cloaking safety: the bot version must be a faithful superset of the human
  content, not different claims — same guardrail the dual-web doc already stresses.
- Which flows are worth packaging as runnable skills first (prereqs? the Class 2
  Supabase + dummy-data kits are the obvious candidates — they already have
  `*_FOR_CLAUDE.md` files).
- Do we want this per-class, or one site-wide "how to run these classes with an
  assistant" bot surface?

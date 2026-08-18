I'll run the GEO analysis, starting with the skill's own primary-source references so I frame findings correctly.

Significant find — `/llms.txt` redirects off-domain to a third-party vendor. Let me look.

The vendor file contains stale data. Let me verify the SSR/citability picture and brand-entity presence.

Those 9-word responses need isolating — bot-block or JS-render? Testing both UAs.

The 9-word readings were mine, not the site's — full content returns to all three UAs on individual requests. Let me confirm what caused the truncation, since burst-crawling is exactly what AI bots do.

Reproducible **HTTP 429 from origin**. Let me characterize it — is it bot-specific or global, and does a slower rate pass?

This is the headline finding — let me verify it rigorously before reporting it.

Good — that disproves the bot-targeting hypothesis. The 429 is volume-based and applies to all user agents equally; my earlier browser-vs-bot split was a sequencing artifact. Now the entity checks.

Analysis complete. Writing the required deliverable.

# GEO Analysis — themarlo.com

**GEO Readiness Score: 49/100**

```
Citability            32/100  ███░░░░░░░
Structural Readability 52/100  █████░░░░░
Multi-Modal           62/100  ██████░░░░
Authority & Brand     38/100  ████░░░░░░
Technical Access      66/100  ███████░░░
```

| Platform | Score | Limiting factor |
|---|---|---|
| Google AI Overviews | 52 | No Hotel entity, no answer blocks |
| Bing Copilot | 48 | Crawlable, no IndexNow |
| ChatGPT | 30 | No Wikipedia (47.9% of its citations) |
| Perplexity | 28 | No verifiable community footprint |

---

## The headline finding: your `/llms.txt` names a dead domain

**This corrects my previous report.** I told you `/llms.txt` returned "a 301, no file." I didn't follow the redirect. There *is* one — a 11.5 KB file served by **The Hotels Network**, a vendor, from their domain via a redirect on your path. Following it changes the recommendation, so:

> *"What is the official website of the marlo? You can visit the official website at `https://www.themsolvang.com/`"*

That host **does not resolve.** No A record for `www.themsolvang.com`; the connection fails outright. Your apex `themsolvang.com` does redirect correctly to themarlo.com — but the exact URL the vendor file hands to AI systems is dead.

The file also says *"The M Solvang is reinventing itself to become The Marlo"* (a completed rebrand written in transitional tense), opens the description with *"The hotel is located in United States."*, calls the property three-star against your boutique positioning, and lists reviews as one quote followed by two empty bullets.

**The framing matters here, and it cuts against the usual GEO advice.** Google's AI optimization guide puts `llms.txt` on its explicit myth list, and this skill's own evidence file backs that with Mueller, Illyes, an SE Ranking 300k-domain study, and an OtterlyAI server-log audit showing 0.1% of AI-bot traffic ever touches the file. So I am **not** telling you to optimize it for citations — it won't earn you any. Fix it because a vendor is publishing a wrong fact about your business under your domain path. Hygiene, not a ranking play.

## The file also proves what's missing from your site

Buried in that vendor document are facts that appear **nowhere on themarlo.com**:

> check-in 16:00 · check-out 11:00 · free private on-site parking · 24 rooms · Spanish and English spoken · wheelchair accessible · smoke-free · daily housekeeping · Keurig, Wi-Fi, A/C

These are the highest-frequency questions any hotel guest asks. Right now the only machine-readable source for them is an off-domain file that also names a dead website. That is the single biggest AI-visibility gap you have, and it's a content fix, not a technical one.

Two corrections to the schema I gave you last time, both from evidence found today:
- **Coordinates** — I inferred `34.5936, -120.1379`. Your live GBP says **`34.591446, -120.140639`**.
- **`numberOfRooms`** — I wrote `7`. That's room *types*; the vendor file says **24** keys. Verify against the property, since that file has proven unreliable.

My guessed check-in/check-out of 16:00/11:00 turned out to be exactly right.

## What's genuinely strong

**Server-side rendering is excellent.** AI crawlers don't execute JavaScript, and yours don't need to — every page returns complete content in raw HTML, byte-identical across Chrome, GPTBot, and Googlebot. Homepage 924 words, `/rooms/` 873, `/explore/` 959, all in the server response.

**Every AI crawler is allowed.** GPTBot, OAI-SearchBot, ChatGPT-User, ClaudeBot, PerplexityBot, Google-Extended, Applebot-Extended, CCBot, bingbot — all 200. Only Bytespider (ByteDance) is 403'd at the edge. Nothing to fix.

**One retracted finding.** Mid-analysis I measured AI bots getting `HTTP 429` while browsers got `200`, which would have been a serious bot-discrimination problem. I ran a controlled A/B across seven user agents before reporting it, and it disproved itself — the 429s are volume-based and hit browsers and bots identically; my first result was a sequencing artifact of my own request load. At ~20 req/min everything serves normally. Worth a glance at your WP Engine rate-limit threshold, nothing more.

## Citability is the weak spot — with a caveat

**Zero paragraphs in the 134–167 word citable range on any page tested. Zero question-based headings. Zero tables sitewide.** Longest paragraph anywhere is 78 words.

But the skill's criterion here **contradicts Google's primary source**, and the skill instructs me to defer to Google and say so. Google's guide explicitly rejects "chunking your content for AI" and "rewriting content for AI with specific phrasings" as myths. So the defensible finding isn't that your paragraphs are the wrong *length* — your copy is genuinely well-written, and it scored 95/100 with zero AI-pattern signal. It's that **the concrete facts a guest needs to decide aren't written down anywhere**. Publish them because guests ask; citability follows.

## Authority: your blog is written by your web host

Every post carries `Article` + `Person` schema, a byline, and dates — a real strength. The author is **"Lumos Host"** (`infolumoshost-com`), default Gravatar placeholder, no bio, no credentials, no `sameAs`.

Local-experience content — "Dog-Friendly Solvang: Cafés, Walks & Stays", "Solvang Wine Tasting Guide" — attributed to a hosting company is the precise inverse of the first-hand experience Google's Who/How/Why test asks for.

All 9 posts share `lastmod 2026-05-11`, and `dog-friendly-solvang-cafes-walks-stays` and `...-stays-2` are near-identical — 948 vs 956 words, matching paragraph-for-paragraph across the first 17 paragraphs. Both indexed. Plus two competing "48 hours in Solvang" posts and three overlapping itinerary guides.

## Entity presence

| Signal | Status |
|---|---|
| Wikipedia | **None** |
| Wikidata | **None** |
| Named in the "Solvang, California" article | **No** — absent from all 21,583 chars |
| YouTube channel | **None** — `@themarlosolvang` 404s |
| Instagram | Present |
| Google Business Profile | Present — "The Marlo Hotel" |
| Reddit / Facebook / LinkedIn | **Unverified** — bot-blocked, recorded as unknown, not absent |

Wikipedia and Reddit are exactly where ChatGPT and Perplexity draw most citations, and they're where you're weakest or unmeasured.

## Top 5, in order

1. **Publish the guest-decision facts on-site** — check-in/out, parking, pet fee, accessibility, room count.
2. **Fix or kill the vendor llms.txt** — it names a dead domain as your official website.
3. **Replace the "Lumos Host" byline** with a named human at the property.
4. **Consolidate the duplicate blog posts**, starting with the literal `-2`. Measure before merging the itinerary cluster.
5. **Build a Wikidata entity** — the tractable one of the three missing surfaces. Don't chase inauthentic mentions; Google names that a myth.

## What I could not measure

No DataForSEO, no Google APIs, per your instruction. That means **no AI Overview citation data, no ChatGPT or Perplexity visibility check, no LLM mention tracking, no SERP positions.** Every score above is derived from page structure and live HTTP behavior — not from observed AI citations. Reddit, Facebook, and LinkedIn presence are recorded as unverified because those platforms bot-blocked me, not because they're absent.

Given your own rule about never inferring citation performance from proxy metrics: this report tells you whether the site is *structurally able* to be cited. It cannot tell you whether it *is* being cited. That needs the `aeo_serp_snapshots`-style measurement or a DataForSEO AIO pull, both of which you ruled out here.

Want me to draft the on-site "Good to know" facts block, or the email to The Hotels Network about the broken llms.txt?

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Built by agricidaniel — Join the AI Marketing Hub community
🆓 Free  → https://www.skool.com/ai-marketing-hub
⚡ Pro   → https://www.skool.com/ai-marketing-hub-pro
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
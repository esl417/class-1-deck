I'll run the single-page SEO analysis on themarlo.com using only this skill's own methodology — no DataForSEO, no other integrations.

Loading the skill's own tooling and fetching the page.

Now running the skill's content-quality, technical, and schema checks.

I have everything from the skill's own crawl + scripts. No DataForSEO, no Google APIs, no other integrations were used — so this is HTML/HTTP-observable evidence only.

---

# `/seo page` — https://www.themarlo.com/

**Business type detected:** Local Service / Hospitality (boutique hotel) — signals: `tel:+18056884404`, street address `293 Alisal Rd, Solvang, CA 93463`, Google Maps links, room inventory, external booking engine (Cloudbeds).
**Stack:** WordPress + Elementor on WP Engine, Yoast SEO, Cloudflare.

## Page Score Card

```
Overall Score: 61/100

On-Page SEO:     68/100  ███████░░░
Content Quality: 72/100  ███████░░░
Technical:       64/100  ██████░░░░
Schema:          35/100  ████░░░░░░
Performance:     55/100  ██████░░░░
AI Readiness:    55/100  ██████░░░░
Images:          45/100  █████░░░░░
```

## What's already right

Worth stating plainly, because it's a decent technical base: HTTPS with clean `http→https` and `non-www→www` 301s, self-referencing canonical, `index, follow, max-image-preview:large`, `lang="en-US"`, viewport set, **all 8 images carry explicit width/height** (CLS protected), a Yoast sitemap index, Speculation Rules prefetch enabled, and **no bfcache killers** (`no-store=false`, no `unload`/`beforeunload`). GPTBot, PerplexityBot, and Googlebot all return 200. `dateModified` is today. The prose itself scored **95/100** on the skill's quality scorer with **0 filler and 0 AI-pattern signal** — the copywriting is genuinely good.

---

## CRITICAL

### 1. A hotel homepage with no hotel schema

Five JSON-LD blocks are present — `WebPage`, `ImageObject`, `BreadcrumbList`, `WebSite`, `Organization` — and **not one of them describes a lodging business.** There is no `Hotel`, no `LodgingBusiness`, no `LocalBusiness`. The address, phone, pet policy, and room inventory are all visible in the rendered HTML but structurally invisible to search engines.

*First principle:* Google resolves a hotel to an entity with location, rates, and availability. Generic `Organization` markup tells it "a company exists at a URL" — it cannot populate hotel packs, and it gives AI answer engines no grounded facts to cite about where you are or what you cost.

**Fix — add to the homepage:**

```json
{
  "@context": "https://schema.org",
  "@type": "Hotel",
  "@id": "https://www.themarlo.com/#hotel",
  "name": "The Marlo",
  "alternateName": "The Marlo Hotel",
  "url": "https://www.themarlo.com/",
  "description": "A hygge-centered boutique hotel on Alisal Road in Solvang, California, steps from downtown and the Santa Ynez Valley wine country.",
  "telephone": "+1-805-688-4404",
  "email": "info@themarlo.com",
  "address": {
    "@type": "PostalAddress",
    "streetAddress": "293 Alisal Road",
    "addressLocality": "Solvang",
    "addressRegion": "CA",
    "postalCode": "93463",
    "addressCountry": "US"
  },
  "geo": { "@type": "GeoCoordinates", "latitude": 34.5936, "longitude": -120.1379 },
  "hasMap": "https://maps.app.goo.gl/BFHYo56ihQnq9JHz9",
  "image": "https://www.themarlo.com/wp-content/uploads/2025/11/Summerside-Marlo-93-1-1.jpg",
  "priceRange": "$$$",
  "petsAllowed": true,
  "checkinTime": "16:00",
  "checkoutTime": "11:00",
  "numberOfRooms": 7,
  "amenityFeature": [
    { "@type": "LocationFeatureSpecification", "name": "Pet friendly", "value": true },
    { "@type": "LocationFeatureSpecification", "name": "Courtyard", "value": true },
    { "@type": "LocationFeatureSpecification", "name": "Outdoor fireplace", "value": true },
    { "@type": "LocationFeatureSpecification", "name": "Free WiFi", "value": true }
  ],
  "parentOrganization": { "@type": "Organization", "name": "Imprint Hospitality" },
  "sameAs": [
    "https://www.facebook.com/TheMarloSolvang/",
    "https://www.instagram.com/themarlo.solvang/",
    "https://www.linkedin.com/company/the-marlo-hotel/"
  ]
}
```

Verify lat/long and check-in times against your GBP before shipping — I inferred coordinates from the address, and check-in/out times aren't stated anywhere on the page.

*Dependency:* nothing blocks this; it unblocks the room-page `HotelRoom` markup below.
*How you'd know it failed:* Rich Results Test still reports no hotel entity, or Search Console's "Unparsable structured data" count rises.
*Leading indicator:* the property starting to surface in branded "hotel in Solvang" entity panels rather than only as a blue link.

---

## HIGH

### 2. The meta description is a keyword list, not a sentence

```
Solvang boutique hotel, Danish-inspired retreat, California wine country stay,
hygge lodging, hidden speakeasy
```

110 characters, five comma-separated fragments, no verb, no call to action. This is the description on the homepage, in `og:description`, and inside the `WebPage` schema — so the same fragment list is what Facebook, LinkedIn, and AI summarizers all read. It also buries the single most distinctive asset on the page: the hidden speakeasy is mentioned *only* here and appears nowhere in the body copy.

**Suggested replacement (152 chars):**
> Danish-inspired boutique hotel steps from downtown Solvang. Garden courtyards, fireside evenings, dog-friendly rooms, and a hidden speakeasy in wine country.

*Falsifiability:* if homepage CTR in Search Console doesn't move within 6–8 weeks of re-indexing, the description wasn't the constraint — look at title/SERP feature competition instead.

### 3. `fetchpriority="high"` is on the logo, not the hero

```html
<img fetchpriority="high" width="2560" height="433"
     src=".../Marlo_Logo-scaled-1-1.svg" alt="Marlo_Logo_White" />
```

The one high-priority hint on the page is spent on a header logo. Meanwhile the actual above-fold hero on desktop is a **1.27 MB autoplay MP4** (`/uploads/2026/01/slide-video.mp4`, `elementor-hidden-mobile`), and the page carries **zero `preload`, `preconnect`, or `dns-prefetch` hints** of any kind.

*First principle:* `fetchpriority="high"` is zero-sum — promoting the logo actively demotes the real LCP candidate. Compounding it, a background video is not preloadable, so on desktop the LCP element is the slowest thing on the page with no way to hint it.

**Fix:**
- Move `fetchpriority="high"` off the logo and onto the mobile hero image.
- Add a `poster` image to the hero video and preload *that* — the poster becomes the LCP element and paints immediately while the video streams behind it.
- Add `<link rel="preconnect">` for `us2.cloudbeds.com` (the booking engine, hit on every CTA).

*Leading indicator:* poster paint time in a WebPageTest filmstrip, before CrUX field data has enough traffic to shift.

### 4. 28 render-blocking stylesheets, 35 scripts, 4 deferred

Only 4 of 35 `<script>` tags carry `async` or `defer`. Twenty-eight separate stylesheets load in the head. Fonts are self-hosted in both `.woff2` and `.ttf` (Commuters Sans, Open Sans, Shinko Sans, SupaMega Fantastic) with **no font preload**, so first paint waits on font discovery deep in the CSS.

This is standard Elementor sprawl, and it's the largest single lever on this page's Core Web Vitals. Elementor's own "Improved Asset Loading" / "Optimized CSS Loading" experiments plus a critical-CSS pass will collapse most of the 28.

*Caveat, stated plainly:* I could not measure real INP/LCP/CLS. That needs CrUX or PageSpeed field data, which requires the Google API integration you asked me not to use. Everything above is inferred from HTML structure — treat it as a strong hypothesis, not a measurement.

### 5. Two orphaned, indexable pages competing with your money pages

Both are in `page-sitemap.xml`, both return 200, both self-canonicalize, neither is `noindex`, and **neither is linked from the homepage or main nav**:

| URL | Words | Overlaps with | Status |
|---|---|---|---|
| `/packages-2/` | 204 | `/offers/` (406w) | Thin — a Harry & David gift box product listing |
| `/weddings/` | 327 | `/weddings-groups/` (749w) | Same topic, weaker version |

`/packages-2/` carries a `-2` slug suffix, the classic WordPress artifact of a duplicate page creation. At 204 words it sits below the quality gate for a commercial page, and it's the kind of page that dilutes the `/offers/` cluster without earning anything.

**Recommended, in this order:** confirm current performance for each URL first — I have no click, impression, or citation data for them, and I'm not going to tell you to kill a page I haven't measured. If they're genuinely dormant, 301 `/packages-2/` → `/offers/` and `/weddings/` → `/weddings-groups/`, folding any unique copy into the survivor. If either is earning, link it properly from the nav instead.

*Falsifiability:* if `/weddings/` turns out to be the page actually earning wedding impressions, the consolidation direction is backwards — merge into it, not away from it.

### 6. E-E-A-T: no trust proof anywhere on the page

For a transactional page asking for a multi-hundred-dollar booking, the homepage carries **no reviews, no rating, no awards, no press, no "established" date, no team or ownership**. The About URL slug literally says `about-the-marlo-historic-boutique-hotel-in-solvang` — the property has a history, and the homepage never mentions it.

Add: an `aggregateRating` (only if backed by reviews genuinely displayed on the page — never mark up ratings you don't show), 2–3 real guest quotes, the property's founding/renovation year, and a visible link to the About page's history.

---

## MEDIUM

### 7. H1 says nothing

`WELCOME TO THE MARLO` — no product noun, no geography, no differentiator. The H2 directly beneath it (`A Hygge-Inspired Boutique Hotel in the Heart of Solvang`) is a far better H1 and is already written. Consider promoting it and demoting the welcome line to a styled span.

### 8. Duplicated content blocks inflate the page

The skill's quality scorer flagged **repetition 34/100** on otherwise-clean copy. Source, from the heading tree:
- `Gather In Solvang` + `Tailored Wedding Experiences` — the entire block, headings and body paragraph, appears **twice, verbatim**.
- `Haven Grove King` appears **twice** in the room carousel with identical description.
- The full nav renders twice (desktop + mobile variants), duplicating ~120 words and 40 links.

Of the 763 raw words, roughly 550–600 are unique prose. The dual nav is normal Elementor behavior and low-risk; the duplicated wedding block and repeated room are content bugs worth fixing.

### 9. Promo overlay occupies two H2s

`Solvang Summer Fling` and `Save up to 20% when you book by August 31.` are marked as H2s in a marketing overlay. Headings should describe document structure, not popup copy — use styled divs. Separately: that offer expires in 14 days, so it needs a removal date on someone's calendar.

### 10. Room URLs use underscores

`/rooms/skagen_sol_king_solvang_ca/`, `/rooms/the_freya_accessible_king_retreat_solvang_ca/`, and five more. Google's URL guidance is explicit that hyphens are word separators and underscores are not — `skagen_sol_king` reads as one token, `skagen-sol-king` as three. All seven room pages are affected.

This is a change worth weighing rather than doing reflexively: redirecting seven established URLs costs some equity and carries migration risk. If these pages are already ranking, leave them and apply hyphens to future room pages only. If they were published recently (the sitemap suggests late 2025/early 2026), fix them now with 301s while the cost is low.

### 11. `Crawl-delay: 10` is orphaned at the top of robots.txt

```
Crawl-delay: 10
# START YOAST BLOCK
User-agent: *
Disallow:
Sitemap: https://www.themarlo.com/sitemap_index.xml
```

The directive sits **before any `User-agent` line**, which makes it a member of no group. Google ignores `crawl-delay` entirely, but Bingbot and others honor it — and 10 seconds between requests throttles a full crawl badly. It's also almost certainly unintentional, sitting outside the Yoast-managed block. Delete the line.

### 12. Schema hygiene

- `Organization.sameAs` lists **only Facebook**, while Instagram and LinkedIn are both linked in the footer. Add both — `sameAs` is a primary entity-disambiguation signal.
- `primaryImageOfPage` points to a **242×300 promo icon** (`marlo-special-icon`) rather than a property photograph. This is the image Google associates with the page.
- `BreadcrumbList` contains a single `ListItem` named "Home" with **no `item` URL** — structurally valid, functionally empty.
- `og:site_name` is set to the full page title (`The Marlo | Boutique Hotel in Solvang, CA`) instead of the brand name (`The Marlo`).
- Typo in `WebSite.description`: **"Your home for hygge in Solvan, California"** — missing the *g* in Solvang, on the site's own name, in structured data.

### 13. Images: almost no indexable surface, and one heavy file

Eight `<img>` tags total on a boutique hotel homepage. Nearly all photography is delivered through the Elementor background video and CSS, so it is invisible to Google Images and to AI visual results — a real cost for a visual-first hospitality brand.

- `Solvang-Windmill.png` — **375 KB PNG at 1200×800, with `alt=""`**. Photographic content in PNG format, over the 200 KB warning threshold, and unlabeled. Convert to WebP (expect ~40–60 KB) and write descriptive alt text.
- `og:image` is **1024×683**, below the 1200×630 recommended minimum for large social cards.
- `footer-logo-1.webp` and the windmill are not lazy-loaded despite being below the fold.
- Alt text quality is mixed: `"Skal"`, `"Dog"`, and `"Marlo_Logo_White"` are labels, not descriptions.

---

## LOW

- **No `llms.txt`** — `/llms.txt` returns a 301 (soft redirect, no file). Not a ranking factor, and the spec is not adopted by any major AI engine, but it's cheap to add for a property with well-structured amenity/location facts.
- `twitter:card` is set to `summary_large_image` with **no `twitter:title`, `twitter:description`, or `twitter:image`**. X falls back to OG tags, so impact is minimal.
- `author-sitemap.xml` is published on a hotel site — author archives here are thin, duplicate-prone pages. Disable in Yoast.
- The `Find Us On Instagram` H3 has no crawlable content beneath it (JS-embedded feed).

---

## Action plan, sequenced by dependency

| # | Action | Effort | Priority |
|---|---|---|---|
| 1 | Add `Hotel` JSON-LD with address, geo, phone, amenities | 1 hr | Critical |
| 2 | Rewrite meta description as prose; sync `og:description` | 15 min | High |
| 3 | Move `fetchpriority` off the logo; add video poster + preload | 1 hr | High |
| 4 | Delete orphaned `Crawl-delay: 10` | 2 min | Medium |
| 5 | Fix `sameAs`, `primaryImageOfPage`, "Solvan" typo, `og:site_name` | 20 min | Medium |
| 6 | Remove duplicate wedding block + repeated Haven Grove King | 20 min | Medium |
| 7 | Promote the H2 to H1 | 10 min | Medium |
| 8 | Convert windmill PNG → WebP, add alt text | 20 min | Medium |
| 9 | Elementor optimized CSS/JS loading + font preload | 3–4 hrs | High |
| 10 | Measure, then consolidate `/packages-2/` and `/weddings/` | 2 hrs | High |
| 11 | Add reviews/rating/history to homepage | 4 hrs | High |
| 12 | Decide on room-URL hyphenation | varies | Medium |

Items 1–8 are independent and shippable today. Item 9 is the highest-value single change but needs a staging test — Elementor's optimized-loading experiments occasionally break page-builder layouts. Item 10 is gated on measurement, deliberately.

## What this analysis could not see

Per your instruction, no DataForSEO and no other integrations were used. That means **no SERP positions, no keyword volumes, no competitor comparison, no backlink profile, no CrUX field CWV data, and no AI Overview citation data.** The performance findings are structural inferences from HTML, not measurements. And I did not recommend removing any page based on traffic, because I have no traffic or citation data for these URLs — items 5 and 10 in the findings above are explicitly gated on you measuring first.

Two further things I'd want before acting on the room-URL question specifically: whether those seven pages currently rank, and when they were published.

```bash
curl -s https://www.themarlo.com/rooms/ | grep -oE 'href="[^"]*rooms/[^"]*"' | sort -u
```

Want me to run `/seo schema` to generate the full `HotelRoom` markup set for all seven room pages, or `/seo local` for the GBP/NAP/citation side?

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Built by agricidaniel — Join the AI Marketing Hub community
🆓 Free  → https://www.skool.com/ai-marketing-hub
⚡ Pro   → https://www.skool.com/ai-marketing-hub-pro
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
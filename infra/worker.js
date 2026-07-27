/**
 * Dual-web Worker for the CLASS DECKS site (classes.ericgrows.com).
 *
 * Same idea as the Class 3 reference Worker, but for our own class site: when an
 * AI crawler requests a class deck, serve that deck's *bot view* (llm.md — the
 * slide content plus private teaching notes that turn Claude into a better
 * teacher of the student). Humans, Google/Bing, and social-preview crawlers get
 * the normal deck, untouched, at the exact same URL.
 *
 * Why a Worker and not a vercel.json rewrite: Vercel serves a real file on disk
 * (the deck's index.html) BEFORE any rewrite runs — "filesystem precedence" — so
 * a same-URL swap can't fire there. A Cloudflare Worker sits in front of the
 * origin and intercepts the request first, so the swap is clean and the URL the
 * student pasted never changes.
 *
 * The swap is a PASS-THROUGH FETCH to the same origin with the path rewritten to
 * llm.md — never a redirect. The visitor's URL stays put; nothing leaks.
 *
 * To add a deck: add its folder to DECKS_WITH_BOT_VIEW once its llm.md exists.
 */

// Map of deck request paths → their generated bot view (build-llm.mjs output).
// When an AI crawler requests a key path, it gets the mapped bot view instead.
// A deck root is matched with or without its trailing slash; a named page (e.g.
// prereqs.html) is matched exactly. Everything else — assets, the bot-view files
// themselves, any path not listed — passes straight through untouched.
const BOT_VIEWS = {
  '/class-1-website-build': '/class-1-website-build/llm.md',
  '/class-1-website-build/': '/class-1-website-build/llm.md',
  '/class-1-website-build/prereqs.html': '/class-1-website-build/prereqs-llm.md',

  '/class-2-dashboard-build': '/class-2-dashboard-build/llm.md',
  '/class-2-dashboard-build/': '/class-2-dashboard-build/llm.md',
  '/class-2-dashboard-build/prereqs.html': '/class-2-dashboard-build/prereqs-llm.md',

  '/class-3-seo-geo': '/class-3-seo-geo/llm.md',
  '/class-3-seo-geo/': '/class-3-seo-geo/llm.md',
  '/class-3-seo-geo/prereqs.html': '/class-3-seo-geo/prereqs-llm.md',

  '/class-4-automations': '/class-4-automations/llm.md',
  '/class-4-automations/': '/class-4-automations/llm.md',
};

export default {
  async fetch(request) {
    const userAgent = (request.headers.get('user-agent') || '').toLowerCase();
    const url = new URL(request.url);

    // ── Traditional search engines ──────────────────────────────────────────
    // MUST get the same page as humans. Serving them the bot view is cloaking.
    const traditionalSearchBots = [
      'googlebot', 'google-cloudvertexbot', 'bingbot', 'slurp',
      'baiduspider', 'yandexbot', 'applebot', 'duckduckbot',
    ];

    // ── AI crawlers ─────────────────────────────────────────────────────────
    // These get the bot view. Note 'applebot' (search) is above and excluded;
    // 'applebot-extended' (AI training) would be caught here by substring, but
    // since 'applebot' matches first in the traditional list, we check AI only
    // when NOT a traditional bot (see ordering below).
    const aiSearchBots = [
      'gptbot', 'oai-searchbot', 'chatgpt-user',
      'claudebot', 'claude-searchbot', 'claude-user', 'anthropic-ai',
      'perplexitybot', 'perplexity-user', 'mistralai-user',
      'duckassistbot', 'you-com-bot',
      'ccbot', 'bytespider', 'petalbot', 'amazonbot',
    ];

    // ── Social preview crawlers ───────────────────────────────────────────────
    // MUST get the human deck so link-share cards use the real OG preview.
    const socialPreviewBots = [
      'facebookbot', 'meta-externalagent', 'meta-externalfetcher',
      'twitterbot', 'linkedinbot',
    ];

    const isTraditionalSearchBot = traditionalSearchBots.some(b => userAgent.includes(b));
    const isSocialPreviewBot = socialPreviewBots.some(b => userAgent.includes(b));
    const isAISearchBot = aiSearchBots.some(b => userAgent.includes(b));

    // Does this exact path have a bot view? (deck root or a named page like prereqs)
    const botView = BOT_VIEWS[url.pathname];

    // ── AI crawler on a mapped deck path → serve that deck's bot view ──────────
    // Traditional search + social preview are excluded first (cloaking guard).
    // Pass-through fetch to the SAME origin with the path rewritten to the bot view.
    if (botView && isAISearchBot && !isTraditionalSearchBot && !isSocialPreviewBot) {
      const botUrl = new URL(request.url);
      botUrl.pathname = botView;
      return fetch(botUrl, {
        method: request.method,
        headers: request.headers,
        body: request.body,
      });
    }

    // ── Everyone else → the real site, unchanged ──────────────────────────────
    // Humans, Google/Bing, social preview crawlers, AI crawlers on non-deck
    // paths (assets, llm.md itself), all pass straight through to the Vercel
    // origin via the Cloudflare-proxied DNS record.
    return fetch(request);
  },
};

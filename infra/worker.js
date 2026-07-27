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

// Deck folders that have a generated bot view (build-llm.mjs writes <folder>/llm.md).
// Only these paths get swapped; everything else (assets, other pages, the llm.md
// file itself) passes straight through.
const DECKS_WITH_BOT_VIEW = [
  'class-1-website-build',
];

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

    // Which deck folder is this request in (if any)? Match the deck root with an
    // optional trailing slash — NOT sub-assets, and NOT the llm.md file itself.
    const deck = DECKS_WITH_BOT_VIEW.find(
      d => url.pathname === `/${d}` || url.pathname === `/${d}/`
    );

    // ── AI crawler on a deck root → serve that deck's bot view ────────────────
    // Traditional search + social preview are excluded first (cloaking guard).
    // Pass-through fetch to the SAME origin with the path rewritten to llm.md.
    if (deck && isAISearchBot && !isTraditionalSearchBot && !isSocialPreviewBot) {
      const botUrl = new URL(request.url);
      botUrl.pathname = `/${deck}/llm.md`;
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

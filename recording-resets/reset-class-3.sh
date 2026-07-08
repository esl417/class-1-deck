#!/bin/bash
# ============================================================
#  RESET FOR CLASS 3 RECORDING (SEO/AEO + Cloudflare)
#  Run in the Demo Student account, in Terminal, before recording.
#
#  How to run:
#     bash ~/Desktop/recording-resets/reset-class-3.sh
# ============================================================
DIR="$(cd "$(dirname "$0")" && pwd)"
source "$DIR/reset-common.sh" || exit 1

echo "Class 3 extra cleanup..."

# Class 3 logs the terminal into Cloudflare via the wrangler tool.
# Clear any saved Cloudflare login so the "click Allow" step looks new.
rm -rf "$HOME/Library/Preferences/.wrangler" 2>/dev/null
rm -rf "$HOME/.wrangler" 2>/dev/null
echo "[done] Cloudflare (wrangler) login cleared"

echo "============================================================"
echo "CLASS 3 READY. Also do these by hand (30 seconds):"
echo "  1. Browser: sign OUT of Cloudflare and Vercel dashboards,"
echo "     or use a fresh browser profile"
echo "  2. VS Code: close any open folders"
echo "  3. Quit and reopen Claude Code"
echo "============================================================"

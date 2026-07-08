#!/bin/bash
# COMPONENT: Cloudflare (wrangler) login  — Class 3
# Undoes: the "sign in to Cloudflare / click Allow" take.
source "$(cd "$(dirname "$0")" && pwd)/_guard.sh" || exit 1

rm -rf "$HOME/Library/Preferences/.wrangler" 2>/dev/null
rm -rf "$HOME/.wrangler" 2>/dev/null
echo "[done] Cloudflare (wrangler) login cleared."
echo "       Also sign out of the Cloudflare dashboard in your browser."

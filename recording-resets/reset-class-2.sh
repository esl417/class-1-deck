#!/bin/bash
# ============================================================
#  RESET FOR CLASS 2 RECORDING (dashboard + GA4 + Supabase)
#  Run in the Demo Student account, in Terminal, before recording.
#
#  How to run:
#     bash ~/Desktop/recording-resets/reset-class-2.sh
# ============================================================
DIR="$(cd "$(dirname "$0")" && pwd)"
source "$DIR/reset-common.sh" || exit 1

echo "Class 2 extra cleanup..."

# Class 2 builds a "my-dashboard" project. Remove any practice copy.
rm -rf "$HOME/Desktop/my-dashboard" 2>/dev/null
echo "[done] Removed any demo dashboard project from the Desktop"

echo "============================================================"
echo "CLASS 2 READY. Also do these by hand (30 seconds):"
echo "  1. Browser: sign OUT of Google Analytics and Supabase,"
echo "     or use a fresh browser profile (so sign-in looks new)"
echo "  2. VS Code: close any open folders"
echo "  3. Quit and reopen Claude Code"
echo "============================================================"

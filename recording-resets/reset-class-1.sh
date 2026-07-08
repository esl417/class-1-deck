#!/bin/bash
# ============================================================
#  RESET FOR CLASS 1 RECORDING
#  Run this in the Demo Student account, in Terminal, before
#  you record (or re-record) the Class 1 prereqs walkthrough.
#
#  How to run:
#     bash ~/Desktop/recording-resets/reset-class-1.sh
# ============================================================
DIR="$(cd "$(dirname "$0")" && pwd)"
source "$DIR/reset-common.sh" || exit 1

echo "Class 1 extra cleanup..."

# Class 1 has students create a website PROJECT FOLDER during class.
# Remove any practice project so you start with an empty Desktop.
# (Adjust the name if you use a different demo project name.)
rm -rf "$HOME/Desktop/my-website" 2>/dev/null
rm -rf "$HOME/Desktop/demo-site" 2>/dev/null
echo "[done] Removed any demo website project from the Desktop"

echo "============================================================"
echo "CLASS 1 READY. Now also do these by hand (30 seconds):"
echo "  1. Browser: clear history, or open a fresh browser profile"
echo "  2. VS Code: close any open folders (File > Close Folder)"
echo "  3. Quit and reopen Claude Code so it starts logged out"
echo "============================================================"

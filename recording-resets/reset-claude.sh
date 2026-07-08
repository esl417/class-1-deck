#!/bin/bash
# COMPONENT: Claude Code
# Undoes: signing into Claude Code + any memory/history/settings/agents.
# Re-shoot after this: the "open Claude Code and sign in" take.
# NOTE: also quit & reopen Claude Code after running so it shows logged-out.
source "$(cd "$(dirname "$0")" && pwd)/_guard.sh" || exit 1

rm -rf "$HOME/.claude"
rm -f  "$HOME/.claude.json" 2>/dev/null
echo "[done] Claude Code reset — logged out, memory/history/agents cleared."
echo "       Now QUIT and REOPEN Claude Code before your take."

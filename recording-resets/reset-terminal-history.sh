#!/bin/bash
# COMPONENT: Terminal history
# Undoes: commands from earlier takes showing up when you press Up-arrow
# or in the scrollback. Run before any take where the terminal is on screen.
source "$(cd "$(dirname "$0")" && pwd)/_guard.sh" || exit 1

cat /dev/null > "$HOME/.zsh_history" 2>/dev/null
history -c 2>/dev/null
echo "[done] Terminal history cleared."
echo "       Tip: also press Cmd+K in Terminal to wipe the visible scrollback."

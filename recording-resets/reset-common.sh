#!/bin/bash
# ============================================================
#  SHARED RESET — clears everything the "Demo Student" account
#  remembers about you, so a recording take starts fresh.
#  Sourced by the per-class reset scripts. Not run on its own.
# ============================================================

# --- SAFETY GUARD -------------------------------------------
# Refuse to run in Eric's real account. This protects your real
# ~/.claude (memory, agents, settings) from ever being wiped.
if [ "$(whoami)" = "ericlevine" ]; then
  echo "STOP: this is your REAL account (ericlevine)."
  echo "These resets are only for the Demo Student account. Nothing was changed."
  exit 1
fi

echo "Resetting the demo environment for user: $(whoami)"
echo "------------------------------------------------------------"

# --- Claude Code: log out + wipe memory/history/settings -----
# Removes the whole ~/.claude folder (memory, MEMORY.md, agents,
# MCP servers, saved logins, permission settings, chat history).
if [ -d "$HOME/.claude" ]; then
  rm -rf "$HOME/.claude"
  echo "[done] Claude Code reset (logged out, memory + history cleared)"
else
  echo "[skip] Claude Code already clean"
fi
# Some versions also keep a config file here:
rm -f "$HOME/.claude.json" 2>/dev/null

# --- GitHub CLI: log out ------------------------------------
if command -v gh >/dev/null 2>&1; then
  gh auth logout --hostname github.com 2>/dev/null
  echo "[done] GitHub CLI logged out"
else
  echo "[skip] GitHub CLI not found"
fi

# --- Vercel CLI: log out ------------------------------------
if command -v vercel >/dev/null 2>&1; then
  vercel logout 2>/dev/null
  echo "[done] Vercel CLI logged out"
else
  echo "[skip] Vercel CLI not found"
fi

# --- Shell history: clear the terminal's memory of past takes -
cat /dev/null > "$HOME/.zsh_history" 2>/dev/null
history -c 2>/dev/null
echo "[done] Terminal history cleared"

echo "------------------------------------------------------------"

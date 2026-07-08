#!/bin/bash
# COMPONENT: GitHub CLI login
# Undoes: the "log Claude into GitHub" take.
# Logs out locally only (does not revoke the token on github.com).
source "$(cd "$(dirname "$0")" && pwd)/_guard.sh" || exit 1

if command -v gh >/dev/null 2>&1; then
  gh auth logout --hostname github.com 2>/dev/null && \
    echo "[done] GitHub CLI logged out." || \
    echo "[note] GitHub CLI was already logged out."
else
  echo "[skip] GitHub CLI not installed yet."
fi

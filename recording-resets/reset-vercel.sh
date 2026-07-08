#!/bin/bash
# COMPONENT: Vercel CLI login
# Undoes: the "log Claude into Vercel" take.
source "$(cd "$(dirname "$0")" && pwd)/_guard.sh" || exit 1

if command -v vercel >/dev/null 2>&1; then
  vercel logout 2>/dev/null && \
    echo "[done] Vercel CLI logged out." || \
    echo "[note] Vercel CLI was already logged out."
else
  echo "[skip] Vercel CLI not installed yet."
fi

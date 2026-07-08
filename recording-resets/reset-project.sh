#!/bin/bash
# COMPONENT: The website project folder
# Undoes: the "create the project / clone / build" takes, so the
# Desktop is empty and you can start the folder from scratch again.
#
# Usage:  bash reset-project.sh <folder-name>
#   e.g.  bash reset-project.sh scubazen
# If you don't pass a name, it lists Desktop folders and does nothing.
source "$(cd "$(dirname "$0")" && pwd)/_guard.sh" || exit 1

NAME="$1"
if [ -z "$NAME" ]; then
  echo "No folder name given. Nothing deleted."
  echo "Folders currently on your Desktop:"
  ls -d "$HOME/Desktop"/*/ 2>/dev/null
  echo "Re-run like:  bash reset-project.sh scubazen"
  exit 0
fi

TARGET="$HOME/Desktop/$NAME"
if [ -d "$TARGET" ]; then
  rm -rf "$TARGET"
  echo "[done] Removed project folder: $TARGET"
else
  echo "[skip] No folder named '$NAME' on the Desktop."
fi

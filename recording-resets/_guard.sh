# Shared safety guard — sourced by every reset piece.
# Refuses to run in Eric's REAL everyday account so it can never
# wipe the real ~/.claude or log out real tools by accident.
# (In the Demo Student profile you ARE logged into real accounts,
#  so a reset there DOES log those out — that is expected.)
if [ "$(whoami)" = "ericlevine" ]; then
  echo "STOP: this is your REAL account (ericlevine). Nothing was changed."
  echo "Run resets only in the Demo Student profile."
  exit 1
fi

# Recording resets — one piece per take

Record segment-by-segment. When you flub a take, run **only** the piece that
undoes that segment — not the whole class. All scripts refuse to run in the
real `ericlevine` account; run them in the Demo Student profile.

Run any piece with:  `bash ~/Desktop/recording-resets/<script>.sh`

| Take you're re-shooting | Run this |
|---|---|
| Sign into Claude Code | `reset-claude.sh` (then quit + reopen Claude Code) |
| Log Claude into GitHub | `reset-github.sh` |
| Log Claude into Vercel | `reset-vercel.sh` |
| Sign into Cloudflare (Class 3) | `reset-cloudflare.sh` |
| Any take where the terminal is visible | `reset-terminal-history.sh` |
| Create / clone the project folder | `reset-project.sh <folder-name>` |

## Notes
- **You're using real accounts** in the Demo profile, so `reset-github` /
  `reset-vercel` / `reset-claude` log you out of your REAL accounts. That's
  fine — you just sign back in on the next take. Only run them when you
  actually want to re-shoot that login.
- Mid-build flub *after* you're already logged in? Don't reset — just
  re-record that clip. No logout needed.
- Already-installed Mac-wide tools (Homebrew, etc.) can't be reset per-profile;
  narrate them ("on a new Mac this downloads for a few minutes").
- To start a whole class over from zero, run several pieces in a row.

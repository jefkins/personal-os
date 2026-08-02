# Profile: meta-check

**Always load:** `OS.md` (north star: agent memory, auto-injected)
**Relevant scripts:** `07-scripts/core/meta-check.py`
**Notes:** Run the script first (it outputs JSON — sections: `cron`, `vault`, `email_intel`, `backup_mirror`, `disk_space`, plus `issues_found` and `health`). Read the last entry in `12-memory/meta-check-log.md` and compare — flag regressions (new cron errors, disk usage up >10%, mirror timer inactive, email intel stale). Draft a concise weekly report; if everything healthy, a one-line summary is enough. Append the run to `12-memory/meta-check-log.md` under a dated heading. Deliver to Telegram.

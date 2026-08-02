# Profile: backup-guardian

**Always load:** `OS.md` (north star: agent memory, auto-injected)
**Relevant scripts:** `07-scripts/core/backup-health-check.py`
**Notes:** Run the script first (it outputs JSON — `details` array with `status`/`detail`/`fix` per target). If `has_issues` is false → log "All backups healthy ✅". Otherwise draft a compact Telegram alert per failing target: target, status, detail, action. Append the full result to `12-memory/backup-health-log.md` under a dated entry. If the same target had the same issue in the last run, escalate: "⚠️ PERSISTENT".

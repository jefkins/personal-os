# Workflow: weekly meta-check

**Objective:** Audit all AI-OS subsystems once a week, compare with the previous week, and flag regressions before they become problems.

**Required inputs:** none (the script gathers everything; runs on the server).

## Steps

1. Run `python 07-scripts/core/meta-check.py` — the deterministic T in WAT. The script outputs JSON:

   ```json
   {
     "checked_at": "ISO timestamp", "host": "<host>",
     "cron":          {"jobs_total": int, "jobs_in_error": int, "error_details": [...]},
     "vault":         {"uncommitted": int, "dirty_files": [...], "index_md_age_hours": float|null},
     "email_intel":   {"report_count": int, "most_recent": str|null, "age_hours": float|null},
     "backup_mirror": {"mirror_timer_active": bool, "health_log_entries": int, "last_check_had_issues": bool|null},
     "disk_space":    {"/": {...}, "/mnt/backup": {...}, "/mnt/backup_mirror": {...}},
     "issues_found": int, "health": "✅ HEALTHY" | "⚠️ N ISSUES"
   }
   ```

2. Parse the JSON — the script already counts `issues_found` (cron errors, vault uncommitted, email intel >25h old, mirror timer inactive, last backup check had issues). Disk space is report-only, not counted.

3. Read the last entry in `12-memory/meta-check-log.md` — compare current vs last week:
   - `cron.jobs_in_error` increased, or new error details
   - `disk_space` usage pct increased >10% on any mount
   - `backup_mirror.mirror_timer_active` flipped true → false
   - `email_intel.age_hours` trending up (report staleness)
   - anything that was flagged last week and is still flagged → **regression**

4. Draft the report: health status, per-section summary, regressions found, suggested actions.

5. Append to `12-memory/meta-check-log.md` under `## [YYYY-MM-DD]` — the JSON summary plus your regression notes (append via `python 07-scripts/core/memory_update.py meta-check-log.md <title> <content>` if convenient).

6. Delivery: if `health` is `✅ HEALTHY` → one-line summary to Telegram. Otherwise → full report with regressions and suggested actions.

## Edge cases

- Script fails or times out → the `run()` helper returns `("", "timeout", 124)` — sections show empty/missing values. Don't report a false alarm; note "meta-check script itself failed" and check the agent's logs on the server.
- `vault.status` is `NO_GIT` → vault not on this host; not a regression, just note it (the server pulls, doesn't own the vault).
- No previous log entry (first run) → baseline; report without regression comparison.

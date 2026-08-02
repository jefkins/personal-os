# Workflow: backup health check

**Objective:** Check all backup targets across the two-machine setup, alert on
issues, and log the result so the system compounds awareness over time.

**Required inputs:** none (the script gathers everything it needs).

## Steps

1. Run `python 07-scripts/core/backup-health-check.py` — this is the
   deterministic T in WAT. The script outputs JSON:

   ```json
   { "has_issues": bool, "targets": int, "details": [{"target":..., "status":..., "detail":..., "fix":...}] }
   ```

2. Parse the JSON output — the `details` array contains one entry per backup
   target (disks, git host, cloud backups, rsync mirror, agent archives).

3. If `has_issues` is `false` → log "All backups healthy ✅" and stop. Nothing
   to alert on.

4. If `has_issues` is `true` → for each target whose status is not `"OK"`:
   - Target + status + detail → concise Telegram alert line
   - Include the `fix` field from the JSON as the concrete action

   Format:
   ```
   🔴 Backup Issue — {target}
   {status}: {detail}
   Action: {fix}
   ```

5. Append the full JSON result to `12-memory/backup-health-log.md` under a
   dated heading: `## [YYYY-MM-DD]`. If the same target had the same
   `status` in the most recent prior entry, escalate the tone:
   "⚠️ PERSISTENT — this is the N-th consecutive day."

## Edge cases

- Script exits non-zero → the issue is already captured in the JSON (the script
  always prints a report even when it finds problems). Follow the same alert
  + log path.
- SSH to the workstation unavailable → the script reports it as a status: "ERROR" target;
  the workflow handles it the same way.

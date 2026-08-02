# Profile: update manager

**Always load:** `03-engineering-os/workflows/update_manager.md`
**Script (T in WAT):** `07-scripts/core/update-check.py`
**Runtime:** cron `Update Manager Weekly` (0 9 * * 0)
**Notes:** Report available updates across the machines this OS spans, grouped by host then
package manager. Show top ~10 (security/major/key tools), not all packages.
Report-only — suggest commands, never auto-update. Host offline → note and skip.

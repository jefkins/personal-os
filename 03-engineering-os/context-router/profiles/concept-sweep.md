# Profile: concept sweep + vault consolidation

**Always load:** `03-engineering-os/workflows/concept_sweep.md`
**Relevant skill:** `vault-conventions` (paths/naming/wikilinks)
**Script (T in WAT):** `07-scripts/core/vault-consolidation-scan.py` (read-only)
**Runtime:** cron `Weekly Concept Sweep + Vault Consolidation` (0 11 * * 1)
**Notes:** PROPOSE-ONLY — never create/rename/merge/delete/modify. Verify scan
findings before proposing; read both notes before a merge proposal; check
wikilink impact via `grep [[target]]`. Max 5 proposals/week. Respect the
never-touch exclusions (daily/weekly/decisions, index/log/todo, regenerated pairs).

# Profile: weekly-summary

**Always load:** `OS.md` (north star: agent memory, auto-injected)
**Relevant scripts:** `07-scripts/core/weekly-gather.py`
**Notes:** Run the gather script first (JSON: daily notes, task-log, vault changes, git commits, closed todos, existing weekly note). Synthesize by project/topic, not by day. Write to `<vault>/notes/weekly/YYYY-MM-DD-weekly.md` (date = the week's Monday). After writing, run the vault sync script to commit + pull --rebase + push. Append a short week summary to `12-memory/decisions_log.md`.

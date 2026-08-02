# Workflow: weekly summary

**Objective:** Synthesize the past complete week (Mon–Sun) into a weekly note in the vault, so the week compounds into searchable knowledge.

**Required inputs:** none (the gather script collects everything; vault must be current).

## Steps

1. Run the gather script — the deterministic T in WAT. On a server cron job use
   a wrapper that pulls the vault first, then execs the same script. On the
   workstation run it directly:
   `python 07-scripts/core/weekly-gather.py`

2. Parse the JSON — sections:
   - `week_monday` / `week_sunday` / `week_label` (the script computes the most recent **completed** week)
   - `data.daily_notes` — 7 slots, some may be null (no note written that day)
   - `data.task_log` — task-log.jsonl entries for the week
   - `data.vault_changes` — `created` / `modified` / `decisions` / `concepts` file lists
   - `data.closed_todos` — todos closed in the week
   - `data.commits` — per-repo git commits for the week
   - `data.existing_weekly` — existing note for this week, if any
   - `summary` — one-line overview

3. If `existing_weekly` is present and comprehensive → skip and stop (no duplicate notes).

4. Generate `<vault>/notes/weekly/YYYY-MM-DD-weekly.md` (date = `week_monday`):
   - Frontmatter: `created`, `tags`, `week`, `period`, links to daily notes
   - Group content by **project/topic**, not by day
   - Include `## Created / Updated Notes` with wikilinks
   - Cross-link the daily notes in frontmatter
   - Keep it a synthesis, not a dump — the raw data stays in daily notes

5. Run the vault sync script — commit + pull --rebase + push (sync-after is mandatory; the workstation is master writer, the server pulls — a server weekly push is the one allowed exception, per vault protocol).

6. Append a short entry to `12-memory/decisions_log.md` — `## [YYYY-MM-DD] — Week summary` with the `summary` line from the gather JSON plus 1–2 lines of highlights (OS-internal scope only; personal highlights stay in the vault weekly note).

## Edge cases

- No daily notes for the week → still write the note with what exists (task-log, commits, vault changes); the summary line shows `0/7 daily notes`.
- Vault not current (pull conflicts) → run `vault-sync.sh pull` first; if it still fails, report and skip rather than force-push.
- Git commits section empty → repos may not exist on this machine (tracked repos are workstation-heavy); note it, don't treat as an error.

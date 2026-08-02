# Profile: daily note compile

**Always load:** `03-engineering-os/workflows/daily_note_compile.md`
**Relevant skill:** `vault-conventions` (canonical daily format, MANDATORY)
**Script (T in WAT):** `07-scripts/core/daily-polish-gather.py`
**Runtime:** cron `Daily Note Compile` (30 5 * * *)
**Notes:** Polish yesterday's `<vault>/notes/daily/YYYY-MM-DD.md`. Hard-wrap
~80 chars, `###` sub-headings grouped by project, bullet Summary, verify ISO
`week:`. **Preserve `## Manual Notes` verbatim.** Both formatting rules AND the
loaded skill are required — one without the other produces wall-of-text.

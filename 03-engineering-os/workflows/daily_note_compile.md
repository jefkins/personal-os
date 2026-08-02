# Workflow: daily note compile

**Objective:** Polish the previous day's Obsidian daily note into the canonical
vault format — grouped, hard-wrapped, cross-linked — without touching the
human's manual additions.

**Required inputs:** none. The gather script `07-scripts/core/daily-polish-gather.py`
(the T in WAT) collects structured context: task log, git commits, vault
changes, closed todos, planner tasks, ticket summary, and an asset-health scan.

**Runtime:** cron `Daily Note Compile` (30 5 * * *).
**Loads the `vault-conventions` skill — follow it exactly.**

## Steps

1. Read the gathered JSON context and the target note at
   `<vault>/notes/daily/YYYY-MM-DD.md`.

2. Fill the note following vault-conventions formatting **exactly**:
   - **Hard-wrap ~80 chars** — no walls of text; wrap long `- ` items with 2-space continuation indent
   - **Work section** → `###` sub-headings grouped by project/topic (not a flat list)
   - **Private section** → `###` sub-headings per topic
   - **Summary** → bullets, one per major topic (not a dense paragraph)
   - **Frontmatter `week:`** → correct ISO week (`YYYY-Www`), verified against the date
   - **Wikilinks** `[[page]]` for all cross-references

3. Populate `## Created / Updated Notes` with wikilinks to every new/modified
   vault file. `## Closed Todos` uses `- ✅ text — details` (or `_No todos
   closed today._`).

4. **Preserve `## Manual Notes` verbatim** — never touch it.

5. Asset health: if the `asset_health` context shows orphaned assets or stale
   wikilinks, add a `## Vault Health` section after `## Closed Todos` listing
   only genuinely actionable items (orphaned PDFs/guides, notable broken
   wikilinks). Skip noise (git hashes, dates, script names).

## Edge cases

- Note doesn't exist yet → the 6 AM `Daily Obsidian Journal` skeleton cron
  normally creates it first; if absent, create it in canonical format.
- Empty context (quiet day) → still produce a valid note; use the "no todos /
  routine day" fallbacks rather than inventing content.

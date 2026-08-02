# Workflow: weekly concept sweep + vault consolidation

**Objective:** Once a week, (1) surface material that deserves a standalone
concept note and (2) run the vault consolidation check — **propose-only, never
create/rename/merge/delete/modify any file.**

**Required inputs:** none. The scan script `07-scripts/core/vault-consolidation-scan.py`
(the T in WAT, read-only) outputs mechanical findings: long filenames, naming
violations, missing frontmatter/H1, same-stem notes, same-source notes, stale
`_index.md` wikilinks.

**Runtime:** cron `Weekly Concept Sweep + Vault Consolidation` (0 11 * * 1).
**Loads `vault-conventions`.**

## Steps

### Task 1 — Concept sweep
Scan the past 7 days for synthesis candidates:
1. `<vault>/notes/daily/` (last 7 days), `decisions/`, `ideas-brainstorming/`
   (recent `created` / `status: captured`), and `todo.md` for emerging topics.
2. Flag: a topic across 2+ daily notes; a decision with broader implications; a
   brainstorm referenced repeatedly; a tool/pattern/workflow learned.

### Task 2 — Consolidation check
1. **Verify scan findings** — skim flagged files; don't trust blindly
   (intentional folder/tag names are fine; date-prefixed daily/weekly/decisions are excluded).
2. **Semantic duplicates** — the scan only sees same-stem/same-source; also read
   overlapping-tag/title pairs and judge true-duplicate vs complementary. Read
   both notes before proposing a merge.
3. **Propose (never apply):** merges (canonical target, what folds in, wikilink
   impact via `grep [[target]]` first), renames (lowercase-hyphens + index
   updates), frontmatter fixes, stale-link resolutions.

**Exclusions (never touch):** `daily/`, `weekly/`, `decisions/` (date-prefixed
by design); `_index.md`/`_log.md`/`todo.md`; `CLAUDE.md/` folders;
`tools-to-evaluate.md` ↔ `tool-matrix.md` (cron-regenerated — never merge).

## Report

Sections: `Candidates for Concept Notes` · `Consolidation Proposals` ·
`Orphaned Content` · `Cross-Links to Add` · `Summary`. **Max 5 proposals/week** —
quality over quantity. Nothing found → "Vault is clean ✅".

## Rules

1. PROPOSE-ONLY — the human applies changes in a session (step-by-step approval).
2. Proposed paths follow vault conventions (`concepts/`, `entities/`, etc.).
3. Cross-reference `notes/_index.md` to avoid duplicate proposals.
4. Be specific ("daily notes Jul 28-30 discuss n8n error handling"), not vague.


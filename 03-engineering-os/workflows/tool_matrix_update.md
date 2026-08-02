# Workflow: weekly tool matrix update

**Objective:** Keep `notes/tools/tool-matrix.md` current — add new tools from
the source list, refresh pricing, and keep the credential-status column accurate.

**Required inputs:** none. The gather script `07-scripts/core/tool-matrix-gather.py`
(the T in WAT) writes `<config>/tool-matrix-context.json`:
`tools[]` (from `tools-to-evaluate.md`), `statuses{}` (credential/CLI detection
WITHOUT reading secret values), `configured[]`, `not_configured[]`.

**Runtime:** cron `Weekly Tool Matrix Update` (0 9 * * 1).

## Files

1. Source list: `<vault>/notes/tools/tools-to-evaluate.md` (master)
2. Target: `<vault>/notes/tools/tool-matrix.md` (regenerated)
3. Context: `<config>/tool-matrix-context.json`

## Steps

1. Read the source list, the context JSON, and the current matrix.
2. Compare all three — add new tools, remove stale ones, update status icons.
3. New tool → research pricing via **browser** (never fabricate; "Contact for
   pricing" if unfound), assign category, write summary + use cases + comparison.
4. Existing tool → update pricing if changed, refresh status icon from context.
5. **Status column** (every pricing table): ✅ = credentials/config/CLI found ·
   ❌ = not found · — = OSS/no signup · ❔ = uncertain. Drive from `statuses[name]`.
6. Add `[[wikilinks]]` to related tools that already have vault notes (check
   `_index.md`); update the frontmatter `updated` field.

## Categories (maintain; add as needed)

Web Scraping & Data Extraction · AI API Gateways & Cost Optimization · AI Video
& Image Generation · Productivity & Project Management · Backend / Database /
Hosting · AI Agent Intermediaries & Human-in-Loop · Social Media & Content
Automation · Diagram & Whiteboard · Voice AI · Network Tunneling · Background
Jobs & Workflow Engines · CLI Agent Plugins & Skills.

## Verification

- Every tool from `tools-to-evaluate.md` is represented.
- Frontmatter `source` links back to `tools-to-evaluate`.
- Pricing current; status icons match context data.

## Edge cases

- Pricing page unreachable → "Contact for pricing", don't guess.
- `tools-to-evaluate.md` ↔ `tool-matrix.md` are a regenerated pair — never merge
  them (see concept_sweep exclusions).

# Profile: tool matrix update

**Always load:** `03-engineering-os/workflows/tool_matrix_update.md`
**Script (T in WAT):** `07-scripts/core/tool-matrix-gather.py`
  → context `<config>/tool-matrix-context.json`
**Runtime:** cron `Weekly Tool Matrix Update` (0 9 * * 1)
**Notes:** Regenerate `notes/tools/tool-matrix.md` from `tools-to-evaluate.md`.
Research pricing via browser — never fabricate. Keep the ✅/❌/—/❔ status column
accurate from the context JSON. Never merge the source↔matrix pair.

# CLAUDE.md — Claude Code entry point

Read `OS.md` first — it is the operating contract and overrides defaults.

Claude Code-specific rules:
- Invoke the `os-practice` skill
  (`03-engineering-os/skills/os-practice.md`) at session start
- Run scripts from the repo root: `python 07-scripts/<domain>/<script>.py`
- Never `git add -A` — stage files explicitly
- `.env` is gitignored; never stage it

Then route your intent: `03-engineering-os/context-router/intent-map.md`

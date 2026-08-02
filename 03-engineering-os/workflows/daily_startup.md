# Workflow: daily startup

**Objective:** start the day oriented, with valid credentials and clear priorities.
**Required inputs:** none.

## Steps
1. Run `python 07-scripts/core/check_env.py` — fix any missing credentials first
2. Re-anchor on the north star: agent memory (auto-injected) + vault `notes/ai/os/<your-os>.md`
3. Read the last entry in `12-memory/decisions_log.md` (OS-internal decisions)
4. Check the vault's `todo.md` — list top 3 priorities for today
5. Write today's 3 priorities to `.tmp/today.md`
6. Route the first task: `03-engineering-os/context-router/intent-map.md`

## Edge cases
- check_env fails on a key you no longer use → remove it from `.env.example`
- No north star in memory / vault → stop and write 5 lines in the vault `notes/ai/os/<your-os>.md`. Everything else can wait.
- Two-machine check: ping the machines the OS spans before proceeding — if one is unreachable, note it in `.tmp/today.md` and continue with the reachable one.

# Workflow: daily startup

**Objective:** start the day oriented, with valid credentials and clear priorities.
**Required inputs:** none.

## Steps
1. Run `python 07-scripts/core/check_env.py` — fix any missing credentials first
2. Read `12-memory/strategy.md` — re-anchor on where this is all going
3. Read the last entry in `12-memory/decisions_log.md`
4. List today's 3 priorities — write them to `.tmp/today.md`
5. Route the first task: `03-engineering-os/context-router/intent-map.md`

## Edge cases
- check_env fails on a key you no longer use → remove it from `.env.example`
- No strategy written yet → stop and write 5 lines. Everything else can wait.

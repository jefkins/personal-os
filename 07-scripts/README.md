# 07-scripts — deterministic tools (the T in WAT)

Plain Python. Each script: does one thing, reads config from `.env`, run from
the repo root, prints what it did.

- `core/check_env.py` — validate credentials before a session
- `core/memory_update.py` — append a structured entry to a memory file

Grow by domain: `07-scripts/<domain>/<tool>.py` — and add a row to `OS.md`'s
script map in the same commit (parity rule).

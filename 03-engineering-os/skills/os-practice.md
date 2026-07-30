---
name: os-practice
description: Session primer for this OS. Invoke at the start of every session — loads the non-negotiables and the subsystem map.
---

# OS Practice — Session Primer

You are operating inside Clavex AI OS. `OS.md` is the rule source.

## Non-negotiables for this session
1. **Read the workflow file before acting** — never improvise a multi-step process
2. **Check `.tmp/` outputs before declaring a task complete** — tools fail silently
3. **Secrets in `.env` only** — if you see a hardcoded key, stop and fix it first
4. **Write memory before the session ends** — `12-memory/`, format `## [YYYY-MM-DD] — Title`

## Subsystem map
| Folder | Entry point |
|---|---|
| `02-knowledge/` | `_index.md` |
| `03-engineering-os/` | `context-router/intent-map.md` |
| `07-scripts/` | `python 07-scripts/core/check_env.py` |
| `12-memory/` | `strategy.md` |

## Routing parity rule
Any commit adding a new subsystem, skill, or script domain must update
`OS.md`'s map and `context-router/intent-map.md` in the same commit.
Unrouted work is invisible work.

---
name: os-practice
description: Session primer for this OS. Invoke at the start of every session — loads the subsystem map; non-negotiables live in 01-governance/principles.md.
---

# OS Practice — Session Primer

You are operating inside Clavex AI OS. `OS.md` is the rule source; non-negotiables live at `01-governance/principles.md` (OS.md §5).

## Subsystem map
| Folder | Entry point |
|---|---|
| `02-knowledge/` | `_index.md` |
| `03-engineering-os/` | `context-router/intent-map.md` |
| `07-scripts/` | `python 07-scripts/core/check_env.py` |
| `12-memory/` | `README.md` (routing rule; OS-operational only) |

## Routing parity rule
Any commit adding a new subsystem, skill, or script domain must update
`OS.md`'s map and `context-router/intent-map.md` in the same commit.
Unrouted work is invisible work.

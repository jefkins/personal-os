# 12-memory — OS-operational memory (the compounding loop)

> **This OS may have memory systems OUTSIDE this repo.** `12-memory/` is not
> necessarily the only place memory lives, so it is **OS-operational-only** —
> the routing split below is the boundary. Personal memory routes to the
> agent's memory tool + your notes vault.

## What goes where

| Memory | Home | Why |
|---|---|---|
| **Personal / strategic** (your north star, personal decisions, personal ideas) | **Agent memory tool** (auto-injected every turn) + **vault** `notes/decisions/`, `notes/ideas-brainstorming/` | You are the subject; the agent always needs it in context, and the vault is where your synthesis lives |
| **OS-internal decisions** (architecture/process changes to this OS) | **`decisions_log.md`** | OS machinery, not personal life |
| **OS-internal lessons** (pitfalls, API quirks, breakage root-causes) | **`lessons_learned.md`** | OS machinery, not personal life |
| **OS health logs** (cron-run state, backup checks, meta-checks) | **`backup-health-log.md`**, **`meta-check-log.md`** | Written by deterministic workflows, appended on a schedule |

The OS gets smarter only if sessions write back what they learned — but the
**write-back goes to the right store**: personal → agent memory / vault;
OS-operational → here.

## Files in this layer

| File | What goes in |
|---|---|
| `decisions_log.md` | OS-internal decisions — architecture/process changes to this OS, with the reasoning |
| `lessons_learned.md` | OS-internal lessons — what broke, what you learned, what changed (in the OS) |
| `backup-health-log.md` | Compounding log for the Backup Guardian workflow (cron-appended) |
| `meta-check-log.md` | Compounding log for the AI-OS Meta-Check workflow (cron-appended) |

## Format

Always `## [YYYY-MM-DD] — Title`.

Append via: `python 07-scripts/core/memory_update.py <file> <title> <content>`
(`memory_update.py` discovers files dynamically — any `*.md` here works).

## Routing rule (check before writing)

1. Is it about **you** (strategy, personal decision, personal idea, something you learned about life/work)? → **agent memory tool** + vault (`notes/decisions/`, `notes/ideas-brainstorming/`). Not here.
2. Is it about **this OS** (decision/lesson re: the skeleton, workflows, scripts, infra)? → `decisions_log.md` / `lessons_learned.md`.
3. Is it **operational run-state** from a scheduled workflow? → the matching health log.
4. Unsure → default to agent memory + vault; this layer is the OS's, not yours.

## Archived

`strategy.md` (personal north star) and `ideas_vault.md` (empty personal stub)
were archived to `11-archive/12-memory-legacy/` — their content belongs in
agent memory + the vault, per the routing rule above. History is preserved, not
deleted.

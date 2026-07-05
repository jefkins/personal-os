---
name: route-context
description: Identify the task intent and load only the context it needs. Use at session start and whenever the task type changes.
---

# Route Context

> Identify the intent. Load only what the task needs. Begin with precision.

## Process
1. **Identify intent** — what is being produced, for whom, in what domain?
   Unclear → ask one scoping question before loading anything.
2. **Match** against `03-engine/context-router/intent-map.md`
3. **Load** only the files the matched profile lists
4. **Before building anything**, check for existing assets:
   `10-templates/` → `03-engine/skills/` → `07-scripts/`. Reuse before rebuild.
5. **Task type changes mid-session** → re-route from step 1.

## Principle
Minimum viable context. A 200-file repo loaded into context is not power,
it's noise. The router is what keeps sessions sharp.

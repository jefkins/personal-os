---
created: 2026-08-01
tags: [os-internal, delivery, client-handoff, policy]
sources:
  - "05-delivery-os/README.md"
  - "OS.md"
  - "01-governance/principles.md"
last_verified: 2026-08-01
---

# Client Handoff Policy

OS-internal domain policy: what a controlled handover requires before delivery
counts as "done." Grounds the `05-delivery-os` → `06-clients` transition.

> **Draft policy — placeholder.** Seeded so the delivery domain has a real
> `02-knowledge` entry and the routing/index parity is demonstrated. Replace the
> checklist below with the actual handover standard when the delivery pipeline
> is built out.

## When it applies

At the pre-signature → post-signature boundary: commercial machinery lives in
`05-delivery-os/`; the moment work is scoped and signed, it moves to
`06-clients/` (gitignored — client data never enters git or AI context per
governance rule 2).

## Handover checklist (draft)

1. **Scope frozen** — deliverable, acceptance criteria, and exclusions written down
2. **Governance clear** — no secrets in deliverables; no client PII in AI context
3. **Artifact verified** — "done" means a working, verified artifact, not a description of one (governance refusal rule)
4. **Human sign-off** — consequential delivery gets explicit human approval before it ships
5. **Memory written** — OS decisions + lessons banked to `12-memory/`; personal/client outcomes to agent memory + the vault before the engagement closes

## Boundary note

This is *policy* (how delivery should run), not client data (which never leaves
`06-clients/`) and not general delivery knowledge (which, if it's synthesis,
belongs in the vault). It sits here because it's an OS operating rule the agent
must apply mid-task.

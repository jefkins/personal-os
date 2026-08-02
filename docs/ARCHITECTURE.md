# Clavex AI OS — 12-layer architecture

Clavex AI OS separates authority, knowledge, reasoning, execution and memory so
an AI-assisted process remains understandable, repeatable and portable across
AI providers.

## The 12 layers

| Layer | Responsibility | Key boundary |
|---|---|---|
| `01-governance/` | Principles, policies, approvals and non-negotiables | Rules belong here; task execution does not |
| `02-knowledge/` | Trusted domain context and internal synthesis | Knowledge informs work; it does not execute it |
| `03-engineering-os/` | Context routing, skills, workflows and agent instructions | Orchestrates work; deterministic execution belongs in scripts |
| `04-clavex-os-product/` | Reusable capabilities, modules and product architecture | Shared capability stays separate from bespoke delivery |
| `05-delivery-os/` | Pipeline, scoping, projects and controlled handovers | Engagement context belongs here before or during delivery |
| `06-clients/` | Isolated client workspaces and sensitive context | Client boundaries must remain explicit |
| `07-scripts/` | Tested, deterministic tools and integrations | Code executes; it does not decide business policy |
| `08-references/` | External standards, source documents and official guidance | Preserve sources separately from internal synthesis |
| `09-deployments/` | Development, staging and production release state | Records environments and versions; never stores secrets |
| `10-templates/` | Approved reusable starting points | Encode standards without duplicating live records |
| `11-archive/` | Retired versions and historical material | Preserve history without routing active work through it |
| `12-memory/` | OS-operational memory: decisions, lessons, health logs | Captures learning so future sessions start stronger |

## How a request moves

```text
Request
  ↓
OS.md operating contract
  ↓
Governance constraints + relevant knowledge
  ↓
Engineering OS routes the workflow and agent
  ↓
Scripts execute deterministic actions
  ↓
Output is tested, reviewed and released
  ↓
Useful decisions and lessons return to memory
```

## Why it is AI-provider-agnostic

Claude Code, Codex, Gemini and future AI harnesses read the same `OS.md`
contract. Workflows, skills and routing rules are plain markdown. Deterministic
actions live in ordinary scripts. Provider-specific entry files remain thin
adapters, so changing the AI model does not require rebuilding the operating
system.

The separation is intentional:

- AI reasons, routes and coordinates.
- Workflows define the approved method.
- Scripts execute repeatable actions.
- Humans remain accountable for consequential decisions.

## Extension rule

Add a new layer only when an existing layer cannot own the responsibility
without losing a clear boundary. Whenever the structure changes, update
`README.md`, `OS.md` and `03-engineering-os/context-router/intent-map.md` in
the same commit.

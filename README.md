# Personal OS

> A hackable, file-based AI operating system for your life and business.
> Built on the **WAT framework**: Workflows → Agents → Tools.

Personal OS is the public skeleton of a real system — [Clavex OS] — that runs a
UK AI-automation company end to end: client delivery, compliance, content,
memory, and autonomous pipelines. This repo is that architecture with the
business stripped out, so you can clone it and make it yours in minutes.

## Why this exists

Most people use AI as a chat window. The results are impressive one message at
a time and unreliable across a real process. The fix is architectural, not a
better prompt:

- **Workflows** (markdown SOPs) say *what* to do and in what order
- **Agents** (Claude Code, Codex, Gemini — any harness) decide and coordinate
- **Tools** (plain Python scripts) execute deterministically

If each improvised AI step is 90% accurate, a five-step process succeeds 59%
of the time. Move execution into deterministic tools and the agent only has to
orchestrate — that's how this stays reliable.

## Quickstart (10 minutes)

```bash
git clone https://github.com/jefkins/personal-os.git my-os
cd my-os
cp .env.example .env          # add your API keys
```

1. Open the folder in your AI coding tool (Claude Code, Codex CLI, Gemini CLI)
2. It reads `CLAUDE.md` / `AGENTS.md` / `GEMINI.md` → which point to `OS.md`,
   the operating contract
3. Say: *"Read OS.md and run the daily startup workflow"*
4. Start replacing placeholders with your own life/business — see
   `docs/GETTING-STARTED.md`

## The structure

| Folder | What lives there |
|---|---|
| `01-governance/` | Your rules: principles, policies, non-negotiables |
| `02-knowledge/` | Domain knowledge the AI should draw on |
| `03-engine/` | The OS machinery: skills, workflows, context routing |
| `04-product/` | What you're building |
| `05-delivery/` | How work goes out: pipeline, proposals, projects |
| `06-clients/` | Per-client workspaces (gitignored — client data never commits) |
| `07-scripts/` | Deterministic Python tools — the T in WAT |
| `08-references/` | External standards and source material |
| `10-templates/` | Reusable starting points |
| `11-archive/` | Retired content — nothing is deleted, it's archived |
| `12-memory/` | Persistent memory: strategy, decisions, lessons, ideas |

Numbering is deliberate: it fixes the order in listings, gives every concern
one home, and leaves gaps to grow into (the private OS this comes from is at
16 subsystems and counting).

## Core ideas worth stealing even if you don't clone

1. **One operating contract** (`OS.md`) every AI harness reads first —
   AI-agnostic by design
2. **Intent routing** (`03-engine/context-router/`) — load only the context
   the task needs, not the whole repo
3. **File-based memory** (`12-memory/`) — the system gets smarter because
   sessions write back what they learned
4. **Skills as plain markdown** — processes any AI can follow, no vendor lock-in
5. **Secrets in `.env` only** — enforced by contract and .gitignore

## Author

Built by **Jefkins Nwabenu** — founder of Clavex AI Solutions Ltd, applying AI
automation to the UK health & social care sector.
LinkedIn: https://www.linkedin.com/in/jefkins-nwabenu-digital-ai

MIT licensed. Fork it, gut it, make it yours. If it helps you, a star helps
others find it.

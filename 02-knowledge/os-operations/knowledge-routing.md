---
created: 2026-08-01
tags: [os-internal, knowledge-routing, retrieval, architecture]
sources:
  - "02-knowledge/README.md"
last_verified: 2026-08-01
---

# Knowledge Routing — where each kind of knowledge lives

Operational brief for the agent: an OS may have **external** knowledge stores
besides this repo. Route retrieval to the right one instead of assuming a
single store.

## The surfaces

| Surface | Role | Retrieval | Indexes the others? |
|---|---|---|---|
| **02-knowledge** (this layer) | OS-internal operational briefs | `02-knowledge/_index.md` | no |
| **Notes vault** (e.g. Obsidian) | Write / synthesis — hand-authored notes, concepts, decisions | vault index + filename search | no |
| **Reference corpus / KB app** | Read / reference — collected docs, RAG + FTS | its own search tools | no |

**Disjoint by design.** A KB app's search does **not** see the vault; the vault
index does **not** see the KB corpus. No surface is "the single source of
truth" — they cover different material.

## Routing order

1. **OS-internal** (how this repo/layers/routing work, domain policy) → `02-knowledge/_index.md`
2. **Synthesis** (something you concluded, decided, or wrote up) → the vault index
3. **Reference** (source material, books, articles, transcripts) → the KB app
4. **Nowhere** → research fresh, then bank in the correct store (vault if synthesis, here if OS-internal)

## Why this brief exists here and not in the vault

It describes how *this OS* routes retrieval — it's operational machinery the
agent needs mid-task inside the repo, not personal synthesis. That's the
02-knowledge boundary.

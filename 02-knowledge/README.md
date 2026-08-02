# 02-knowledge — what the AI should know

Domain knowledge the AI draws on before producing anything domain-specific.

> **This OS may have knowledge stores OUTSIDE this repo.** `02-knowledge` is
> not necessarily the only place knowledge lives, so it is a **router +
> OS-internal briefs layer**, not a general knowledge dump. Read the routing
> rule below before writing anything here.

## The external knowledge stores (neither is this folder)

| Store | Role | Content | Retrieval |
|---|---|---|---|
| **Notes vault** (e.g. Obsidian) | **Write / synthesis** | Hand-authored notes, concepts, entities, projects, decisions, daily/weekly | The vault's index first, then filename search |
| **Reference corpus / KB app** | **Read / reference** | Collected docs (ebooks, HTML clips, articles, interviews, transcripts) with search + RAG | Its own search / chat tools |

**Critical:** the stores are **disjoint**. A KB app's search searches only its
own corpus — it does **not** index the vault. Combined, the vault (what you
wrote) + the KB app (source material you collected) form the full knowledge
base. Do not treat the vault as a single source of truth.

## What belongs in 02-knowledge

Only **OS-internal operational briefs** — things the agent needs *mid-task,
inside this repo,* that neither the vault nor the KB app serves:

- How this OS's own layers, routing, and operating loop work
- Domain policies specific to running the OS (delivery, client-handoff rules)
- Decision-ready research summaries produced via
  `03-engineering-os/workflows/example_research_summary.md`

General personal / business / technical knowledge does **not** go here — it
already has homes (vault + KB app). Duplicating it here creates a split-brain.

## Retrieval routing (check in this order)

1. **OS-internal operational question** → `02-knowledge/_index.md` → the brief
2. **Your own synthesis / notes / decisions** → the notes vault
3. **Source material / reference / research corpus** → the KB app
4. **Found nowhere** → research fresh (per the research-summary workflow), then
   bank it in the *correct* store: vault if it's synthesis, `02-knowledge` if
   it's OS-internal. Retrieval that doesn't compound is wasted.

## File conventions (for notes written here)

- **Path:** `02-knowledge/<domain>/<topic>.md`, lowercase-hyphens filenames
- **Frontmatter (required):** `created: YYYY-MM-DD`, `tags: [...]`,
  `sources: [...]` (URLs — no source, no note), `last_verified: YYYY-MM-DD`
- **Cross-link:** `related::` to connected briefs / vault notes
- **Freshness:** when a brief goes stale, move it to `11-archive/` — never
  silently rot; never delete
- **Index parity:** a new brief updates `_index.md` in the same commit
  (mirror of the routing-parity rule — unrouted knowledge is invisible)
- **Write gate:** propose new briefs; the human approves consequential ones

## Index model — decided

`02-knowledge/_index.md` is **dedicated to OS-internal knowledge only**.
It catalogs *only* briefs that live nowhere else — disjoint from the vault, so
the indices never overlap and the parity burden stays minimal. Everything
personal / business / technical / reference routes out to the vault or the KB
app (see the routing rule above) and gets **no row here**.


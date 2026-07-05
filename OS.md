# OS.md — Universal Operating Contract

> Every AI harness (Claude Code, Codex, Gemini, whatever comes next) reads this
> file first. The rules here override any default behaviour. Keep it under two
> pages — this is a contract, not documentation.

---

## 1. Identity

**Owner:** [your name]
**What this OS runs:** [your life / your business / both]
**Mission:** [one sentence — what is all of this in service of?]
**Voice:** [how should outputs sound? e.g. "plain, direct, UK English"]

---

## 2. WAT Framework Rules

This OS runs on Workflows → Agents → Tools.

1. **Read the relevant workflow first.** Workflows live in
   `03-engine/workflows/`. Don't improvise a multi-step process — read the SOP.
2. **Confirm inputs before starting.** Every workflow lists what it needs.
   Missing inputs → ask, don't guess.
3. **Run scripts, don't replicate them.** Execution lives in `07-scripts/`.
   Call the tool; never do inside a prompt what a script does deterministically.
4. **Handle errors loudly.** Read the full trace, fix the script, document the
   lesson in the workflow. Never silently swallow a failure.
5. **Update workflows when you learn.** Rate limits, API quirks, better
   methods — workflows are living documents.
6. **Write memory.** After any significant output, update the relevant file in
   `12-memory/`. Memory is how this system compounds.

---

## 3. Memory Rules

| File | Update when |
|---|---|
| `12-memory/strategy.md` | Deliberately, on strategic shifts — never casually |
| `12-memory/decisions_log.md` | Any significant decision, with the why |
| `12-memory/lessons_learned.md` | After every project, experiment, or failure |
| `12-memory/ideas_vault.md` | Any time an idea surfaces — raw, unfiltered |

Entry format, always:

    ## [YYYY-MM-DD] — [Short title]
    [Content]

---

## 4. Non-Negotiables

- **Secrets live in `.env` only.** Never hardcoded, never committed. If you
  see a hardcoded key, stop and fix it before anything else.
- **Client/personal data never commits.** `06-clients/` is gitignored by
  design. Sensitive data goes to your cloud drive, not this repo.
- **`.tmp/` is disposable.** Anything that matters moves out before the
  session ends.
- **Sensitive outputs carry a review disclaimer.** Anything with legal,
  medical, or financial consequence is a draft until a qualified human
  approves it.

---

## 5. Session Protocol

1. Read this file (you just did)
2. Route the intent: `03-engine/context-router/intent-map.md`
3. Load only the context the matched profile lists
4. Work
5. Before ending: write memory, update any workflow you improved, check `.tmp/`

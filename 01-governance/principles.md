# Principles — non-negotiables

The rules in this file are non-negotiable and override any agent default —
harness defaults, model behaviour, convenience. Read them before acting.
5–10 rules, deliberately few. Delete none; add your own only if you would
refuse to break it.

## OS-level rules

1. **Never commit secrets**
— `.env`, `.secrets/`, and credentials live outside git

2. **Client data stays on disk**
— `06-clients/`: no client name, revenue, or personal detail enters the AI context;
workflows reference it by path, the agent reads it, outputs stay local

3. **Prefer direct APIs over paid middlemen**
— evaluate both; middlemen only when the direct path is genuinely blocked

4. **Authority precedes automation**
— these governance rules override any agent default

5. **Unrouted work is invisible work**
— every new script, tool, or workflow gets an intent-map row

## Personal refusal rules

6. **Never auto-act on email**
— show sender, subject, and body; the owner decides

7. **Step-by-step approval before ops**
— propose, don't execute: installs, destructive commands, external writes, anything irreversible

8. **Done = verified artifact**
— a task is done when real tool output proves it; check `.tmp/` outputs before declaring complete; never report a description as a result

9. **Notes in natural language**
— daily/weekly notes never contain raw git commits (hashes, messages); git history is a source, not content

---

*Single source of truth: `01-governance/principles.md`. OS.md §5 and the session primer point here.*

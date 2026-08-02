# Intent Map — master routing table

> Match the intent, load the profile/workflow, begin. No match → ask one
> scoping question.

Every routable capability lives here (routing-parity rule: *unrouted work is
invisible work*). Rows point at a **profile** (loads context + workflow) or a
**skill**. Deterministic `no_agent` watchdogs have no context to load — they're
listed at the bottom for visibility, but they route to a cron/script, not a profile.

## Agent-driven capabilities (profile-routed)

| Intent | Trigger keywords | Load |
|---|---|---|
| Session startup | start, morning, check env | `profiles/daily-session.md` |
| Build a script/tool | script, python, automate, tool | `profiles/build.md` |
| Look something up | find, research, what is, knowledge | `profiles/knowledge.md` |
| Email intelligence | email, inbox, mail, triage | `profiles/email-intel.md` |
| Daily note compile | daily note, journal, polish, compile | `profiles/daily-note-compile.md` |
| Concept sweep / vault cleanup | concept, consolidate, vault sweep, dedupe | `profiles/concept-sweep.md` |
| Tool matrix update | tools, tool matrix, evaluate, pricing | `profiles/tool-matrix.md` |
| Update manager | updates, packages, upgrade, patches | `profiles/update-manager.md` |
| Weekly summary | weekly, summary, recap, review | `profiles/weekly-summary.md` |
| Backup health check | backup, guardian, health, disk | `profiles/backup-guardian.md` |
| Weekly meta-check | meta, health, audit, subsystems | `profiles/meta-check.md` |
| Cron health check | cron, jobs, scheduler health | your agent's cron tool (list jobs) |

## Content monitors (agent-light, script-gathered)

| Intent | Trigger keywords | Load |
|---|---|---|
| Breaking changes watch | breaking changes, deprecations | cron `Breaking Changes Daily` (breaking-changes.py) |
| (add your own) | (add your own) | (cron + gather script) |

## Deterministic watchdogs (no_agent — cron only, not profile-routed)

Listed for visibility; these run as pure scripts on a schedule and need no
context loading. Manage via `cronjob` / the agent's scheduler, not the router.

| Capability | Script | Schedule |
|---|---|---|
| Daily journal skeleton | `daily-journal.py` | 0 6 * * * |
| Vault dirty check | `obsidian-dirty-check.py` | 0 7 * * * |
| Watch todo.md / schema.md | `todo-md-watch.py` / `schema-md-watch.py` | every 30m |
| Capabilities inventory sync | `capabilities-update.py` | every 6h |
| (add your own) | (your script) | (your schedule) |

**Priority when intents collide:** riskier context loads first —
Governance/Compliance > Delivery > Deadline-bound > Build > Content > everything
else.

**Skills are first-class route targets** — a row may point at a skill (e.g.
`vault-conventions`, `email-workflow`) instead of a profile.

> **Promotion note:** email-intel, daily-note-compile, concept-sweep,
> tool-matrix, and update-manager were promoted from inline cron prompts to full
> Clavex profiles + workflows. The cron still owns the schedule; the
> profile/workflow now owns the procedure (versioned in git, reusable from a
> chat). See `docs/FLOW.md`.

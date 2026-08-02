# Profile: email intelligence

**Always load:** `OS.md`, `01-governance/principles.md` (email non-negotiable),
`03-engineering-os/workflows/email_intelligence.md`
**Relevant skill:** `email-workflow` (CLI client, VIP/whitelist rules)
**Script (T in WAT):** `07-scripts/core/email-intelligence-gather.py`
**Runtime:** cron `Email Intelligence Daily` (30 7 * * *)
**Notes:** Never auto-act on email — propose one action per message, the human
decides. Run the gather script, then follow the workflow. Zero emails → "Inbox
zero today ✅".

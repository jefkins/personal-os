# Workflow: daily email intelligence

**Objective:** Process the day's inbox into a structured, actionable report —
propose (never execute) an action per email so the human decides in seconds.

**Required inputs:** none. The gather script `07-scripts/core/email-intelligence-gather.py`
(the T in WAT) outputs JSON with today's emails: sender, subject, date, folder,
signal flags, and body previews (first 500 chars) for the top 15.

**Runtime:** cron `Email Intelligence Daily` (30 7 * * *).
Governance rule: *never auto-act on email* (`01-governance/principles.md`).

## Steps

1. Read VIP config `<config>/email-vips.yaml` for sender patterns and
   `folder_rules`. If a frequent/important sender isn't listed, suggest adding.

2. For each email, propose exactly ONE action — never execute:
   - 🗑️ **Delete** — spam, noise, one-time notifications, unengaged marketing
   - 📁 **Move to folder** — per `folder_rules` (e.g. substack.com → `INBOX.$$$substack+lists`); suggest new rules on patterns
   - 🧠 **KB Ingest** — email carries an article URL worth saving; note topic+URL (run your KB ingest command, propose only)
   - 👁️ **Mark as read** — summary was enough, no action
   - 📌 **Needs attention** — the human should read/reply; keep in inbox

3. Write the report to `<tmp>/daily-email/intel-{today}.md` **and** print a
   compact version inline in the final response (not just "saved to file").

   Report sections: `📌 Needs Attention` · `📰 Newsletters` · `🔔 Notifications`
   · `🗑️ Suggested Deletes` · `📊 Extracted` (appointments, KB candidates,
   potential VIPs, folder rules to create).

## Rules

1. Never auto-execute — propose, the human reviews and approves.
2. Delivery notifications (courier, DHL, …) → 📌 Needs Attention.
3. Newsletter with no body preview → 👁️ Mark as read.
4. Marketing/promo → 🗑️ Delete.
5. Body previews are enough to decide — don't fetch more.
6. Zero emails → "Inbox zero today ✅" and stop.

## Edge cases

- `email-vips.yaml` missing → note it, proceed with no VIPs, suggest creating it.
- Gather script returns 0 emails → inbox-zero path (rule 6).

# Intent Map — master routing table

> Match the intent, load the profile, begin. No match → ask one scoping question.

| Intent | Trigger keywords | Load |
|---|---|---|
| Session startup | start, morning, check env | `profiles/daily-session.md` |
| Build a script/tool | script, python, automate, tool | `profiles/build.md` |
| Look something up | find, research, what is, knowledge | `profiles/knowledge.md` |
| [your intent] | [your triggers] | [your profile or skill] |

**Priority when intents collide:** riskier context loads first. Define your
own order (the private OS this comes from uses:
Compliance > Delivery > Deadline-bound > Build > Content > everything else).

**Skills are first-class route targets** — a row may point at a skill in
`03-engine/skills/` instead of a profile.

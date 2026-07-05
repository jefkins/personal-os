# Getting Started — make it yours

The skeleton works out of the box, but it becomes powerful when you replace
the placeholders with your reality. Work through this checklist.

## 1. The contract (10 min)
- [ ] Open `OS.md` → fill in Identity: who you are, what this OS runs, mission, voice
- [ ] Read the Non-Negotiables — delete none, add your own

## 2. Credentials (5 min)
- [ ] `cp .env.example .env`, add the keys for platforms you actually use
- [ ] Run `python 07-scripts/core/check_env.py` — it validates what's present

## 3. Memory (5 min)
- [ ] `12-memory/strategy.md` — write 5 lines: where you're going and why
- [ ] From now on, end sessions by writing to memory. That's the compounding loop.

## 4. First workflow run
Tell your AI harness:
> "Read OS.md, then run 03-engine/workflows/daily_startup.md"

## 5. Grow it
- New repeatable process → write a workflow in `03-engine/workflows/`
- New deterministic task → write a script in `07-scripts/`
- New process an AI should follow → write a skill in `03-engine/skills/`
- New subsystem → new numbered folder + one row in `OS.md`'s map
  (**routing parity rule**: if the routing docs don't know about it, no AI can find it)

## The one habit that matters
Every failure: fix the tool → verify → document the lesson in the workflow →
move on with a more robust system. That loop is the whole game.

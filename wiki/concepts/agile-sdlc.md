---
tags: [agile, scrum, kanban, sdlc, process]
status: done
phase: 7
updated: 2026-06-01
---

# Agile / Scrum / Kanban / SDLC

## What it is
Ways of organizing software delivery. **Agile** = iterative, incremental delivery
with feedback (vs big-bang waterfall). **Scrum** and **Kanban** are two Agile
frameworks.

## How it maps to what I already know
This whole bootcamp was run as Agile: a **Kanban board** (GitHub Projects) with
the work broken into phase "cards" moving Backlog → In progress → Done. That's a
concrete story I can tell.

## Key terms (say these confidently)
**SDLC** (Software Dev Life Cycle): Plan → Design → Develop → Test → Deploy →
Maintain. CI/CD automates the Develop→Test→Deploy part.

**Scrum:**
- *Roles:* Product Owner (what/priority), Scrum Master (process/unblock), Dev Team.
- *Artifacts:* Product Backlog, Sprint Backlog, Increment.
- *Ceremonies:* Sprint Planning, Daily Standup, Sprint Review (demo), Retrospective.
- *Sprint:* fixed timebox (1–4 wks) producing a shippable increment.

**Kanban:**
- Continuous flow (no fixed sprints); visualize work on a board.
- **WIP limits** (cap items "In progress") to expose bottlenecks.
- Pull-based: pick up the next item when you have capacity.

**Scrum vs Kanban:** Scrum = timeboxed sprints + roles + ceremonies; Kanban =
continuous flow + WIP limits, lighter process. Many teams blend them ("Scrumban").

## Likely interview Q&A
- **Q: How do you work in a team?** A: Agile — I take work off a prioritized
  board, keep WIP low, demo increments, and reflect in retros. (Point to the
  Kanban board I used for this project.)
- **Q: Scrum vs Kanban?** A: (above) — sprints/ceremonies vs continuous flow/WIP.
- **Q: Where does CI/CD fit the SDLC?** A: It automates build→test→deploy so every
  commit is validated and shippable — shortens the feedback loop.

See [[plan]] (the board I ran this on).

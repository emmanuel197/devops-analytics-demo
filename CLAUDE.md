# DevOps Analytics Bootcamp — Wiki Schema

This repo is a weekend crash-course to prepare Emmanuel for a **Full-Stack DevOps
Analytics Engineer** interview (Monday 2026-06-01). It uses Andrej Karpathy's
**LLM Wiki** pattern: Claude maintains a compounding, interlinked markdown
knowledge base so nothing is lost to chat history.

## Roles
- **Emmanuel (human):** does the hands-on practice, curates sources, asks questions,
  decides what matters.
- **Claude (maintainer):** gives step-by-step instructions, then keeps the wiki
  consistent — writes/updates concept pages, the index, the log, and the cheat
  sheet. Claude owns all bookkeeping and cross-referencing.

## Layout
```
wiki/
  index.md          # catalog of every page, one line each (UPDATE on every change)
  log.md            # append-only chronological progress (newest at top)
  plan.md           # the master roadmap + live status per phase
  concepts/         # one page per skill, grows as Emmanuel practices
  interview/        # cheatsheet.md — compounds into the Monday crib sheet
  sources/          # raw inputs (job desc, articles) — read-only, never edited
```

## Conventions
- Every page starts with YAML frontmatter:
  ```yaml
  ---
  tags: [tool, category]
  status: not-started | in-progress | done
  phase: <number>
  updated: 2026-05-30
  ---
  ```
- Cross-link pages with `[[wikilink]]` style using the page's filename (no ext).
- Concept pages follow this section order: **What it is · How it maps to what I
  already know · Hands-on (what I built) · Key commands/snippets · Likely
  interview Q&A · Gotchas**.
- `status` values drive the Kanban view in `plan.md`.

## Workflows (Claude runs these)
- **Ingest:** new source dropped in `sources/` → read it, write/refresh the
  relevant concept page, update `index.md`, append a `log.md` entry.
- **After each practice phase:** update that concept page's Hands-on + Q&A
  sections, flip its `status`, bump `updated`, append to `log.md`, refresh
  `interview/cheatsheet.md`.
- **Lint (Sun night):** check for contradictions, stale TODOs, orphan pages,
  missing cross-links, and gaps before the interview.

## Log entry format
`## [YYYY-MM-DD HH:MM] <verb> | <short title>` followed by 1–3 bullet lines.

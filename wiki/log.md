# Log

Append-only, newest at top. Format: `## [YYYY-MM-DD HH:MM] verb | title`.

## [2026-05-31] phase-5 | Power BI dashboard built (done out of order)
- Installed Power BI Desktop (winget). Connected LIVE to Postgres taskboard DB.
- Wrote 4 DAX measures (Total/Completed/Completion Rate/Avg Days to Complete).
- Dashboard: 4 KPI cards + donut (status) + stacked column (priority×status) +
  line (created_at). Saved powerbi/taskboard-analytics.pbix.
- 250 tasks, 120 done, 48% completion, 5.33 avg days. Phase 5 DONE.
- Next recommended: Phase 2 (Prometheus+Grafana) or cheat sheet finalize.

## [2026-05-31] phase-1 | Jenkins CI pipeline green
- Ran Jenkins LTS in Docker (custom image: + Docker CLI + plugins; socket mounted).
- Pipeline job from SCM (GitHub repo) runs Jenkinsfile: Checkout → Build image → Test.
- Build #1 SUCCESS: built/tagged taskboard:1 + :latest, `Ran 4 tests ... OK`.
- Added DJANGO_TEST_SQLITE branch so CI tests run on in-memory SQLite (no Postgres).
- Phase 1 DONE. Next: Phase 2 — Prometheus + Grafana.

## [2026-05-30] phase-0 | App verified + diagrams rendered
- `docker compose up` succeeds: web + db (healthy) containers running.
- Verified endpoints: /api/tasks/ (JSON), /metrics (Prometheus), 250 tasks seeded.
- Installed mermaid-cli globally (`mmdc` on PATH) after the Docker mermaid images
  hit puppeteer/Chrome launch bugs. Regenerate visuals via `wiki/diagrams/README.md`.
- Rendered 3 diagrams: current-state, target-architecture, roadmap (in wiki/diagrams/).
- Phase 0 backbone DONE. Next: Phase 1 — Jenkins.

## [2026-05-30] phase-0 | TaskBoard app scaffolded
- Created full Django+Postgres app under `app/` (model, DRF API, admin, /metrics,
  seed command for ~250 tasks, tests, Dockerfile, docker-compose, entrypoint).
- Verified env: Docker 28.5.1 + Compose v2.40 installed (daemon not yet started),
  git 2.51, gh 2.87 logged in as emmanuel197 (scopes: repo, workflow — need
  `project` scope later for Kanban).
- Next: start Docker Desktop, `docker compose up --build`, verify endpoints,
  create GitHub repo + Kanban board.

## [2026-05-30] setup | Wiki scaffold created
- Adopted Karpathy LLM Wiki pattern for tracking the weekend.
- Created schema (CLAUDE.md), index, plan, 7 concept stubs, cheat sheet stub.
- Plan = Approach A: one end-to-end pipeline (TaskBoard app) + Analytics, run as
  Agile sprints. Local-first, Docker, AWS vocabulary.
- Next: Phase 0 — GitHub repo + Kanban board + scaffold the TaskBoard app.

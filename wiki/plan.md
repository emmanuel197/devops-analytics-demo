---
tags: [plan, roadmap]
status: in-progress
phase: 0
updated: 2026-05-30
---

# Master Plan

**Goal:** prepare for a Full-Stack DevOps Analytics Engineer interview on
**Monday 2026-06-01** by getting real hands-on experience with the gap skills.

**Approach (A):** one end-to-end pipeline as the spine + Analytics as act two,
run as Agile sprints. Reuse a fresh minimal **TaskBoard** (Django + Postgres)
app as the "product"; every tool acts on that one app. Local-first via Docker,
using AWS vocabulary. Built-in fallback: if time runs short Sunday night, stop
building and convert remaining phases to talking points.

## The backbone app: TaskBoard
Tiny Django + Postgres REST app: `Task(title, status, priority, created_at)` +
admin + one API endpoint + `/metrics`. Dockerized (web + db). Its DB is also the
dataset for Power BI.

## Phases (Kanban)
| # | Phase | Est | Status | Page |
|---|-------|-----|--------|------|
| 0 | Setup + Agile board + scaffold app | 45m | done | this page |
| 1 | Jenkins CI pipeline | 2.5h | not-started | [[concepts/jenkins]] |
| 2 | Prometheus + Grafana | 2.5h | not-started | [[concepts/prometheus-grafana]] |
| 3 | Terraform (IaC) | 2.5h | not-started | [[concepts/terraform]] |
| 4 | Ansible (config mgmt) | 2h | not-started | [[concepts/ansible]] |
| 5 | Power BI dashboard | 3.5h | not-started | [[concepts/power-bi]] |
| 6 | ELK logging (stretch) | 2h | not-started | [[concepts/elk]] |
| 7 | Agile/SDLC study + cheat sheet | 1h | not-started | [[concepts/agile-sdlc]] |

## Schedule
- **Sat:** phases 0–2 (~6h)
- **Sun:** phases 3–5 (~8h)
- **Sun night:** phase 7 + cheat sheet lint; ELK only if ahead

## Skill → existing-experience map (the interview narrative)
- Jenkins ≈ your GitHub Actions `deploy.yml`, stage for stage
- Terraform/Ansible = infra & config as code (new tools, familiar "as code" idea)
- Prometheus/Grafana = monitoring (golden signals)
- Power BI/Tableau = the "Analytics" half (you already model SQL/Mongo data)
- Scrum/Kanban/SDLC = vocabulary for how you already ship software

# DevOps Analytics Bootcamp

A weekend, end-to-end DevOps + Analytics project built to demonstrate the full
software delivery lifecycle on a single app.

**TaskBoard** (Django + Postgres) is taken from commit → CI → provisioned infra →
configured → monitored → analyzed, all run as Agile sprints:

| Stage | Tool |
|-------|------|
| App | Django REST + Postgres (Dockerized) |
| CI/CD | Jenkins (`Jenkinsfile`) |
| Infrastructure as Code | Terraform |
| Configuration management | Ansible |
| Monitoring | Prometheus + Grafana |
| Logging | ELK (Elasticsearch + Kibana) |
| Analytics / BI | Power BI |
| Process | Scrum / Kanban / SDLC |

## Quick start (the app)

```bash
cd app
docker compose up --build
```

Then visit:
- App API: http://localhost:8000/api/tasks/
- Admin: http://localhost:8000/admin/  (admin / admin)
- Metrics: http://localhost:8000/metrics
- Postgres (for Power BI): localhost:5432 (taskboard / taskboard)

## Knowledge base

Progress and learning notes are maintained as a Karpathy-style **LLM Wiki** in
[`wiki/`](wiki/) — see [`wiki/plan.md`](wiki/plan.md) for the roadmap.

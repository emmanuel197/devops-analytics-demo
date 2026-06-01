---
tags: [interview, cheatsheet]
status: done
phase: 0
updated: 2026-06-01
---

# Monday Interview Cheat Sheet

## The 30-second pitch
> I'm a full-stack engineer — React, Django, SQL & MongoDB — who already ships
> with CI/CD via GitHub Actions. To round out the DevOps + Analytics side I built
> an end-to-end project: a Dockerized Django app taken from commit → **Jenkins**
> CI → **Prometheus/Grafana** monitoring → a live **Power BI** analytics
> dashboard, all tracked on a **Kanban** board. So I can speak to the full
> delivery lifecycle, not just writing the app.

## The architecture story (walk this)
TaskBoard (Django + Postgres, in Docker) is the product. Around it:
- **git push → GitHub →** picked up by **Jenkins**, which runs a pipeline:
  checkout → build the Docker image → run the tests. Green build = shippable.
- The app exposes **`/metrics`**; **Prometheus** scrapes it every 5s; **Grafana**
  graphs it live (request rate, etc.).
- The same Postgres DB feeds a **Power BI** dashboard — KPIs + charts with DAX.
- The whole thing was planned and tracked as **Agile** work on a Kanban board.

## What I actually built (proof points)
- **App:** Django REST API + admin + `/metrics`, Postgres, `docker compose up`.
- **Jenkins:** Dockerized, pipeline-from-SCM, green build, 4 tests pass.
- **Prometheus + Grafana:** scraping target UP, live PromQL graph.
- **Power BI:** live Postgres connection, 4 DAX measures, cards+donut+bar+line.
- **Process:** GitHub repo + Kanban board + this compounding wiki & diagrams.

## Per-tool one-liners
| Tool | What it is | What I built | Maps to |
|------|-----------|--------------|---------|
| Jenkins | Self-hosted CI/CD; pipeline-as-code (Jenkinsfile) | Dockerized Jenkins, SCM pipeline checkout→build→test, green | GitHub Actions |
| Prometheus+Grafana | Pull-based metrics DB + dashboards | Scrape app /metrics, live request-rate graph | monitoring/observability |
| Power BI | Connect→model→DAX→visuals | Live Postgres, 4 DAX measures, dashboard, .pbix | SQL modeling; DAX≈SQL aggregates |
| Docker | Containerized app + all tooling | compose for app, Jenkins, monitoring | (already used in CI) |
| Agile/Kanban | Iterative delivery, visualized flow | Ran this project as phases on a board | how I ship |

## Key Q&A (see each concept page for more)
- **Jenkins vs GitHub Actions:** same CI/CD; Jenkins self-hosted/plugins, Actions
  managed. Jenkinsfile ≈ workflow yaml. [[concepts/jenkins]]
- **Containerized Jenkins builds images how?** mount the host Docker socket.
- **Prometheus push or pull?** pull/scrape `/metrics`. `rate(counter[1m])` for
  per-sec. [[concepts/prometheus-grafana]]
- **Measure vs column (Power BI)?** measure = filter-aware, computed at query
  time; column = per-row, stored. [[concepts/power-bi]]
- **Scrum vs Kanban?** sprints+ceremonies vs continuous flow+WIP limits.
  [[concepts/agile-sdlc]]

## The gaps — how to speak to them honestly
I didn't hands-on these in the window, but I understand them and the "as-code"
principle behind them is the same one I used everywhere:
- **Terraform** = infrastructure as code; declarative, idempotent, has state.
  "I'd declare the same containers/cloud resources I built by hand in compose."
- **Ansible** = configuration management; idempotent playbooks. Terraform
  *provisions* infra, Ansible *configures* it.
- **ELK** = centralized logging (Elasticsearch store + Kibana view); the "logs"
  pillar that complements my Prometheus "metrics" pillar.
- **Tableau** = same space as Power BI; concepts (data model, measures, viz)
  transfer.
Framing: "I learn tools fast by building — here's a weekend where I stood up
Jenkins, Prometheus/Grafana, and Power BI from scratch. Terraform/Ansible are the
next ones and I already use the same IaC mindset."

## Questions to ask them
- What does your CI/CD pipeline look like today — Jenkins, Actions, GitLab?
- Cloud + IaC: AWS/Azure/GCP, Terraform or something else?
- What does "Analytics" mean in this role day-to-day — Power BI reports, data
  pipelines, both?
- How do the DevOps and Analytics halves of the role split?

---
tags: [prometheus, grafana, monitoring, observability]
status: done
phase: 2
updated: 2026-06-01
---

# Prometheus + Grafana

## What it is
- **Prometheus**: a time-series database that **pulls** ("scrapes") metrics from
  targets' `/metrics` endpoints on an interval, and stores them.
- **Grafana**: a dashboarding tool that queries Prometheus (via PromQL) and draws
  live graphs.

## How it maps to what I already know
New tooling, but the model is simple: app exposes numbers → Prometheus collects
them → Grafana visualizes. It's the "metrics" pillar of observability (the others
being logs — [[concepts/elk]] — and traces).

## Hands-on (what I built)
- Added `django-prometheus` to the app → it exposes `/metrics`.
- Ran Prometheus + Grafana via `monitoring/docker-compose.yml`.
- Configured Prometheus to scrape the app at `host.docker.internal:8000` every 5s
  — confirmed the `taskboard` target is **UP** at `localhost:9090/targets`.
- Connected Grafana to Prometheus (`http://prometheus:9090`) and graphed request
  rate with PromQL.

## Key commands / snippets
```yaml
# prometheus.yml
scrape_configs:
  - job_name: 'taskboard'
    metrics_path: /metrics
    static_configs:
      - targets: ['host.docker.internal:8000']
```
```promql
rate(django_http_requests_total_by_method_total[1m])   # requests/sec
```

## Likely interview Q&A
- **Q: Push or pull?** A: Prometheus **pulls** (scrapes) targets — unlike, say,
  StatsD which is push. Targets just expose `/metrics`.
- **Q: What's `rate()` for?** A: Metrics like request counts are monotonic
  counters; `rate(counter[1m])` gives the per-second increase over a window —
  that's what you actually graph.
- **Q: Prometheus vs Grafana — what does each do?** A: Prometheus = collect +
  store + alert; Grafana = visualize (it's not a datastore).
- **Q: Golden signals?** A: latency, traffic, errors, saturation — what you'd
  build dashboards/alerts around.

## Gotchas
- A container scraping the host app uses `host.docker.internal` (Docker Desktop),
  not `localhost` (which would mean the Prometheus container itself).
- Grafana reaches Prometheus by service name on the shared compose network.

See [[plan]] · pairs with [[concepts/elk]] as observability.

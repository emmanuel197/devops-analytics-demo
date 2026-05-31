---
tags: [power-bi, bi, analytics, tableau, dax]
status: done
phase: 5
updated: 2026-05-31
---

# Power BI (+ Tableau)

## What it is
Microsoft's BI tool: connect to data → model it → write metrics in **DAX** →
build interactive visuals. The "Analytics" half of the job title.

## How it maps to what I already know
I already model relational data (SQL/Django). Power BI adds the metrics +
visualization layer:

| Power BI | My existing analog |
|---|---|
| Data source / connector | the Django DB |
| Power Query (M) | SQL `SELECT` / querysets (shape on load) |
| Data model (tables + relationships) | Django models / FKs |
| **DAX measures** | SQL aggregates, but reusable & filter-aware |
| Import vs DirectQuery | snapshot vs live query |

## Hands-on (what I built)
- Connected Power BI **live to the Postgres `taskboard` DB** (`localhost:5432`,
  Import mode) — the same DB the app + Jenkins use.
- Renamed the table to `tasks` in Power Query.
- Wrote **4 DAX measures** (below).
- Built a dashboard: 4 KPI cards, a donut (status), a stacked column
  (priority × status), a line (tasks over time).
- Saved as `powerbi/taskboard-analytics.pbix`.
- Result: 250 tasks, 120 done, **48% completion**, **5.33 avg days to complete**.

## DAX measures (and what each function does)
```DAX
Total Tasks     = COUNTROWS('tasks')
Completed Tasks = CALCULATE(COUNTROWS('tasks'), 'tasks'[status] = "done")
Completion Rate = DIVIDE([Completed Tasks], [Total Tasks])
Avg Days to Complete =
    AVERAGEX(FILTER('tasks', 'tasks'[status] = "done"),
             DATEDIFF('tasks'[created_at], 'tasks'[completed_at], DAY))
```
- **COUNTROWS** — count rows in a table.
- **CALCULATE** — evaluate an expression under a modified filter (the workhorse of DAX).
- **DIVIDE** — safe division (handles divide-by-zero → blank).
- **AVERAGEX** — iterate a table, evaluate an expression per row, average it.
- **FILTER** — return a filtered subset of a table.
- **DATEDIFF** — difference between two dates in a chosen unit.

## Likely interview Q&A
- **Q: Measure vs calculated column?** A: A column is computed per row and
  stored; a measure is computed at query time, respecting the visual's filter
  context. Measures for aggregations/KPIs, columns for row-level attributes.
- **Q: Import vs DirectQuery?** A: Import loads a cached snapshot (fast, needs
  refresh); DirectQuery queries the source live (always current, slower, source
  load). I used Import against Postgres.
- **Q: What's CALCULATE?** A: Changes filter context for an expression — e.g.
  count only "done" tasks regardless of the visual.
- **Q: Power BI vs Tableau?** A: Same space; Power BI is Microsoft-stack /
  cheaper / DAX, Tableau is strong on visual exploration / VizQL. Concepts transfer.

## Gotchas
- PostgreSQL connector needs Npgsql — bundled in modern Power BI Desktop, worked
  out of the box.
- Measures need explicit number formatting (e.g. Completion Rate → Percentage via
  the "Measure tools" tab, which only shows when a measure is selected).
- Date fields on a line axis default to a Year/Quarter/Month/Day hierarchy.

See [[plan]] · models the same DB as [[concepts/jenkins]]'s app.

# TaskBoard app

Minimal Django + Postgres REST app. Exists to be built, deployed, monitored, and
analyzed by the surrounding DevOps tooling.

## Run

```bash
docker compose up --build
```

The `web` container auto-runs migrations, creates an `admin/admin` superuser,
and seeds ~250 sample tasks on first start.

## Endpoints
- `GET/POST /api/tasks/` — task CRUD (Django REST Framework)
- `/admin/` — Django admin (admin / admin)
- `/metrics` — Prometheus metrics (django-prometheus)

## Run tests
```bash
docker compose run --rm web python manage.py test
```

## Data model
`Task(title, status[todo|in_progress|done], priority[low|medium|high], created_at, completed_at)`

#!/bin/sh
set -e

echo "Running migrations..."
python manage.py migrate --noinput

echo "Collecting static files..."
python manage.py collectstatic --noinput

echo "Creating superuser (if missing)..."
python manage.py createsuperuser --noinput 2>/dev/null || true

echo "Seeding sample tasks (if empty)..."
python manage.py seed_tasks

echo "Starting server..."
exec "$@"

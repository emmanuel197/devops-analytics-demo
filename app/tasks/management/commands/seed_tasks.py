import random
from datetime import timedelta

from django.core.management.base import BaseCommand
from django.utils import timezone

from tasks.models import Task

ADJECTIVES = [
    "Refactor", "Investigate", "Deploy", "Document", "Optimize", "Migrate",
    "Configure", "Monitor", "Automate", "Review", "Patch", "Provision",
]
NOUNS = [
    "auth service", "billing module", "CI pipeline", "dashboard", "database",
    "cache layer", "API gateway", "log shipper", "metrics exporter",
    "Terraform module", "Ansible playbook", "Grafana panel",
]


class Command(BaseCommand):
    help = "Seed ~250 sample tasks for analytics demos (no-op if data exists)."

    def add_arguments(self, parser):
        parser.add_argument("--count", type=int, default=250)

    def handle(self, *args, **options):
        if Task.objects.exists():
            self.stdout.write("Tasks already exist; skipping seed.")
            return

        now = timezone.now()
        statuses = ["todo", "in_progress", "done"]
        priorities = ["low", "medium", "high"]
        count = options["count"]

        tasks = []
        for i in range(count):
            created = now - timedelta(
                days=random.randint(0, 90), hours=random.randint(0, 23)
            )
            status = random.choices(statuses, weights=[3, 2, 5])[0]
            completed = None
            if status == "done":
                completed = created + timedelta(days=random.randint(1, 10))
                if completed > now:
                    completed = now
            tasks.append(
                Task(
                    title=f"{random.choice(ADJECTIVES)} {random.choice(NOUNS)} #{i + 1}",
                    status=status,
                    priority=random.choices(priorities, weights=[3, 4, 2])[0],
                    created_at=created,
                    completed_at=completed,
                )
            )

        Task.objects.bulk_create(tasks)
        self.stdout.write(self.style.SUCCESS(f"Seeded {count} tasks."))

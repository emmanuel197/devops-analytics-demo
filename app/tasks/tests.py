from django.test import TestCase
from django.utils import timezone

from .models import Task


class TaskModelTests(TestCase):
    def test_str_returns_title(self):
        task = Task.objects.create(title="Write Jenkinsfile", created_at=timezone.now())
        self.assertEqual(str(task), "Write Jenkinsfile")

    def test_defaults(self):
        task = Task.objects.create(title="Default task", created_at=timezone.now())
        self.assertEqual(task.status, Task.Status.TODO)
        self.assertEqual(task.priority, Task.Priority.MEDIUM)


class TaskApiTests(TestCase):
    def test_list_endpoint_returns_200(self):
        Task.objects.create(title="Seeded", created_at=timezone.now())
        response = self.client.get("/api/tasks/")
        self.assertEqual(response.status_code, 200)

    def test_create_via_api(self):
        response = self.client.post(
            "/api/tasks/",
            {"title": "Via API", "status": "todo", "priority": "high"},
            content_type="application/json",
        )
        self.assertEqual(response.status_code, 201)
        self.assertTrue(Task.objects.filter(title="Via API").exists())

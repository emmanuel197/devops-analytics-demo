from django.contrib import admin
from django.http import HttpResponse
from django.urls import include, path


def home(request):
    """Simple landing page so the root URL isn't a 404."""
    return HttpResponse(
        """
        <html>
        <head><title>TaskBoard</title>
        <style>
          body { font-family: system-ui, sans-serif; max-width: 640px;
                 margin: 60px auto; line-height: 1.7; color: #222; }
          h1 { margin-bottom: 4px; }
          .muted { color: #666; }
          a { display: block; margin: 10px 0; font-size: 1.05rem; }
        </style>
        </head>
        <body>
          <h1>TaskBoard</h1>
          <p class="muted">Django + Postgres demo app — DevOps Analytics Bootcamp.</p>
          <a href="/admin/">/admin/ &mdash; Django admin (admin / admin)</a>
          <a href="/api/tasks/">/api/tasks/ &mdash; REST API</a>
          <a href="/metrics">/metrics &mdash; Prometheus metrics</a>
        </body>
        </html>
        """
    )


urlpatterns = [
    path("", home, name="home"),
    path("admin/", admin.site.urls),
    path("api/", include("tasks.urls")),
    path("", include("django_prometheus.urls")),  # exposes /metrics
]

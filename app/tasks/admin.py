from django.contrib import admin

from .models import Task


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ("title", "status", "priority", "created_at", "completed_at")
    list_filter = ("status", "priority")
    search_fields = ("title",)
    date_hierarchy = "created_at"

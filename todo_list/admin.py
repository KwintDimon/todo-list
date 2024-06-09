from django.contrib import admin

from todo_list.models import Task, Tag


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_filter = ("tags", "done")
    list_display = ("content", "created_at", "done",)


admin.site.register(Tag)

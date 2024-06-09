from django.shortcuts import render
from django.views.generic import ListView

from .models import Task, Tag


class TaskListView(ListView):
    queryset = Task.objects.all().prefetch_related("tags")
    paginate_by = 10


class TagListView(ListView):
    queryset = Tag.objects.all()
    paginate_by = 10

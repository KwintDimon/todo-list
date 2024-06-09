from django.shortcuts import render
from django.views.generic import ListView

from todo_list.models import Task


class TaskListView(ListView):
    queryset = Task.objects.all().prefetch_related("tags")

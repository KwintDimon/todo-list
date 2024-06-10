from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DeleteView,
)

from .models import Task, Tag


class TaskListView(ListView):
    queryset = Task.objects.all().prefetch_related("tags")
    paginate_by = 10


class TaskCreateView(CreateView):
    model = Task
    fields = "__all__"
    success_url = reverse_lazy("todo_list:task-list")


class TaskUpdateView(UpdateView):
    model = Task
    fields = "__all__"
    success_url = reverse_lazy("todo_list:task-list")


class TaskDeleteView(DeleteView):
    model = Task
    success_url = reverse_lazy("todo_list:task-list")


class DoUndoTaskView(View):
    @staticmethod
    def get(request, *args, **kwargs):
        task = get_object_or_404(Task, id=kwargs['pk'])

        if task.done:
            task.done = False

        else:
            task.done = True
        task.save()
        return HttpResponseRedirect(reverse_lazy("todo_list:task-list"))


class TagListView(ListView):
    queryset = Tag.objects.all()
    paginate_by = 10


class TagCreateView(CreateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("todo_list:tag-list")


class TagUpdateView(UpdateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("todo_list:tag-list")


class TagDeleteView(DeleteView):
    model = Tag
    success_url = reverse_lazy("todo_list:tag-list")

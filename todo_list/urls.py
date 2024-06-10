from django.urls import path

from .views import (
    TaskListView,
    TagListView,
    TaskCreateView,
    TaskUpdateView,
    TaskDeleteView,
    DoUndoTaskView
)

urlpatterns = [
    path('', TaskListView.as_view(), name='task-list'),
    path('tasks/create', TaskCreateView.as_view(), name='task-create'),
    path('tasks/<int:pk>/update', TaskUpdateView.as_view(), name='task-update'),
    path('tasks/<int:pk>/delete', TaskDeleteView.as_view(), name='task-delete'),
    path('tasks/<int:pk>/do-undo', DoUndoTaskView.as_view(), name='task-do-undo'),
    path('tags/', TagListView.as_view(), name='tag-list'),
]

app_name = 'todo_list'

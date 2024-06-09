from django.urls import path

from todo_list.views import TaskListView

urlpatterns = [
    path('', TaskListView.as_view(), name='task-list')
]

app_name = 'todo_list'

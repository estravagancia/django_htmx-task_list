from django.urls import path
from .views import delete_task, display_tasks, add_task

urlpatterns = [
    path('', display_tasks, name='display_tasks'),
    path('<int:id>/delete/', delete_task, name='delete_task'),
    path('add_task/', add_task, name='add_task'),
]
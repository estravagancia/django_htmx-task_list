from django.shortcuts import render
from .models import Task
from django.views.decorators.http import require_http_methods
# Create your views here.

def display_tasks(request):
    tasks = Task.objects.all()
    return render(request, 'tasks/display_tasks.html', {'tasks': tasks})
    
@require_http_methods(['DELETE'])
def delete_task(request, id):
    Task.objects.all().filter(id=id).delete()
    tasks = Task.objects.all()
    return render(request, 'tasks/tasks_lists.html', {'tasks': tasks})

@require_http_methods(['POST'])
def add_task(request):
    texto=request.POST.get("tarea")
    Task.objects.create(description=texto)
    tasks = Task.objects.all()
    return render(request, 'tasks/tasks_lists.html', {'tasks': tasks})
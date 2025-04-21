from django.shortcuts import render, redirect, get_object_or_404
from .models import Task

def index(request):
    # Fetch all tasks from the database
    tasks = Task.objects.all().order_by('-id')

    # Handle form submission to add a new task
    if request.method == 'POST':
        title = request.POST.get('title')
        if title:
            Task.objects.create(title=title)
            return redirect('index')

    return render(request, 'tracker/index.html', {'tasks': tasks})


def complete_task(request, task_id):
    # Mark a specific task as completed
    task = get_object_or_404(Task, id=task_id)
    task.completed = True
    task.save()
    return redirect('index')


def delete_task(request, task_id):
    # Delete a specific task
    task = get_object_or_404(Task, id=task_id)
    task.delete()
    return redirect('index')


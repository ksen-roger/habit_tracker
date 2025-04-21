from django.shortcuts import render, redirect, get_object_or_404
from .models import Task

def index(request):
    """Display all tasks and handle task creation"""
    tasks = Task.objects.all()
    
    if request.method == 'POST':
        title = request.POST.get('title')
        if title:
            Task.objects.create(title=title)
            return redirect('index')
    
    return render(request, 'tracker/index.html', {'tasks': tasks})

def complete_task(request, task_id):
    """Mark the specified task as complete"""
    task = get_object_or_404(Task, id=task_id)
    task.completed = True
    task.save()
    
    return redirect('index')

def delete_task(request, task_id):
    """Delete the specified task"""
    task = get_object_or_404(Task, id=task_id)
    task.delete()
    
    return redirect('index')

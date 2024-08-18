from django.shortcuts import render, redirect, get_object_or_404
from .models import Task
from django.contrib import messages
from .forms import TaskForm

# Create your views here.

def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'task_list.html', {'tasks': tasks})


def task_create(request):
    if request.method == "POST":
        title = request.POST.get('title')
        description = request.POST.get('description')
        due_date = request.POST.get('due_date')
        is_complete = request.POST.get('is_complete') == 'on'

        task = Task(title = title, description = description, due_date = due_date, is_complete = is_complete)
        task.save()
        messages.success(request, "Task created successfully!")
        return redirect('task_list')
    return render(request, 'task_form.html')


def task_detail(request, id):
    task = get_object_or_404(Task, id=id)
    return render(request, 'task_detail.html', {'task': task})

def task_delete(request, id):
    task = get_object_or_404(Task, id=id)
    task.delete()
    messages.success(request, "Task deleted successfully!")
    return redirect('task_list')

# def delete_task(request, task_id):
#     task = Task.objects.filter(id=task_id)
#     task.delete()
#     return redirect('/myapp/task_llist/')

def task_edit(request, id):
    task = get_object_or_404(Task, id=id)
    
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task_list')  # Redirect to the task list after saving
    else:
        form = TaskForm(instance=task)
    
    return render(request, 'task_edit.html', {'form': form, 'task': task})
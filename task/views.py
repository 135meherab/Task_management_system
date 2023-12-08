from django.shortcuts import render, redirect
from . form import TaskForm
from . models import Task
# Create your views here.
def add_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show_task')
    else:
        form = TaskForm()
    return render (request, 'task.html', {'form': form})

def edit_task(request, id):
    task = Task.objects.get(pk = id)
    form = TaskForm(instance=task)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('show_task')
    return render (request, 'task.html', {'form': form})

def delete_task(request, id):
    Task.objects.get(pk = id).delete()
    return redirect('show_task')
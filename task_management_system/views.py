from django.shortcuts import render
from task.models import Task
def show(request):
    data = Task.objects.all()
    return render (request, 'show_task.html',{'data': data})
from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from .models import Project,Task
from django.shortcuts import get_object_or_404,render
from django.core import serializers
# Create your views here.


def hello(request):
    return render(request, 'index.html')

def about(request):
    return HttpResponse("<h1>about</h1>")


def hello_with_params(_, name):
    
    
    return HttpResponse(f"<h1>Hello {name}</h1>")

def get_all_projects(_):
    projects_db = list(Project.objects.values())
    return JsonResponse(projects_db, safe=False)

def get_all_tasks(_):
    
    return JsonResponse(list(Task.objects.values()), safe=False)

def get_tasks_id(_,id):
    
    task =  Task.objects.get(id = id)
   
    return JsonResponse({"id" : task.id, "title" : task.title, "description" : task.description},safe=False)

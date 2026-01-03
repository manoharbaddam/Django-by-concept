from django.shortcuts import render,redirect
from .forms import ProjectCreationForm,TaskCreationForm

# Create your views here.

def index(request):
    return render(request,'layout.html')

def create_project(request):
    form = ProjectCreationForm()
    if request.method == "POST":
        form = ProjectCreationForm(request.POST)
        if form.is_valid():
            project = form.save(commit=False)
            project.owner = request.user
            project.save()
            return redirect('index')
    return render(request,'create_project.html',{'form':form})

def create_task(request):
    form = TaskCreationForm()
    if request.method == "POST":
        form = TaskCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    return render(request,'create_task.html',{'form':form})
        
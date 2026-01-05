from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .forms import ProjectCreationForm,TaskCreationForm
from customUser.models import CustomUserModel
from .models import Project,Task

# Create your views here.

def index(request):
    return render(request,'index.html')

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
    form = TaskCreationForm(user=request.user)
    if request.method == "POST":
        form = TaskCreationForm(request.POST,user= request.user)
        if form.is_valid():
            form.save()
            return redirect('index')
    return render(request,'create_task.html',{'form':form})

#allows to view all projects created by a user
@login_required()
def view_projects(request):
    user_id = request.user.id
    user = CustomUserModel.objects.get(id=user_id)
    projects = user.owned_projects.all()
    return render(request,'view_projects.html',{'projects':projects})

@login_required()
def view_tasks(request,project_id):
    tasks = Task.objects.filter(project_id=project_id)
    return render(request,'view_tasks.html',{'tasks':tasks})

from django.shortcuts import render,redirect,get_object_or_404
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

@login_required
def edit_tasks(request,task_id):
    print(task_id)
    task= get_object_or_404(Task,id=task_id)
    if request.method=="POST":
        form = TaskCreationForm(request.POST,instance=task,user=request.user)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = TaskCreationForm(instance=task,user=request.user)
    return render(request,'edit_tasks.html',{'form':form})



@login_required()
def filter_tasks(request,project_id):
    tasks = Task.objects.filter(project_id=project_id)
    filtered_tasks = {
        'completed' : [],
        'pending':[],
    }

    filtered_tasks['completed'] = tasks.filter(completed = True)
    filtered_tasks['pending'] = tasks.filter(completed =False)

    return render(request,'view_tasks.html',{'filtered_tasks':filtered_tasks})
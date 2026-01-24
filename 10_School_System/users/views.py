from django.shortcuts import render,redirect
from django.contrib.auth import login,authenticate
from django.http import HttpResponseForbidden
from django.contrib.auth.decorators import login_required
from .forms import RegistrationForm,LoginForm,StudentCreationForm,TeacherCreationForm

# Create your views here.
def index(request):
    return render(request,'layout.html')

def register_user(request):
    form = RegistrationForm()
    if request.method=="POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login_user")
    return render(request,'register.html',{'form':form})

@login_required()
def create_student(request):
    if request.user.role != "ADMIN":
        return HttpResponseForbidden()
    
    form = StudentCreationForm()
    if request.method=="POST":
        form = StudentCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    return render(request,'register.html',{'form':form})

@login_required()
def create_teacher(request):
    if request.user.role!="ADMIN":
        return HttpResponseForbidden()
    
    form = TeacherCreationForm()
    if request.method=="POST":
        form = TeacherCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    return render(request,'register.html',{'form':form})

def login_user(request):
    form = LoginForm()
    if request.method=="POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            role = form.cleaned_data['role']
            user = authenticate(request,email=email,password=password)
            if user is not None:
                login(request,user)
                if role=="ADMIN":
                    return redirect("admin_dashboard.html")
                elif role=="TEACHER":
                    return redirect("teacher_dashboard.html")
                else:
                    return redirect("student_dashboard.html")

    return render(request,"login.html",{'form':form})
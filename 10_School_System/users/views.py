from django.shortcuts import render,redirect
from django.contrib.auth import login,authenticate,logout
from django.http import HttpResponseForbidden
from django.contrib.auth.decorators import login_required
from .forms import RegistrationForm,LoginForm,StudentCreationForm,TeacherCreationForm

# Create your views here.
def index(request):
    return render(request,'layout.html')


def registration(request):
    return render(request,'registration.html',)

@login_required
def add_user(request):
    if request.user.role != "ADMIN":
        return HttpResponseForbidden()

    role = request.POST.get("role") or request.GET.get("role")

    student_form = StudentCreationForm(prefix="student")
    teacher_form = TeacherCreationForm(prefix="teacher")

    if request.method == "POST":
        if role == "STUDENT":
            student_form = StudentCreationForm(request.POST, prefix="student")
            if student_form.is_valid():
                student_form.save()
                return redirect("users:dashboard_view")

        elif role == "TEACHER":
            teacher_form = TeacherCreationForm(request.POST, prefix="teacher")
            if teacher_form.is_valid():
                teacher_form.save()
                return redirect("users:admin_dashboard")

    return render(
        request,
        "add_user.html",
        {
            "student_form": student_form,
            "teacher_form": teacher_form,
        },
    )


def login_user(request):
    form = LoginForm()
    if request.method=="POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request,email=email,password=password)
            login(request,user)
            return redirect("users:dashboard_view")
    return render(request,"login.html",{'form':form})

def logout_user(request):
    logout(request)
    return redirect("users:login_user")

def dashboard_view(request):
    role = request.user.role
    if role=="ADMIN":
        return render(request,"dashboards/admin_dashboard.html")
    elif role=="TEACHER":
        return render(request,"dashboards/teacher_dashboard.html")
    else:
        return render(request,"dashboards/student_dashboard.html")
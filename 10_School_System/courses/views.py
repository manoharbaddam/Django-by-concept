from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from .forms import ClassCreateForm
from .models import Class,Enrollment
from users.models import CustomUser

@login_required
def create_class(request):
    if request.user.role != "ADMIN":
        return HttpResponseForbidden("Access denied")

    if request.method == "POST":
        form = ClassCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("courses:class_list")
    else:
        form = ClassCreateForm()

    return render(request, "create_class.html", {"form": form})

@login_required
def class_list(request):
    classes = Class.objects.select_related("teacher")

    return render(request,"class_list.html",{"classes": classes})

@login_required()
def student_enrollments(request,username=None):
    if request.user.role == "TEACHER":
        return HttpResponseForbidden("Access denied")
    
    classes_enrolled = Enrollment.objects.filter(student=request.user)
    return render(request,'student_enrollments.html',{"classes":classes_enrolled})


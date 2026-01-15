from django.shortcuts import render,redirect
from .forms import CourseCreationForm, CourseEnrollForm
from .models import Course
# Create your views here.

def view_courses(request):
    courses = Course.objects.all()
    return render(request,'view_courses.html',{'courses':courses})

def enroll_course(request):
    if request.method=="POST":
        form = CourseEnrollForm(request.POST)
        form.save()
        return redirect('index')
    else:
        form = CourseEnrollForm()

    return render(request,'enroll_course.html',{'form':form})
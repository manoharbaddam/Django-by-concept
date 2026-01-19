from django.shortcuts import render,get_object_or_404,redirect
from django.contrib.auth.decorators import login_required
from .models import Course,Enrollment

# Create your views here.
def index(request):
    return render(request,'index.html')

@login_required
def list_courses(request):
    all_courses = Course.objects.all()
    return render(request,'list_courses.html',{'courses':all_courses})

@login_required
def enroll_course(request, course_id):
    course = get_object_or_404(Course, id=course_id)

    Enrollment.objects.get_or_create(
        student=request.user,  
        course=course
    )

    return redirect('courses:my_courses',)


def my_courses(request):
    courses = Course.objects.filter(id=request.user.id)
    enrollments= Enrollment.objects.filter(student=request.user)
    return render(request,'my_courses.html',{'courses':courses,'enrollments':enrollments})

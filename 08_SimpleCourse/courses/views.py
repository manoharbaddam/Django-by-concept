from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required,user_passes_test
from userApp.models import Student
from .models import Course
# Create your views here.

@login_required()
def view_courses(request):
    courses = Course.objects.all()
    return render(request,'view_courses.html',{'courses':courses})

@login_required()
def enroll_course(request,course_id):
    course = get_object_or_404(Course,id=course_id)
    if request.method=="POST":
        # id = course_id
        student_id = request.user.id
        student = get_object_or_404(Student,id=student_id)
        student.enrolled_courses.add(course)
        return redirect('view_courses')
        
    return render(request,'enroll_course.html',{'course':course})

def unenroll_course(request,course_id):
    course = get_object_or_404(Course,id=course_id)
    if request.method=="POST":        
        request.user.student.enrolled_courses.remove(course)
        
    return redirect('view_courses')

@user_passes_test(lambda u: u.is_superuser)
def dashboard(request):
    courses = Course.objects.all()
    return render(request,'dashboard.html',{'courses':courses})
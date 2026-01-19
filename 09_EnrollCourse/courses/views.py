from django.shortcuts import render,get_object_or_404,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
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

@login_required
def my_courses(request):
    enrollments = Enrollment.objects.filter(student=request.user)
    return render(request,'my_courses.html',{'enrollments':enrollments})

@login_required
def update_enrollment_status(request, pk):
    enrollment = get_object_or_404(
        Enrollment,
        pk=pk,
        student=request.user  # security check
    )

    if request.method == "POST":
        new_status = request.POST.get("status")
        if new_status in dict(Enrollment.STATUS_CHOICES):
            enrollment.status = new_status
            enrollment.save()

    return redirect("courses:my_courses")

@staff_member_required
def course_enrollment_history(request, course_id):
    course = get_object_or_404(Course, id=course_id)

    enrollments = (
        Enrollment.objects
        .filter(course=course)
        .select_related("student")
        .order_by("-enrolled_date")
    )

    return render(
        request,
        "course_enrollment_history.html",
        {
            "course": course,
            "enrollments": enrollments,
        }
    )
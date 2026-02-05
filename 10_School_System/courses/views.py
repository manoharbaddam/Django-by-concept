from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from .forms import ClassCreateForm
from .models import Class, Enrollment
from users.models import CustomUser


@login_required
def create_class(request):
    if request.user.role != "ADMIN":
        return HttpResponseForbidden("Access denied")

    if request.method == "POST":
        form = ClassCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("courses:create_class")
    else:
        form = ClassCreateForm()

    return render(request, "create_class.html", {"form": form})


@login_required
def all_classes(request):
    classes = Class.objects.select_related("teacher")

    return render(request, "class_list.html", {"classes": classes})


@login_required
def student_classes(request, username=None):
    print(request.user.role)
    if request.user.role != "STUDENT":
        return HttpResponseForbidden("Access denied")

    classes_enrolled = Enrollment.objects.filter(student=request.user)
    return render(request, "student_enrollments.html", {"classes": classes_enrolled})


@login_required
def teacher_classes(request,username=None):
    if request.user.role != "TEACHER":
        print(request.user.role)
        return HttpResponseForbidden("Access Denied")

    classes_assigned = Class.objects.filter(teacher=request.user)
    return render(
        request, "teacher_classes.html", {"classes_assigned": classes_assigned}
    )


def enroll_class(request, class_id):
    if request.method == "POST":
        cls = get_object_or_404(Class, id=class_id)
        Enrollment.objects.create(student=request.user, class_enrolled=cls)
        return redirect("courses:student_classes", username=request.user.username)
    return redirect("courses:all_classes")

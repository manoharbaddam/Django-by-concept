from django.shortcuts import render,redirect
from .forms import CourseCreationForm

# Create your views here.

def create_Course(request):
    if request.method=="POST":
        form = CourseCreationForm(request.POST)
        form.save()
        return redirect('index')
    else:
        form = CourseCreationForm()

    return render(request,'create_course.html',{'form':form})
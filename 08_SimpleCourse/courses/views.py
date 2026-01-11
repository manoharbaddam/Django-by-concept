from django.shortcuts import render


# Create your views here.

def create_Course(request):
    if request.method=="POST":
        form = CourseCreationForm(request.POST)
        form.save()
        return redirect('index')

    return render(request,'index')
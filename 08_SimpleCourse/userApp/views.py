from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth import login,logout,authenticate
from .models import Student
from .forms import StudentCreationForm, StudentLoginForm
from courses.models import Course

# Create your views here.
def index(request):
    return render(request,'index.html')

def register(request):
    if request.method=="POST":
        form = StudentCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            login(request,user)
            return redirect('index')
    else:
        form = StudentCreationForm()
    return render(request,'register.html',{'form':form})

def login_view(request):
    if request.method=="POST":
        form = StudentLoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request,email=email,password=password)
            if user is not None: 
                login(request, user)
                return redirect("index")
            else:
                form.add_error(None, "Invalid email or password")
    else:
        form = StudentLoginForm()
    return render(request,'login.html',{'form':form})

def logout_view(request):
    if request.method=="POST":
        logout(request)
        return redirect('index')
    return render(request,'logout.html')

def profile(request):
    student = get_object_or_404(Student,id=request.user.id)
    courses_enrolled = student.enrolled_courses.all()
    return render(request,'profile.html',{'courses_enrolled':courses_enrolled})


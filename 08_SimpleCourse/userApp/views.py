from django.shortcuts import render,redirect
from django.contrib.auth import login,logout,authenticate
from .models import Student
from .forms import StudentCreationForm, StudentLoginForm

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

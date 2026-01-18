from django.shortcuts import render,redirect
from django.contrib.auth import login as auth_login,authenticate,logout
from django.http import HttpResponse
from .models import Student
from .forms import SignupForm,LoginForm

# Create your views here.
def index(request):
    return HttpResponse("Working")

def signup(request):
    if request.method=="POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request,user)
            user.save()
            return redirect('index')
    else:
        form = SignupForm()
    
    return render(request,'register.html',{'form':form})


def user_login(request):
    form = LoginForm()
    if request.method=="POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password=form.cleaned_data['password']
            user = authenticate(request,email=email,password=password)
            if user is not None:
                auth_login(request,user)
                return redirect('index')
            else:
                form.add_error(None,"Invalid email or Password.")
            
    return render(request,'login.html',{'form':form})

def user_logout(request):
    if request.method=="POST":
        logout(request)
        return redirect('index')
    return render(request,'logout.html')
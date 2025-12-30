from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from .forms import CreateCustomUserForm,UserLoginForm

# Create your views here.
def index(request):
    return render(request,'register.html')


def register_user(request):
    if request.method=='POST':
        form = CreateCustomUserForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Successfully Registered User.")
    else:
        form = CreateCustomUserForm()

    return render(request,'register.html',{'form':form})    


def login_user(request):
    form = UserLoginForm()
    if request.method == "POST":
        form = UserLoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request,email=email,password=password)

            if user is not None:
                login(request,user)
                return redirect('index')
            else:
                form.add_error(None,"Invalid email or password")
    
    return render(request,'login_user.html',{'form':form})

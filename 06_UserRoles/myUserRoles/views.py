from django.shortcuts import render,redirect
from django.contrib.auth import login,authenticate,logout
from .forms import CustomUserForm,UserLoginForm
# from django.http import request

# Create your views here.
def index(request):
    return render(request,'index.html')

def register_user(request):
    if request.method=="POST":
        form = CustomUserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = True 
            user.save()
            return mapUserToTemplate(request,user=user)
    else:
        form = CustomUserForm()
    return render(request,'registration/register_user.html',{'form':form})
    

def login_user(request):
    if request.method=="POST":
        form = UserLoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            print(f"{email} {password}")
            user = authenticate(request,email=email,password=password)
            
            print(user)
            if user is not None:
                login(request,user)
                return mapUserToTemplate(request,user)
            else :
                form.add_error(None,"Invalid email or password")
    else:
        form = UserLoginForm()
    return render(request,'registration/login_user.html',{'form':form})

def logout_user(request):
    if request.method=="POST":
        logout(request)
        return redirect('index')
    return render(request,'registration/logout_user.html')
        

def mapUserToTemplate(request,user):
    if user.role =="ADMIN":
        return render(request,'Dashboards/admin_dashboard.html')
    elif user.role=="MEMBER":
        return render(request,'Dashboards/member_dashboard.html')
    else:
        return render(request,'Dashboards/guest_dashboard.html')

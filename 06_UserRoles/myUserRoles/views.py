from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login,authenticate,logout
from django.http import HttpResponseForbidden

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
            login(request,user)
            return redirect_to_user_dashboard(user)
    else:
        form = CustomUserForm()
    return render(request,'registration/register_user.html',{'form':form})
    

def login_user(request):
    if request.method=="POST":
        form = UserLoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request,email=email,password=password)
            if user is not None:
                login(request,user)
                return redirect_to_user_dashboard(user)
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
        

def redirect_to_user_dashboard(user):
    role_urls ={
        'ADMIN' : 'admin_dashboard',
        'MEMBER': 'member_dashboard',
        'GUEST': 'guest_dashboard',
    }

    return redirect(role_urls.get(user.role,'guest_dashboard'))

@login_required(login_url='login_user')
def admin_dashboard(request):
    if request.user.role != 'ADMIN':
        return HttpResponseForbidden("You don't have permission to access this page.")
    return render(request, 'Dashboards/admin_dashboard.html', {'user': request.user})

@login_required(login_url='login_user')
def member_dashboard(request):
    if request.user.role != 'MEMBER':
        return HttpResponseForbidden("You don't have permission to access this page.")
    return render(request, 'Dashboards/member_dashboard.html', {'user': request.user})

@login_required(login_url='login_user')
def guest_dashboard(request):
    if request.user.role != 'GUEST':
        return HttpResponseForbidden("You don't have permission to access this page.")
    return render(request, 'Dashboards/guest_dashboard.html', {'user': request.user})
from django.shortcuts import render,redirect
from .forms import CustomUserForm
# from django.http import request

# Create your views here.
def index(request):
    return render(request,'index.html')

def register_user(request):
    if request.method=="POST":
        form = CustomUserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            if user.role =="ADMIN":
                return render(request,'Dashboards/admin_dashboard.html')
            elif user.role=="MEMBER":
                return render(request,'Dashboards/member_dashboard.html')
            else:
                return render(request,'Dashboards/guest_dashboard.html')
    else:
        form = CustomUserForm()
    return render(request,'registration/register_user.html',{'form':form})
    
            
from django.shortcuts import render,redirect
from .forms import CustomUserForm

# Create your views here.
def index(request):
    return render(request,'layout.html')


def register_view(request):
    form = CustomUserForm
    if request.method=="POST":
        form = CustomUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
        
    return render(request,'register_user.html',{'form':form})

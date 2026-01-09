from django.shortcuts import render,redirect
from .models import Student
from .forms import StudentCreationForm

# Create your views here.
def index(request):
    return render(request,'index.html')

def register(request):
    if request.method=="POST":
        form = StudentCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = StudentCreationForm()
    return render(request,'register.html',{'form':form})

        
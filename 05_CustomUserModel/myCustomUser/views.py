from django.shortcuts import render
from django.http import HttpResponse
from .forms import CreateCustomUserForm

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


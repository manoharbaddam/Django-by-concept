from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Notes
from .forms import CreateForm

# Create your views here.

def index(request):
    notes  = Notes.objects.all()
    return render(request,'notes/index.html',{'notes':notes})

def create_note(request):
    if request.method == "POST":
        form = CreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("index")
    else:
        form = CreateForm()

    return render(request,'notes/create_note.html',{'form':form})



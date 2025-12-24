from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from .models import Notes
from .forms import CreateForm

# Create your views here.

def index(request):
    notes  = Notes.objects.all().order_by('-created_at')
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

def view_note(request,note_id):
    note = Notes.objects.get(id=note_id)
    return render(request,'notes/view_note.html',{'note':note})

def edit_note(request,note_id):
    note = get_object_or_404(Notes,id=note_id)
    if request.method=="POST":
        form = CreateForm(request.POST,instance=note)
        if form.is_valid():
            form.save()
            return redirect("index")
    else:
        form = CreateForm(instance=note)
    return render(request,'notes/edit_note.html',{'form':form})

def delete_note(request,note_id):
    note = get_object_or_404(Notes,id=note_id)
    if request.method=="POST":
        note.delete()
        return redirect("index")

    return render(request,"notes/delete_note.html")

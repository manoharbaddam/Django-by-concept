from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from .models import Notes,Category
from .forms import CreateNoteForm

# Create your views here.
def index(request):
    notes = Notes.objects.order_by("category")
    cats = Category.objects.all()
    return render(request,'index.html',{'notes':notes,'cats':cats})

def create_note(request):
    if request.method == "POST":
        form = CreateNoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = CreateNoteForm()
    return render(request,'create_note.html',{'form':form})

def view_note(request,note_id):
    note = get_object_or_404(Notes,id=note_id)
    if not note:
        return redirect('create_note')
    return render(request,'view_note.html',{'note':note})

def edit_note(request,note_id):
    note = get_object_or_404(Notes,id=note_id)
    if request.method=="POST":
        form = CreateNoteForm(request.POST,instance=note)
        if form.is_valid():
            form.save()
            return redirect('index')  
    else:
        note = CreateNoteForm(instance=note)
    return render(request,'edit_note.html',{'form':note})


def delete_note(request,note_id):
    note = get_object_or_404(Notes,id=note_id)
    if request.method == "POST":
        note.delete()
        return redirect('index')
    return render(request,'delete_note.html',{'note':note})

def category_notes(request,cat_id):
    cat_title = Category.objects.get(id=cat_id)
    notes = Notes.objects.filter(category_id=cat_id)
    return render(request,'category_notes.html',{'notes':notes,'cat_title':cat_title})
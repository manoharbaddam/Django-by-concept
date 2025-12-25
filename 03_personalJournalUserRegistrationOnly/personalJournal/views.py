from django.shortcuts import render,redirect,get_object_or_404
from .forms import JournalCreationForm
from .models import Journal

# Create your views here.
def index(request):
    journals = Journal.objects.all()
    return render(request,'index.html',{'journals' : journals})

def create_journal(request):
    if request.method=="POST":
        form = JournalCreationForm(request.POST,request.FILES)
        if form.is_valid():
            journal = form.save(commit=False)
            journal.user = request.user
            journal.save()
            return redirect('index')
    else:
        form = JournalCreationForm()
    return render(request,'create_journal.html',{'form':form})

def view_journal(request,journal_id):
    journal = get_object_or_404(id=journal_id)
    return render(request,'view_journal.html',{'journal':journal})
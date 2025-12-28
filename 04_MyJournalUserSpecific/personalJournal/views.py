from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from  django.contrib.auth.decorators import login_required

from .forms import JournalCreationForm,UserRegistrationForm
from .models import Journal

# Create your views here.
def index(request):
    journals = Journal.objects.all()
    return render(request,'index.html',{'journals':journals})

@login_required
def user_journal(request):
    journals = Journal.objects.filter(author=request.user)
    return render(request,'user_journal.html',{'journals':journals})

@login_required
def create_journal(request):
    if request.method=="POST":
        form = JournalCreationForm(request.POST,request.FILES)
        if form.is_valid():
            journal = form.save(commit=False)
            journal.author = request.user
            journal.save()
            return redirect('user_journal')
    else:
        form  = JournalCreationForm()
    return render(request,'create_journal.html',{'form':form})

@login_required
def view_journal(request,journal_id):
    journal = get_object_or_404(Journal,id=journal_id)
    return render(request,'view_journal.html',{'journal':journal})

@login_required
def edit_journal(request,journal_id):
    journal  = get_object_or_404(Journal,id=journal_id)
    if request.method=="POST":
        form = JournalCreationForm(request.POST,request.FILES,instance=journal)
        if form.is_valid():
            form.save()
            return redirect('user_journal')
    else:
        form = JournalCreationForm(instance=journal)
    return render(request,'edit_journal.html',{'form':form})

@login_required
def delete_journal(request,journal_id):
    journal = get_object_or_404(Journal,id=journal_id)
    if request.method=="POST":
        journal.delete()    
        return redirect('user_journal')
    return render(request,'delete_journal.html',{'journal':journal})

def register(request):
    if request.method=="POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login_view')
    else:
        form = UserRegistrationForm()
    return render(request,'registration/register.html',{'form':form})


def login_view(request):
    if request.method=="POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('user_journal')
    return render(request,'registration/login.html')


def logout_view(request):
    if request.method=="POST":
        logout(request)
        return redirect('index')
    return render(request,'registration/logout.html')

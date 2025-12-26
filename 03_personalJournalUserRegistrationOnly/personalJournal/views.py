from django.shortcuts import render,redirect,get_object_or_404
from .forms import JournalCreationForm,UserRegistrationForm,UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login
from django.contrib import messages
from .models import Journal

# Create your views here.
def index(request):
    journals = Journal.objects.all()
    return render(request,'index.html',{'journals' : journals})

@login_required
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
    journal = get_object_or_404(Journal,id=journal_id)
    return render(request,'view_journal.html',{'journal':journal})

@login_required
def edit_journal(request,journal_id):
    journal = get_object_or_404(Journal,id=journal_id)
    if request.method == "POST":
        form = JournalCreationForm(request.POST,request.FILES,instance=journal)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = JournalCreationForm(instance=journal)
    return render(request,'edit_journal.html',{'form':form})


def register(request):
    if request.method=="POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password1'])
            user.save()
            return redirect('index')
    else:
        form = UserRegistrationForm()
    return render(request,'registration/register.html',{'form':form})

def login_view(request):
    if request.method =="POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request,username=username,password=password)

        if user is not None:
            login(request,user)
            return redirect('index')
        else:
            messages.info(request, 'This is an informational message!')
            return render(request,'login.html')
    return render(request,'registration/login.html')

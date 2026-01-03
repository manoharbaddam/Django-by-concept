from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from .forms import CustomUserForm, UserLoginForm


# Create your views here.
def index(request):
    return render(request, "layout.html")


def register_view(request):
    form = CustomUserForm()
    if request.method == "POST":
        form = CustomUserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = True
            user.save()
            login(request, user)
            return redirect("index")

    return render(request, "register_user.html", {"form": form})


def login_view(request):
    form = UserLoginForm()
    if request.method == "POST":
        form = UserLoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password"]
            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                return redirect("index")
            else:
                form.add_error(None, "Invalid email or password")

    return render(request, "login_user.html", {"form": form})


def logout_view(request):
    if request.method == "POST":
        logout(request)
        return redirect("index")

    return render(request, "logout_user.html")

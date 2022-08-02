from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from .forms import RegisterUserForm
from django.contrib import messages
# Create your views here.

def Home(request):
    return render(request, "index.html")

def SignUp(request):
    if request.method == "POST":
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Succsessfully Job :) ")
            return redirect("users:LI")
        # else:
        #     messages.error(request, "Something went to wrong!")
    form = RegisterUserForm
    return render(request, "register/signup.html", context={"form":form})


def Login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f"Welcome to Our Team {user.username}")
                return redirect("users:HM")
            messages.error(request, "Something went to wrong!")
        messages.error(request, "Something went to wrong!")
    form = AuthenticationForm
    return render(request, "register/login.html", {"form":form})

def Logout(request):
    logout(request)
    messages.info(request, "Hayr ((")
    return redirect("users:HM")
from django.core.exceptions import ValidationError
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login
from django.contrib.auth import logout as django_logout
from . import forms
# Create your views here.

def need_account(request):
    return render(request,"need-account.html")


def logout(request):
    django_logout(request)
    return redirect("areas:index")


def register(request):
    form = forms.RegisterForm()
    if request.method == "POST":
        form = forms.RegisterForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect("areas:index")
    context = {
    "form":form
    }
    return render(request,"register.html",context)


def loginPage(request):
    form = forms.LoginForm()
    if request.method == "POST":
        form = forms.LoginForm(request.POST)
        username = request.POST.get("username")
        password = request.POST.get("password")
        
        account = authenticate(request,username=username,password=password)
        if account is None:
            raise ValidationError(request,"Istifadeci Adiniz Ve Ya Parolunuz Sehvdir!")
        else:
            login(request,account)
            return redirect("areas:index")

    context = {
        "form":form
    }
    return render(request,"login.html",context)
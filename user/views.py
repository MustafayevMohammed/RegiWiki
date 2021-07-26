from django.core.exceptions import ValidationError
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login
from django.contrib.auth import logout as django_logout

from areas import models
from . import forms
from django.contrib import messages
from areas.models import CommentModel
from django.contrib.auth.decorators import login_required
# Create your views here.

def need_account(request):
    return render(request,"need-account.html")


def logout(request):
    django_logout(request)
    messages.success(request,"Ugurla Cixis Etdiniz :)")
    return redirect("areas:index")


def register(request):
    form = forms.RegisterForm()
    if request.method == "POST":
        form = forms.RegisterForm(request.POST)
        if form.is_valid:
            form.save()
            messages.success(request,"Hesab Ugurla Yaradildi Indi Yaratdiginiz Hesaba Giris Etmelisiniz :)")
            return redirect("user:login")
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

@login_required(login_url="user:need_account")
def profile(request):
    comments = CommentModel.objects.filter(yazan=request.user)
    # comments = CommentModel.objects.filter(yazan=request.user)

    context = {
        "comments":comments
    }
    return render(request,"profile.html",context)

def profileConversation(request,id):
    yazi = models.CommentModel.objects.get(id=id)
    conversations = models.ConversationModel.objects.filter(comment=yazi)

    context = {
        "conversations":conversations,
    }
    return render(request,"convdetail.html",context)
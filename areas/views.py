from django.shortcuts import render,redirect

from areas import models
from . import forms
from areas.models import CommentModel
from django.contrib import messages


# Create your views here.
def index(request):
    return render(request,"index.html")


def addcomment(request):
    form = forms.CommentForm()

    if request.method == "POST":
        form = forms.CommentForm(request.POST,request.FILES)
        if form.is_valid:
            instance = form.save(commit=False)
            instance.yazan = request.user
            instance.save()
            return redirect("/")
    
    context = {
        "form":form
    }
    return render(request,"addcomment.html",context)

def deletecomment(request,id):
    comment = CommentModel.objects.get(id=id)
    comment.delete()
    messages.success(request ,"Comment Silindi:)")
    return redirect("user:profile")

def updatecomment(request,id):
    comment = CommentModel.objects.get(id=id)
    form = forms.CommentForm(instance=comment)
    
    if request.method == "POST":
        form = forms.CommentForm(request.POST,instance=comment)
        if form.is_valid():
            form.save()
            return redirect("/user/profile/")
    
    context = {
        "form":form
    }
    return render(request,"update_task.html",context)


def areas(request):
    areas = models.RayonModel.objects.all()

    context = {
        "areas":areas
    }

    return render(request,"areas.html",context)

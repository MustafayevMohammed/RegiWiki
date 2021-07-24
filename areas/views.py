from django.shortcuts import render,redirect
from django.core.paginator import Paginator
from areas import models
from . import forms
from areas.models import CommentModel
from django.contrib import messages
from django.db.models import Q

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
    sorgu = request.GET.get('sorgu')
    areas = models.RayonModel.objects.all()
    if sorgu:
        areas = areas.filter(
            Q(ad__icontains=sorgu)
        ).distinct()

    sehife = request.GET.get("sehife")
    paginator = Paginator(areas,12)


    context = {
        "areas":paginator.get_page(sehife)
    }
    return render(request,"areas.html",context)


def area_detail(request,id):
    area = models.RayonModel.objects.get(id=id)
    comments = models.CommentModel.objects.filter(rayon=area)
    
    context = {
        "area":area,
        "comments":comments
    }
    return render(request,"area_detail.html",context)
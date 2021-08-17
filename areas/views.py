from django.shortcuts import render,redirect
from django.core.paginator import Paginator
from areas import models
from . import forms
from areas.models import CommentModel
from django.contrib import messages
from django.db.models import Q, fields
from django.contrib.auth.decorators import login_required


# Create your views here.
def index(request):
    if request.user.is_authenticated:
        return redirect("areas:posts")
    return render(request,"index.html")

@login_required(login_url="user:need_account")
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


@login_required(login_url="user:need_account")
def deletecomment(request,id):
    comment = CommentModel.objects.get(id=id)
    comment.delete()
    messages.success(request ,"Comment Silindi:)")
    return redirect("user:profile")


@login_required(login_url="user:need_account")
def updatecomment(request,id):
    comment = CommentModel.objects.get(id=id)
    form = forms.CommentForm(instance=comment)
    
    if request.method == "POST":
        form = forms.CommentForm(request.POST,request.FILES,instance=comment)
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
            Q(ad__startswith=sorgu)
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
    # form = forms.CommentForm()
    # if request.method == "POST":
    #     form = forms.CommentForm(request.POST,request.FILES)
    #     if form.is_valid:
    #         instance = form.save(commit=False)
    #         instance.yazan = request.user
    #         instance.rayon = area
    #         instance.save()
    #         return redirect("areas:area_detail/area.id")

    context = {
        "area":area,
        "comments":comments,
        # "form":form,
    }
    return render(request,"area_detail.html",context)


def regions(request):
    regions = models.RegionModel.objects.all()

    context = {
        "regions":regions,
    }
    return render(request,"regions.html",context)


def posts(request):
    comments = models.CommentModel.objects.all()
    context = {
        "comments":comments,
    }
    return render(request,"posts.html",context)

@login_required(login_url="user:need_account")
def addConversation(request,id):
    yazi = models.CommentModel.objects.get(id=id)
    convs = models.ConversationModel.objects.filter(comment=yazi)
    form = forms.ConversationForm()
    if request.method == "POST":
        form = forms.ConversationForm(request.POST)
        if form.is_valid:
            instance = form.save(commit=False)
            instance.comment = yazi    
            instance.yazan = request.user
            instance.save()
            return redirect("areas:posts")
    
    context = {
        "form":form,
        "convs":convs
    }
    return render(request,"addconv.html",context)

@login_required(login_url="user:need_account")
def deleteConversation(request,id):
    conversation = models.ConversationModel.objects.get(id=id)
    conversation.delete()
    messages.success(request,"Yaziniz Ugurla Silindi")
    return redirect("areas:posts")

from django.db.models.expressions import F
from django.shortcuts import render,redirect
from . import forms

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
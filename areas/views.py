from django.shortcuts import render,redirect
from . import models
# Create your views here.

def index(request):
    areas = models.Area.objects.all()
    context={
        "areas":areas
    }

    return render(request,"index.html",context)
from os import name
from django.urls import path
from . import views
app_name = "areas"

urlpatterns = [
    path("",views.index,name="index"),
    path("addcomment/",views.addcomment,name="addcomment")
    ]
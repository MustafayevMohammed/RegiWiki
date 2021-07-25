from os import name
from django.urls import path
from . import views
app_name = "areas"

urlpatterns = [
    path("",views.index,name="index"),
    path("addcomment/",views.addcomment,name="addcomment"),
    path("delete-comment/<id>",views.deletecomment,name="delete_comment"),
    path("update-task/<id>",views.updatecomment,name="update_comment"),
    path("areas/",views.areas,name="areas"),
    path("area/<id>",views.area_detail,name="area_detail"),
    path("regions/",views.regions,name="regions"),
]
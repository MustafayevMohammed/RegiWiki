from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from .import views

app_name="areas"

urlpatterns = [
    path('',views.index,name="index"),
]
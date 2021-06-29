from django.contrib import admin
from . import models
# Register your models here.
@admin.register(models.RegionModel)
class RegionAdmin(admin.ModelAdmin):
    list_display = ("ad","sahe","ehali")

@admin.register(models.RayonModel)
class RayonAdmin(admin.ModelAdmin):
    list_display = ["ad","region","sahe","ehali"]
    list_display_links = ["ad","region","sahe","ehali"]
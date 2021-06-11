from django.contrib import admin
from . import models
# Register your models here.
@admin.register(models.Area)
class AreaAdmin(admin.ModelAdmin):
    list_display=["id","title"]
    
    class Meta:
        model = models.Area
        
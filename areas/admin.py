from django.contrib.admin.helpers import AdminForm
from django.contrib.admin.options import ModelAdmin
from areas.models import Areas
from django.contrib import admin
from .models import Areas
# Register your models here.
@admin.register(Areas)
class Areasadmin(admin.ModelAdmin):
    list_display=['id','title']
    class Meta:
        model=Areas
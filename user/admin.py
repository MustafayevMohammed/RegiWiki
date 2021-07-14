from django.contrib.admin.decorators import register
from user.models import CustomUserModel
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUserModel

# Register your models here.

class CustomAdmin(UserAdmin):
    model = CustomUserModel
    list_display = ["username","email"]
    fieldsets = UserAdmin.fieldsets + (
        ('Profil sekli deyistir',{
            'fields':['prophile_photo']
        }),
    )

admin.site.register(CustomUserModel,CustomAdmin)

from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class CustomUserModel(AbstractUser):
    prophile_photo = models.ImageField(upload_to="prophile_photos",blank=True,null=True)

    class Meta:
        db_table = 'user'

    def __str__(self):
        return self.username
    
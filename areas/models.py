from email.policy import default
from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.expressions import Case
from django.db.models.fields import CharField, TextField
from django.db.models.fields.related import ForeignKey, OneToOneField
from django.contrib.auth.models import User
# Create your models here.

class RegionModel(models.Model):
    ad = models.CharField(verbose_name="Region Adi:",max_length=30)
    sahe = models.FloatField(verbose_name="Sahesi min km² ile")
    ehali = models.FloatField(verbose_name="Ehali min:" ,null=True ,blank=True)
    
    def __str__(self):
        return self.ad


class RayonModel(models.Model):
    sekil = models.ImageField(upload_to="rayon_sekilleri",null=True,blank=True)
    region = ForeignKey(RegionModel,on_delete=CASCADE,verbose_name="Region:",related_name="rayonlar")
    melumat = TextField(verbose_name="Melumat:")
    ad = models.CharField(verbose_name="Rayon Adi:",max_length=35)
    sahe = models.FloatField(verbose_name="Sahesi km² ile:",null=True,blank=True)
    ehali = models.FloatField(verbose_name="Ehali min:" ,null=True ,blank=True)

    def __str__(self):
        return self.ad
    
    
class CommentModel(models.Model):
    rayon = models.ForeignKey("Rayonmodel",related_name="comments",on_delete=CASCADE)
    basliq = models.CharField(max_length=120,verbose_name="Basliq:")
    mezmun = models.TextField(verbose_name="Mezmun:")
    created_date = models.DateTimeField(auto_now_add=True)
    sekil = models.ImageField(upload_to="koment_sekilleri",null=True,blank=True,default="/koment_sekilleri/default_landscape.png")
    yazan = models.ForeignKey('user.CustomUserModel',related_name="comments",on_delete=CASCADE,null=True,blank=True)

    def __str__(self):
        return self.basliq
    
class ConversationModel(models.Model):
    comment = models.ForeignKey("CommentModel",related_name="conversations",on_delete=models.CASCADE)
    mezmun = models.TextField(verbose_name="Mezmun:")
    created_date = models.DateTimeField(auto_now_add=True)
    yazan = models.ForeignKey('user.CustomUserModel',related_name="conversations",on_delete=models.CASCADE,null=True,blank=True)

    def __str__(self):
        return self.mezmun
    
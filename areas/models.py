from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields import TextField
from django.db.models.fields.related import ForeignKey, OneToOneField

# Create your models here.

class RegionModel(models.Model):
    ad = models.CharField(verbose_name="Region Adi:",max_length=30)
    sahe = models.FloatField(verbose_name="Sahesi min km² ile")
    ehali = models.FloatField(verbose_name="Ehali min:" ,null=True ,blank=True)
    
    def __str__(self):
        return self.ad


class RayonModel(models.Model):
    region = ForeignKey(RegionModel,on_delete=CASCADE,verbose_name="Region:")
    melumat = TextField(verbose_name="Melumat:")
    ad = models.CharField(verbose_name="Rayon Adi:",max_length=35)
    sahe = models.FloatField(verbose_name="Sahesi min km² ile:",null=True,blank=True)
    ehali = models.FloatField(verbose_name="Ehali min:" ,null=True ,blank=True)
    
from django.db import models

# Create your models here.

class Area(models.Model):
    title = models.CharField(verbose_name="Basliq:",max_length=35)
    content = models.TextField(verbose_name="Mezmun:")
    image = models.ImageField(verbose_name="Sekil:")
    
    def __str__(self):
        return self.title
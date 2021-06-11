from django.db import models

# Create your models here.
class Areas(models.Model):
    id = models.AutoField(primary_key=True)
    title=models.CharField(verbose_name='Başlıq', max_length=20)
    content=models.CharField(verbose_name='Məzmun',max_length=100)
    image=models.ImageField(verbose_name='Şəkil')
    def __str__(self):
        return self.title
# Generated by Django 3.1.7 on 2021-06-29 07:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('areas', '0006_auto_20210629_1152'),
    ]

    operations = [
        migrations.AlterField(
            model_name='regionmodel',
            name='ad',
            field=models.CharField(max_length=30, verbose_name='Region Adi:'),
        ),
    ]
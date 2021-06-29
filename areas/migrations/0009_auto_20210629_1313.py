# Generated by Django 3.1.7 on 2021-06-29 09:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('areas', '0008_rayonmodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='rayonmodel',
            name='ehali',
            field=models.FloatField(blank=True, null=True, verbose_name='Ehali min:'),
        ),
        migrations.AddField(
            model_name='rayonmodel',
            name='sahe',
            field=models.FloatField(blank=True, null=True, verbose_name='Sahesi min km² ile:'),
        ),
    ]
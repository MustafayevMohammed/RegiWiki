# Generated by Django 3.1.7 on 2021-06-29 07:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('areas', '0002_regionmodel_ehali'),
    ]

    operations = [
        migrations.AlterField(
            model_name='regionmodel',
            name='ehali',
            field=models.IntegerField(blank=True, null=True, verbose_name='Ehali:'),
        ),
    ]
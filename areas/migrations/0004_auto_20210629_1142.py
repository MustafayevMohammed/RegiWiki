# Generated by Django 3.1.7 on 2021-06-29 07:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('areas', '0003_auto_20210629_1136'),
    ]

    operations = [
        migrations.AlterField(
            model_name='regionmodel',
            name='sahe',
            field=models.IntegerField(verbose_name='Sahesi km² ile'),
        ),
    ]

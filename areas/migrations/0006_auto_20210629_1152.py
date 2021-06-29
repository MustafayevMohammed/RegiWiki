# Generated by Django 3.1.7 on 2021-06-29 07:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('areas', '0005_auto_20210629_1148'),
    ]

    operations = [
        migrations.AlterField(
            model_name='regionmodel',
            name='ehali',
            field=models.FloatField(blank=True, null=True, verbose_name='Ehali min:'),
        ),
        migrations.AlterField(
            model_name='regionmodel',
            name='sahe',
            field=models.FloatField(verbose_name='Sahesi min km² ile'),
        ),
    ]
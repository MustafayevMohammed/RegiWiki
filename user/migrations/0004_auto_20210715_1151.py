# Generated by Django 3.1.7 on 2021-07-15 07:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_auto_20210715_1149'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customusermodel',
            name='prophile_photo',
            field=models.ImageField(blank=True, default='/prophile_photos/instagram_default.png', null=True, upload_to='prophile_photos'),
        ),
    ]
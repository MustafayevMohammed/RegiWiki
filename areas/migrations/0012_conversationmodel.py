# Generated by Django 3.1.7 on 2021-07-01 06:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('areas', '0011_auto_20210701_1040'),
    ]

    operations = [
        migrations.CreateModel(
            name='ConversationModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mezmun', models.TextField(verbose_name='Mezmun:')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('comment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='conversations', to='areas.commentmodel')),
            ],
        ),
    ]

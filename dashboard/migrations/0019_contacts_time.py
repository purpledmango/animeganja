# Generated by Django 2.2.7 on 2019-12-14 03:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0018_auto_20191214_0837'),
    ]

    operations = [
        migrations.AddField(
            model_name='contacts',
            name='time',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
# Generated by Django 2.2.7 on 2019-11-24 22:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0006_auto_20191124_2221'),
    ]

    operations = [
        migrations.AddField(
            model_name='episodes',
            name='episode_no',
            field=models.IntegerField(null=True, verbose_name='Episode no.'),
        ),
    ]

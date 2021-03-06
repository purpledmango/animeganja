# Generated by Django 2.2.7 on 2019-11-24 16:48

from django.db import migrations
import optimized_image.fields


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0004_auto_20191124_2038'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newanime',
            name='thumbnail',
            field=optimized_image.fields.OptimizedImageField(help_text='Upload the Official Anime Poster', null=True, upload_to='media/', verbose_name='Thumbanail'),
        ),
    ]

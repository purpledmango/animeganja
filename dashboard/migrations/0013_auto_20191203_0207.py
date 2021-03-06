# Generated by Django 2.2.7 on 2019-12-02 20:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0012_auto_20191127_1506'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='episodes',
            options={'ordering': ['date'], 'verbose_name_plural': 'Episodes'},
        ),
        migrations.AlterModelOptions(
            name='newanime',
            options={'ordering': ['-date'], 'verbose_name_plural': 'Animes'},
        ),
        migrations.AlterField(
            model_name='newanime',
            name='language',
            field=models.CharField(choices=[('Sub', 'SUB'), ('Dub', 'DUB')], default='SUB', max_length=8, null=True, verbose_name='Language'),
        ),
    ]

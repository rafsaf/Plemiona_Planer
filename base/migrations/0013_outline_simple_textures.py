# Generated by Django 3.2.2 on 2021-05-14 23:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0012_outline_choice_sort'),
    ]

    operations = [
        migrations.AddField(
            model_name='outline',
            name='simple_textures',
            field=models.BooleanField(default=False),
        ),
    ]

# Generated by Django 4.1.2 on 2022-11-17 23:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("base", "0060_profile_input_data_type"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="outline",
            name="initial_outline_maximum_front_dist",
        ),
        migrations.AlterField(
            model_name="outline",
            name="input_data_type",
            field=models.CharField(
                choices=[
                    ("Army collection", "Army collection"),
                    ("Deff collection", "Deff collection "),
                ],
                default="Army collection",
                max_length=32,
            ),
        ),
        migrations.AlterField(
            model_name="profile",
            name="input_data_type",
            field=models.CharField(
                choices=[
                    ("Army collection", "Army collection"),
                    ("Deff collection", "Deff collection "),
                ],
                default="Army collection",
                max_length=32,
            ),
        ),
    ]

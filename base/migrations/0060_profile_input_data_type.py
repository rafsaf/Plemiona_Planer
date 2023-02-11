# Generated by Django 4.1.2 on 2022-11-12 22:36

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("base", "0059_outline_input_data_type"),
    ]

    operations = [
        migrations.AddField(
            model_name="profile",
            name="input_data_type",
            field=models.CharField(
                choices=[
                    ("Army collection", "Army collection"),
                    ("Deff collection", "Deff collection"),
                ],
                default="Army collection",
                max_length=32,
            ),
        ),
    ]

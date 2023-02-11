# Generated by Django 4.0.4 on 2022-04-25 21:49

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("base", "0048_payment_promotion"),
    ]

    operations = [
        migrations.AddField(
            model_name="pdfpaymentsummary",
            name="created_at",
            field=models.DateTimeField(
                auto_now_add=True, default=django.utils.timezone.now
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="pdfpaymentsummary",
            name="updated_at",
            field=models.DateTimeField(auto_now=True),
        ),
    ]

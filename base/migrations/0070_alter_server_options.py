# Generated by Django 4.2.2 on 2023-06-10 18:17

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("base", "0069_profile_send_message_text_message_and_more"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="server",
            options={"ordering": ("dns",)},
        ),
    ]

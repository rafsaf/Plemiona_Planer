# Copyright 2023 Rafał Safin (rafsaf). All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==============================================================================

# Generated by Django 4.1.4 on 2022-12-20 16:14

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("base", "0063_payment_is_completed_payment_language_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="outline",
            name="send_message_with_url",
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name="profile",
            name="send_message_with_url",
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name="profile",
            name="sending_option",
            field=models.CharField(
                choices=[
                    ("default", "(Default) Auto generated, fully equipped safe links"),
                    ("string", "Text simple directly in message"),
                    ("extended", "Text extended directly in message"),
                    ("deputy", "Text for deputy directly in message"),
                ],
                default="default",
                max_length=50,
            ),
        ),
    ]

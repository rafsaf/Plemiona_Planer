# Copyright 2021 Rafał Safin (rafsaf). All Rights Reserved.
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

# Generated by Django 3.0.7 on 2021-02-28 17:31

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("base", "0009_auto_20210218_1528"),
    ]

    operations = [
        migrations.AddField(
            model_name="weightmodel",
            name="t1",
            field=models.TimeField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name="weightmodel",
            name="t2",
            field=models.TimeField(blank=True, default=None, null=True),
        ),
    ]

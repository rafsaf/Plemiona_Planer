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

# Generated by Django 4.2.7 on 2023-11-10 09:44

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("base", "0076_weightmaximum_nobles_limit_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="world",
            old_name="last_update",
            new_name="created_at",
        ),
        migrations.AddField(
            model_name="targetvertex",
            name="player_created_at",
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name="world",
            name="updated_at",
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name="player",
            name="name",
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name="targetvertex",
            name="target",
            field=models.CharField(max_length=7),
        ),
        migrations.AlterField(
            model_name="villagemodel",
            name="coord",
            field=models.CharField(max_length=7),
        ),
        migrations.AlterField(
            model_name="weightmaximum",
            name="start",
            field=models.CharField(max_length=7),
        ),
        migrations.AddIndex(
            model_name="villagemodel",
            index=models.Index(
                fields=["world", "coord"], name="base_villag_world_i_864875_idx"
            ),
        ),
        migrations.AddIndex(
            model_name="villagemodel",
            index=models.Index(
                fields=["world", "player"], name="base_villag_world_i_b7a1ab_idx"
            ),
        ),
        migrations.AddIndex(
            model_name="villagemodel",
            index=models.Index(
                fields=["world", "village_id"], name="base_villag_world_i_08015e_idx"
            ),
        ),
    ]

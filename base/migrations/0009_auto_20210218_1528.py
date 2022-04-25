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

# Generated by Django 3.0.7 on 2021-02-18 14:28

import datetime

import django.core.validators
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("base", "0008_auto_20210205_2111"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="weightmaximum",
            name="nobleman_in_village",
        ),
        migrations.RemoveField(
            model_name="weightmaximum",
            name="off_in_village",
        ),
        migrations.RemoveField(
            model_name="weightmodel",
            name="t1",
        ),
        migrations.RemoveField(
            model_name="weightmodel",
            name="t2",
        ),
        migrations.AddField(
            model_name="outline",
            name="avaiable_ruins",
            field=models.IntegerField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name="outline",
            name="default_fake_time_id",
            field=models.IntegerField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name="outline",
            name="default_off_time_id",
            field=models.IntegerField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name="outline",
            name="default_ruin_time_id",
            field=models.IntegerField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name="outline",
            name="filter_targets_number",
            field=models.IntegerField(
                default=12,
                validators=[
                    django.core.validators.MinValueValidator(1),
                    django.core.validators.MaxValueValidator(50),
                ],
            ),
        ),
        migrations.AddField(
            model_name="outline",
            name="initial_outline_average_ruining_points",
            field=models.CharField(
                choices=[
                    ("big", "Average greater than 8k"),
                    ("medium", "Average 5-8k"),
                ],
                default="big",
                max_length=150,
            ),
        ),
        migrations.AddField(
            model_name="outline",
            name="initial_outline_catapult_default",
            field=models.IntegerField(
                choices=[
                    (50, "50"),
                    (75, "75"),
                    (100, "100"),
                    (150, "150"),
                    (200, "200"),
                ],
                default=100,
            ),
        ),
        migrations.AddField(
            model_name="outline",
            name="initial_outline_fake_mode",
            field=models.CharField(
                choices=[
                    ("off", "Fakes only from off villages"),
                    ("all", "Fakes from all villages"),
                ],
                default="off",
                max_length=60,
            ),
        ),
        migrations.AddField(
            model_name="outline",
            name="initial_outline_fakes",
            field=models.TextField(blank=True, default=""),
        ),
        migrations.AddField(
            model_name="outline",
            name="initial_outline_off_left_catapult",
            field=models.IntegerField(
                default=50,
                validators=[
                    django.core.validators.MinValueValidator(0),
                    django.core.validators.MaxValueValidator(400),
                ],
            ),
        ),
        migrations.AddField(
            model_name="outline",
            name="initial_outline_ruining_order",
            field=models.CharField(
                choices=[
                    ("first", "Farm -> Headquarters -> Smithy -> Barracks -> EKO..."),
                    ("second", "Farm -> Headquarters -> Warehouse -> Smithy -> EKO..."),
                ],
                default="first",
                max_length=150,
            ),
        ),
        migrations.AddField(
            model_name="outline",
            name="initial_outline_ruins",
            field=models.TextField(blank=True, default=""),
        ),
        migrations.AddField(
            model_name="overview",
            name="extended",
            field=models.TextField(default=""),
        ),
        migrations.AddField(
            model_name="profile",
            name="validity_date",
            field=models.DateField(
                blank=True, default=datetime.date(2021, 2, 25), null=True
            ),
        ),
        migrations.AddField(
            model_name="targetvertex",
            name="ruin",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="weightmaximum",
            name="catapult_left",
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name="weightmaximum",
            name="catapult_max",
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name="weightmaximum",
            name="catapult_state",
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name="weightmodel",
            name="building",
            field=models.CharField(
                blank=True,
                choices=[
                    ("headquarters", "Headquarters"),
                    ("barracks", "Barracks"),
                    ("stable", "Stable"),
                    ("workshop", "Workshop"),
                    ("church", "Church"),
                    ("academy", "Academy"),
                    ("smithy", "Smithy"),
                    ("rally_point", "Rally point"),
                    ("statue", "Statue"),
                    ("market", "Market"),
                    ("timber_camp", "Timber camp"),
                    ("clay_pit", "Clay pit"),
                    ("iron_mine", "Iron mine"),
                    ("farm", "Farm"),
                    ("warehouse", "Warehouse"),
                    ("wall", "wall"),
                ],
                default=None,
                max_length=50,
                null=True,
            ),
        ),
        migrations.AddField(
            model_name="weightmodel",
            name="catapult",
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name="weightmodel",
            name="ruin",
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name="outline",
            name="initial_outline_targets",
            field=models.TextField(blank=True, default=""),
        ),
        migrations.CreateModel(
            name="Payment",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "status",
                    models.CharField(
                        choices=[("finished", "Finished"), ("returned", "Returned")],
                        default="finished",
                        max_length=30,
                    ),
                ),
                ("send_mail", models.BooleanField(default=True)),
                ("amount", models.IntegerField()),
                ("payment_date", models.DateField()),
                ("months", models.IntegerField(default=1)),
                ("comment", models.CharField(blank=True, default="", max_length=150)),
                ("new_date", models.DateField(blank=True, default=None, null=True)),
                (
                    "user",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]

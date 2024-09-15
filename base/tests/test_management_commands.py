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


import datetime

from django.conf import settings
from django.core.management import call_command

from base.models import Outline, OutlineOverview, Overview, Server, World
from base.tests.test_utils.create_user import create_user


def test_create_servers_command() -> None:
    call_command("createservers")

    assert Server.objects.all().count() == len(settings.TRIBAL_WARS_SUPPORTED_SERVERS)

    for server in Server.objects.all():
        worlds: list[World] = list(World.objects.filter(server=server))
        assert len(worlds) == 1
        assert worlds[0].postfix == "Test"


def test_orphanedoutlineoverviewsdelete_no_delete_with_outline() -> None:
    Server.objects.create(
        dns="testserver",
        prefix="te",
    )
    world = World.objects.get(postfix="Test")
    outline = Outline.objects.create(
        name="",
        date=datetime.date.today(),
        world=world,
        owner=create_user("user", "password"),
    )
    OutlineOverview.objects.create(outline=outline)

    call_command("orphanedoutlineoverviewsdelete")

    assert OutlineOverview.objects.count() == 1


def test_orphanedoutlineoverviewsdelete_no_delete_with_overview() -> None:
    outline_overview = OutlineOverview.objects.create(outline=None)
    Overview.objects.create(
        outline_overview=outline_overview,
        outline=None,
        player="xxxx",
        token="abcd",
        table="xxxx",
        string="xxxx",
        deputy="xxxx",
        extended="xxxx",
    )

    call_command("orphanedoutlineoverviewsdelete")

    assert OutlineOverview.objects.count() == 1


def test_orphanedoutlineoverviewsdelete_delete() -> None:
    OutlineOverview.objects.create(outline=None)

    call_command("orphanedoutlineoverviewsdelete")

    assert OutlineOverview.objects.count() == 0

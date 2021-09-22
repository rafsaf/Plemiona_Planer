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

from django.urls import reverse

from base.models import TargetVertex
from base.tests.test_utils.mini_setup import MiniSetup


class InitialSetAllTime(MiniSetup):
    def test_planer_set_all_time___302_not_auth_redirect_login(self):
        outline = self.get_outline()
        outline_time = self.create_outline_time(outline)
        PATH = reverse("base:planer_set_all_time", args=[outline_time.pk])

        response = self.client.get(PATH)
        assert response.status_code == 302
        response = self.client.post(PATH)
        assert response.status_code == 302
        assert response.url == self.login_page_path(next=PATH)

    def test_planer_set_all_time___404_foreign_user_no_access(self):
        outline = self.get_outline()
        outline_time = self.create_outline_time(outline)
        PATH = reverse("base:planer_set_all_time", args=[outline_time.pk])

        self.login_foreign_user()
        response = self.client.get(PATH)
        assert response.status_code == 405

        response = self.client.post(PATH)
        assert response.status_code == 404

    def test_planer_set_all_time___302_change_correct_for_real(self):
        outline = self.get_outline()
        self.create_target_on_test_world(outline)
        self.create_target_on_test_world(outline, fake=True, coord="201|200")
        self.create_target_on_test_world(outline, ruin=True, coord="202|200")
        outline_time = self.create_outline_time(outline)

        PATH = (
            reverse("base:planer_set_all_time", args=[outline_time.pk])
            + "?page=2&mode=time"
        )
        REDIRECT = (
            reverse("base:planer_initial", args=[outline.pk]) + "?page=2&mode=time"
        )

        self.login_me()
        response = self.client.get(PATH)
        assert response.status_code == 405

        response = self.client.post(PATH)
        assert response.status_code == 302
        assert response.url == REDIRECT

        real_target: TargetVertex = TargetVertex.objects.get(target="200|200")
        assert real_target.outline_time == outline_time
        fake_target: TargetVertex = TargetVertex.objects.get(target="201|200")
        assert fake_target.outline_time is None
        ruin_target: TargetVertex = TargetVertex.objects.get(target="202|200")
        assert ruin_target.outline_time is None

        outline.refresh_from_db()
        assert outline.default_off_time_id == outline_time.pk

    def test_planer_set_all_time___302_change_correct_for_fake(self):
        outline = self.get_outline()
        self.create_target_on_test_world(outline)
        self.create_target_on_test_world(outline, fake=True, coord="201|200")
        self.create_target_on_test_world(outline, ruin=True, coord="202|200")
        outline_time = self.create_outline_time(outline)

        PATH = (
            reverse("base:planer_set_all_time", args=[outline_time.pk])
            + "?page=2&mode=time&fake=true"
        )
        REDIRECT = (
            reverse("base:planer_initial", args=[outline.pk]) + "?page=2&mode=time"
        )

        self.login_me()
        response = self.client.get(PATH)
        assert response.status_code == 405

        response = self.client.post(PATH)
        assert response.status_code == 302
        assert response.url == REDIRECT

        real_target: TargetVertex = TargetVertex.objects.get(target="200|200")
        assert real_target.outline_time is None
        fake_target: TargetVertex = TargetVertex.objects.get(target="201|200")
        assert fake_target.outline_time == outline_time
        ruin_target: TargetVertex = TargetVertex.objects.get(target="202|200")
        assert ruin_target.outline_time is None

        outline.refresh_from_db()
        assert outline.default_fake_time_id == outline_time.pk

    def test_planer_set_all_time___302_change_correct_for_ruin(self):
        outline = self.get_outline()
        self.create_target_on_test_world(outline)
        self.create_target_on_test_world(outline, fake=True, coord="201|200")
        self.create_target_on_test_world(outline, ruin=True, coord="202|200")
        outline_time = self.create_outline_time(outline)

        PATH = (
            reverse("base:planer_set_all_time", args=[outline_time.pk])
            + "?page=2&mode=time&ruin=true"
        )
        REDIRECT = (
            reverse("base:planer_initial", args=[outline.pk]) + "?page=2&mode=time"
        )

        self.login_me()
        response = self.client.get(PATH)
        assert response.status_code == 405

        response = self.client.post(PATH)
        assert response.status_code == 302
        assert response.url == REDIRECT

        real_target: TargetVertex = TargetVertex.objects.get(target="200|200")
        assert real_target.outline_time is None
        fake_target: TargetVertex = TargetVertex.objects.get(target="201|200")
        assert fake_target.outline_time is None
        ruin_target: TargetVertex = TargetVertex.objects.get(target="202|200")
        assert ruin_target.outline_time == outline_time

        outline.refresh_from_db()
        assert outline.default_ruin_time_id == outline_time.pk

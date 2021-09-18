from django.urls import reverse

from base.models import WeightModel
from base.tests.test_utils.mini_setup import MiniSetup


class CompleteOutline(MiniSetup):
    def test_planer_complete___302_not_auth_redirect_login(self):
        outline = self.get_outline()
        PATH = reverse("base:planer_complete", args=[outline.pk])

        response = self.client.get(PATH)
        assert response.status_code == 302
        response = self.client.post(PATH)
        assert response.status_code == 302
        assert response.url == self.login_page_path(next=PATH)

    def test_planer_complete___404_foreign_user_no_access(self):
        outline = self.get_outline()
        PATH = reverse("base:planer_complete", args=[outline.pk])

        self.login_foreign_user()
        response = self.client.get(PATH)
        assert response.status_code == 405

        response = self.client.post(PATH)
        assert response.status_code == 404

    def test_planer_complete___302_redirect_when_no_premium_and_25_targets(self):
        outline = self.get_outline(test_world=True)
        outline.off_troops = "102|102,100,100,7002,0,100,2802,0,0,350,100,0,0,0,0,0,"
        outline.save()
        self.create_target_on_test_world(outline=outline, many=26)

        PATH = reverse("base:planer_complete", args=[outline.pk]) + f"?t=ruin"
        REDIRECT = reverse("base:planer_initial_form", args=[outline.pk]) + f"?t=ruin"

        self.login_me()
        response = self.client.get(PATH)
        assert response.status_code == 405

        response = self.client.post(PATH)
        assert response.status_code == 302
        assert response.url == REDIRECT

    def test_planer_complete___302_redirect_redirect_to_next_tab(self):
        outline = self.get_outline(test_world=True)
        outline.off_troops = self.TEST_WORLD_DATA
        outline.save()
        self.create_target_on_test_world(outline=outline, off=5)

        FORM = reverse("base:planer_initial_form", args=[outline.pk])
        PATH = reverse("base:planer_complete", args=[outline.pk]) + f"?t=ruin"
        REDIRECT = (
            reverse("base:planer_initial", args=[outline.pk]) + "?page=1&mode=menu"
        )

        self.login_me()
        # to create 50 weight maxs
        response = self.client.get(FORM)

        response = self.client.get(PATH)
        assert response.status_code == 405

        response = self.client.post(PATH)
        assert response.status_code == 302
        assert response.url == REDIRECT
        outline.refresh_from_db()
        assert outline.written == "active"
        assert WeightModel.objects.all().count() == 5

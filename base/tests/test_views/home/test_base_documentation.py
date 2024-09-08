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

from base.tests.test_utils.mini_setup import MiniSetup


class BaseDocumentation(MiniSetup):
    def test_docs_404(self):
        response = self.client.get(reverse("base:documentation"))
        self.assertEqual(response.status_code, 404)

    def test_docs_redirect(self):
        response = self.client.get("/documentation/")
        self.assertEqual(response.status_code, 302)

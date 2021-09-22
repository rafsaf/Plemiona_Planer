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

from django.db import models


class Tribe(models.Model):
    """Tribe in game"""

    tribe_id = models.IntegerField()
    tag = models.TextField(db_index=True)
    world = models.ForeignKey("World", on_delete=models.CASCADE, db_index=True)

    def __str__(self):
        return self.tag

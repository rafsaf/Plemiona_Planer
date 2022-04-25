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

from base.models.player import Player
from base.models.world import World


class VillageModel(models.Model):
    """Village in the game"""

    village_id = models.IntegerField()
    x_coord = models.IntegerField()
    y_coord = models.IntegerField()
    coord = models.CharField(max_length=7, db_index=True)
    player = models.ForeignKey(Player, on_delete=models.CASCADE, null=True, blank=True)
    world = models.ForeignKey(World, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.coord

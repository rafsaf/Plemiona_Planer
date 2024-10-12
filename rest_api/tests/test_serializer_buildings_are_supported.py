# Copyright 2024 Rafał Safin (rafsaf). All Rights Reserved.
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

from base.models import Outline, WeightModel
from rest_api.serializers import BUILDINGS
from utils.basic.ruin import RuinHandle


def test_buildings_from_serializer_match_from_ruin_and_models():
    assert BUILDINGS == set(RuinHandle.BIG_LEVELS.keys())
    assert BUILDINGS == set(RuinHandle.SMALL_LEVELS.keys())
    assert BUILDINGS == set(building[0] for building in WeightModel.BUILDINGS)
    assert BUILDINGS == set(building[0] for building in Outline.BUILDINGS)

# Copyright 2013 Mirantis Corp.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.


from cinder import exception
from cinder import qos_levels
from cinder import test


class QosLevelsTest(test.TestCase):
    def test_qos_levels_with_wrong_required_qos(self):
        self.assertRaises(exception.InvalidRequiredQos,
                          qos_levels.check_valid_qos_level_for_volume,
                          'wrong_qos_lvl')

    def test_qos_levels_with_correct_required_qos(self):
        resuls = qos_levels.check_valid_qos_level_for_volume(qos_levels.BRONZE)
        self.assertEqual(None, resuls)

    def test_qos_levels_with_correct_required_qos(self):
        resuls = qos_levels.check_valid_qos_level_for_volume(qos_levels.GOLD)
        self.assertEqual(None, resuls)

    def test_qos_levels_with_correct_required_qos(self):
        resuls = \
            qos_levels.check_valid_qos_level_for_volume(qos_levels.PLATINUM)
        self.assertEqual(None, resuls)

    def test_qos_levels_for_get_gold_lvl_from_bronze(self):
        next_qos_lvl = qos_levels.get_next_qos_level(qos_levels.BRONZE)
        self.assertEqual(qos_levels.GOLD, next_qos_lvl)

    def test_qos_levels_for_get_platinum_lvl_from_gold(self):
        next_qos_lvl = qos_levels.get_next_qos_level(qos_levels.GOLD)
        self.assertEqual(qos_levels.PLATINUM, next_qos_lvl)

    def test_qos_levels_for_get_end_of_levels(self):
        next_qos_lvl = qos_levels.get_next_qos_level(qos_levels.PLATINUM)
        self.assertEqual(None, next_qos_lvl)

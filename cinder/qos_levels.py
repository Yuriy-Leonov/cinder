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


BRONZE = 'bronze'
GOLD = 'gold'
PLATINUM = 'platinum'
_qos_levels = (BRONZE, GOLD, PLATINUM, None)
_qos_levels_dict_fot_get_index = {BRONZE: 1, GOLD: 2, PLATINUM: 3, None: 4}
_qos_levels_dict_fot_get_level = {1: BRONZE, 2: GOLD, 3: PLATINUM, 4: None}


def check_valid_qos_level_for_volume(qos_level):
    if qos_level not in _qos_levels:
        reason = 'you use qos = {}, please change to some one of this: ' \
                 'bronze/gold/platinum'.format(qos_level)
        raise exception.InvalidRequiredQos(reason=reason)


def check_valid_qos_level_for_(qos_level, cls_exaption):
    if qos_level not in _qos_levels:
        raise cls_exaption(qos=qos_level)


def get_next_qos_level(qos_level):
    if not qos_level:
        return
    index = _qos_levels_dict_fot_get_index[qos_level]
    return _qos_levels_dict_fot_get_level[index + 1]

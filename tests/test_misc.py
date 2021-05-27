import copy
import datetime

import lil_toml


def test_deepcopy():
    obj = lil_toml.loads(
        """\
[bliibaa.diibaa]
offsettime=[1979-05-27T00:32:00.999999-07:00]
"""
    )
    obj_copy = copy.deepcopy(obj)
    assert obj_copy == obj
    expected_obj = {
        "bliibaa": {
            "diibaa": {
                "offsettime": [
                    datetime.datetime(
                        1979,
                        5,
                        27,
                        0,
                        32,
                        0,
                        999999,
                        tzinfo=datetime.timezone(datetime.timedelta(hours=-7)),
                    )
                ]
            }
        }
    }
    assert obj_copy == expected_obj

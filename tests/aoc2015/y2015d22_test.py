import pytest

import advent.aoc2015.day22 as d

EXAMPLE_INPUT_0 = """
Hit Points: 13
Damage: 8
""".strip()

EXAMPLE_INPUT_1 = """
Hit Points: 14
Damage: 8
""".strip()


@pytest.mark.parametrize("input, expected", [
    (EXAMPLE_INPUT_0, 226),
    (EXAMPLE_INPUT_1, 641),
])
def test_a(input, expected):
    assert d.parta(input, player_hp=10, player_mana=250) == expected


def test_b():
    assert d.partb(EXAMPLE_INPUT_0) is None

import pytest

import advent.aoc2018.day09 as d


@pytest.mark.parametrize("players, last_marble_value, expected", [
    (9, 25, 32),
    (10, 1618, 8317),
    (13, 7999, 146373),
    (17, 1104, 2764),
    (21, 6111, 54718),
    (30, 5807, 37305),
])
def test_run(players, last_marble_value, expected):
    assert d.run(players, last_marble_value) == expected

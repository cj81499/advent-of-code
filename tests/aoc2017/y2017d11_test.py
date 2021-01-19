import pytest

import advent.aoc2017.day11 as d


@pytest.mark.parametrize("input, expected", [
    ("ne,ne,ne", 3),
    ("ne,ne,sw,sw", 0),
    ("ne,ne,s,s", 2),
    ("se,sw,se,sw,sw", 3),
])
def test_a(input, expected):
    assert d.parta(input) == expected

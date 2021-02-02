import pytest

import advent.aoc2016.day01 as d


@pytest.mark.parametrize("input, expected", [
    ("R2, L3", 5),
    ("R2, R2, R2", 2),
    ("R5, L5, R5, R3", 12),
])
def test_a(input, expected):
    assert d.parta(input) == expected


@pytest.mark.parametrize("input, expected", [
    ("R8, R4, R4, R8", 4),
])
def test_b(input, expected):
    assert d.partb(input) == expected

import pytest

import aoc_cj.aoc2018.day11 as d


@pytest.mark.parametrize(
    "input,expected",
    [
        ("18", "33,45"),
        ("42", "21,61"),
    ],
)
def test_a(input, expected):
    assert d.parta(input) == expected


@pytest.mark.slow
@pytest.mark.parametrize(
    "input,expected",
    [
        ("18", "90,269,16"),
        ("42", "232,251,12"),
    ],
)
def test_b(input, expected):
    assert d.partb(input) == expected


@pytest.mark.parametrize(
    "input,expected",
    [
        ((3, 5, 8), 4),
        ((122, 79, 57), -5),
        ((217, 196, 39), 0),
        ((101, 153, 71), 4),
    ],
)
def test_power_level(input, expected):
    assert d.power_level(*input) == expected

import pytest

import aoc_cj.aoc2018.day14 as d


@pytest.mark.parametrize(
    "input, expected",
    [
        ("9", "5158916779"),
        ("5", "0124515891"),
        ("18", "9251071085"),
        ("2018", "5941429882"),
    ],
)
def test_a(input, expected):
    assert d.parta(input) == expected


@pytest.mark.parametrize(
    "input, expected",
    [
        ("51589", 9),
        ("01245", 5),
        ("92510", 18),
        ("59414", 2018),
    ],
)
def test_b(input, expected):
    assert d.partb(input) == expected

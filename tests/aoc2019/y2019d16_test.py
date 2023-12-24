import pytest
from more_itertools import pairwise

import aoc_cj.aoc2019.day16 as d

initial = 12345678


@pytest.mark.parametrize("before, after", pairwise(("12345678", "48226158", "34040438", "03415518", "01029498")))
def test_phase(before, after):
    assert d.phase(d.digits(before)) == d.digits(after)


@pytest.mark.parametrize(
    "input, expected",
    [
        ("80871224585914546619083218645595", "24176176"),
        ("19617804207202209144916044189917", "73745418"),
        ("69317163492948606335995924319873", "52432133"),
    ],
)
def test_part_1(input, expected):
    assert d.part_1(input) == expected


@pytest.mark.parametrize(
    "input, expected",
    [
        ("03036732577212944063491565474664", "84462026"),
        ("02935109699940807407585447034323", "78725270"),
        ("03081770884921959731165446850517", "53553731"),
    ],
)
def test_part_2(input, expected):
    assert d.part_2(input) == expected

import pytest

import aoc_cj.aoc2017.day11 as d


@pytest.mark.parametrize(
    "input, expected",
    [
        ("ne,ne,ne", 3),
        ("ne,ne,sw,sw", 0),
        ("ne,ne,s,s", 2),
        ("se,sw,se,sw,sw", 3),
    ],
)
def test_part_1(input, expected):
    assert d.part_1(input) == expected

import pytest

import aoc_cj.aoc2018.day01 as d


@pytest.mark.parametrize(
    "input, expected",
    [
        ("+1\n-2\n+3\n+1", 3),
        ("+1\n+1\n+1", 3),
        ("+1\n+1\n-2", 0),
        ("-1\n-2\n-3", -6),
    ],
)
def test_part_1(input, expected):
    assert d.part_1(input) == expected


@pytest.mark.parametrize(
    "input, expected",
    [
        ("+1\n-2\n+3\n+1", 2),
        ("+1\n-1", 0),
        ("+3\n+3\n+4\n-2\n-4", 10),
        ("-6\n+3\n+8\n+5\n-6", 5),
        ("+7\n+7\n-2\n-7\n-4", 14),
    ],
)
def test_part_2(input, expected):
    assert d.part_2(input) == expected

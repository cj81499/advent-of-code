import advent.aoc2018.day01 as d
import pytest


@pytest.mark.parametrize("input, expected", [
    ("+1\n-2\n+3\n+1", 3),
    ("+1\n+1\n+1", 3),
    ("+1\n+1\n-2", 0),
    ("-1\n-2\n-3", -6),
])
def test_a(input, expected):
    assert d.parta(input) == expected


@pytest.mark.parametrize("input, expected", [
    ("+1\n-2\n+3\n+1", 2),
    ("+1\n-1", 0),
    ("+3\n+3\n+4\n-2\n-4", 10),
    ("-6\n+3\n+8\n+5\n-6", 5),
    ("+7\n+7\n-2\n-7\n-4", 14),
])
def test_b(input, expected):
    assert d.partb(input) == expected

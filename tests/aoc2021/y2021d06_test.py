import aoc_cj.aoc2021.day06 as d

EXAMPLE_INPUT = "3,4,3,1,2"


def test_a():
    assert d.parta(EXAMPLE_INPUT) == 5934


def test_b():
    assert d.partb(EXAMPLE_INPUT) == 26984457539

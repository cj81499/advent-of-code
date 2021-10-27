import aoc_cj.aoc2016.day03 as d

EXAMPLE_INPUT = "5 10 25"


def test_is_valid_triangle():
    assert d.is_valid_triangle(EXAMPLE_INPUT.split()) is False


def test_a():
    assert d.parta(EXAMPLE_INPUT) == 0

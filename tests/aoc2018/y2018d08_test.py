import advent.aoc2018.day08 as d

EXAMPLE_INPUT = "2 3 0 3 10 11 12 1 1 0 1 99 2 1 1 2"


def test_a():
    assert d.parta(EXAMPLE_INPUT) == 138


def test_b():
    assert d.partb(EXAMPLE_INPUT) == 66

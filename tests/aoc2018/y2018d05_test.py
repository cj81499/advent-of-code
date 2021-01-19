import advent.aoc2018.day05 as d

EXAMPLE_INPUT = "dabAcCaCBAcCcaDA"


def test_a():
    assert d.parta(EXAMPLE_INPUT) == 10


def test_b():
    assert d.partb(EXAMPLE_INPUT) == 4

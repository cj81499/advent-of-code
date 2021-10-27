import aoc_cj.aoc2015.day24 as d

EXAMPLE_INPUT = "1 2 3 4 5 7 8 9 10 11".replace(" ", "\n")


def test_a():
    assert d.parta(EXAMPLE_INPUT) == 99


def test_b():
    assert d.partb(EXAMPLE_INPUT) == 44

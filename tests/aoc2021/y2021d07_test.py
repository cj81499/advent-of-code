import aoc_cj.aoc2021.day07 as d

EXAMPLE_INPUT = "16,1,2,0,4,2,7,1,2,14"


def test_a():
    assert d.parta(EXAMPLE_INPUT) == 37


def test_b():
    assert d.partb(EXAMPLE_INPUT) == 168

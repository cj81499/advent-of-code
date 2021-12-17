import aoc_cj.aoc2021.day17 as d

EXAMPLE_INPUT = "target area: x=20..30, y=-10..-5"


def test_a():
    assert d.parta(EXAMPLE_INPUT) == 45


def test_b():
    assert d.partb(EXAMPLE_INPUT) == 112

import aoc_cj.aoc2021.day02 as d

EXAMPLE_INPUT = """
forward 5
down 5
forward 8
up 3
down 8
forward 2
""".strip()


def test_a():
    assert d.parta(EXAMPLE_INPUT) == 150


def test_b():
    assert d.partb(EXAMPLE_INPUT) == 900

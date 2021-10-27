import aoc_cj.aoc2020.day12 as d

EXAMPLE_INPUT = """
F10
N3
F7
R90
F11
""".strip()


def test_a():
    assert d.parta(EXAMPLE_INPUT) == 25


def test_b():
    assert d.partb(EXAMPLE_INPUT) == 286

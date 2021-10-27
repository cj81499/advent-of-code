import aoc_cj.aoc2017.day13 as d

EXAMPLE_INPUT = """
0: 3
1: 2
4: 4
6: 4
""".strip()


def test_a():
    assert d.parta(EXAMPLE_INPUT) == 24


def test_b():
    assert d.partb(EXAMPLE_INPUT) == 10

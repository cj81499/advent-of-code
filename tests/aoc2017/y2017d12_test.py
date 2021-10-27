import aoc_cj.aoc2017.day12 as d

EXAMPLE_INPUT = """
0 <-> 2
1 <-> 1
2 <-> 0, 3, 4
3 <-> 2, 4
4 <-> 2, 3, 6
5 <-> 6
6 <-> 4, 5
""".strip()


def test_a():
    assert d.parta(EXAMPLE_INPUT) == 6


def test_b():
    assert d.partb(EXAMPLE_INPUT) == 2

import advent.aoc2017.day24 as d

EXAMPLE_INPUT = """
0/2
2/2
2/3
3/4
3/5
0/1
10/1
9/10
""".strip()


def test_a():
    assert d.parta(EXAMPLE_INPUT) == 31


def test_b():
    assert d.partb(EXAMPLE_INPUT) == 19

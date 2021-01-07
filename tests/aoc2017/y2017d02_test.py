import advent.aoc2017.day02 as d

EXAMPLE_INPUT_0 = """
5 1 9 5
7 5 3
2 4 6 8
""".strip()

EXAMPLE_INPUT_1 = """
5 9 2 8
9 4 7 3
3 8 6 5
""".strip()


def test_a():
    assert d.parta(EXAMPLE_INPUT_0) == 18


def test_b():
    assert d.partb(EXAMPLE_INPUT_1) == 9

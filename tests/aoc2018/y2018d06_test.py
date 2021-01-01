import advent.aoc2018.day06 as d

EXAMPLE_INPUT = """1, 1
1, 6
8, 3
3, 4
5, 5
8, 9
""".strip()


def test_a():
    assert d.parta(EXAMPLE_INPUT) == 17


def test_b():
    assert d.partb(EXAMPLE_INPUT, total_dist=32) == 16

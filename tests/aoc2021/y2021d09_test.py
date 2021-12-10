import aoc_cj.aoc2021.day09 as d

EXAMPLE_INPUT = """
2199943210
3987894921
9856789892
8767896789
9899965678
""".strip()


def test_a():
    assert d.parta(EXAMPLE_INPUT) == 15


def test_b():
    assert d.partb(EXAMPLE_INPUT) == 1134

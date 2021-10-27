import aoc_cj.aoc2016.day20 as d

EXAMPLE_INPUT = """
5-8
0-2
4-7
""".strip()


def test_a():
    assert d.parta(EXAMPLE_INPUT) == 3


def test_b():
    assert d.partb(EXAMPLE_INPUT, max_ip=10) == 2

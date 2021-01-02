import advent.aoc2015.day17 as d

EXAMPLE_INPUT = """
20
15
10
5
5
""".strip()


def test_a():
    assert d.parta(EXAMPLE_INPUT, liters=25) == 4


def test_b():
    assert d.partb(EXAMPLE_INPUT, liters=25) == 3

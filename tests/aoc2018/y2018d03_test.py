import advent.aoc2018.day03 as d

EXAMPLE_INPUT = """
#1 @ 1,3: 4x4
#2 @ 3,1: 4x4
#3 @ 5,5: 2x2
""".strip()


def test_a():
    assert d.parta(EXAMPLE_INPUT) == 4


def test_b():
    assert d.partb(EXAMPLE_INPUT) == 3

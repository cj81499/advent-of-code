import advent.aoc2016.day15 as d

EXAMPLE_INPUT = """
Disc #1 has 5 positions; at time=0, it is at position 4.
Disc #2 has 2 positions; at time=0, it is at position 1.
""".strip()


def test_a():
    assert d.parta(EXAMPLE_INPUT) == 5

import aoc_cj.aoc2016.day15 as d

EXAMPLE_INPUT = """
Disc #1 has 5 positions; at time=0, it is at position 4.
Disc #2 has 2 positions; at time=0, it is at position 1.
""".strip()


def test_part_1():
    assert d.part_1(EXAMPLE_INPUT) == 5

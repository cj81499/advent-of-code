import aoc_cj.aoc2015.day17 as d

EXAMPLE_INPUT = """
20
15
10
5
5
""".strip()


def test_part_1():
    assert d.part_1(EXAMPLE_INPUT, liters=25) == 4


def test_part_2():
    assert d.part_2(EXAMPLE_INPUT, liters=25) == 3

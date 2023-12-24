import aoc_cj.aoc2018.day03 as d

EXAMPLE_INPUT = """
#1 @ 1,3: 4x4
#2 @ 3,1: 4x4
#3 @ 5,5: 2x2
""".strip()


def test_part_1():
    assert d.part_1(EXAMPLE_INPUT) == 4


def test_part_2():
    assert d.part_2(EXAMPLE_INPUT) == 3

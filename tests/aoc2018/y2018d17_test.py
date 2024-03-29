import aoc_cj.aoc2018.day17 as d

EXAMPLE_INPUT = """
x=495, y=2..7
y=7, x=495..501
x=501, y=3..7
x=498, y=2..4
x=506, y=1..2
x=498, y=10..13
x=504, y=10..13
y=13, x=498..504
""".strip()


def test_part_1():
    assert d.part_1(EXAMPLE_INPUT) == 57


def test_part_2():
    assert d.part_2(EXAMPLE_INPUT) == 29

import aoc_cj.aoc2016.day20 as d

EXAMPLE_INPUT = """
5-8
0-2
4-7
""".strip()


def test_part_1():
    assert d.part_1(EXAMPLE_INPUT) == 3


def test_part_2():
    assert d.part_2(EXAMPLE_INPUT, max_ip=10) == 2

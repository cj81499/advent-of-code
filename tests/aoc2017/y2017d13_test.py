import aoc_cj.aoc2017.day13 as d

EXAMPLE_INPUT = """
0: 3
1: 2
4: 4
6: 4
""".strip()


def test_part_1() -> None:
    assert d.part_1(EXAMPLE_INPUT) == 24


def test_part_2() -> None:
    assert d.part_2(EXAMPLE_INPUT) == 10

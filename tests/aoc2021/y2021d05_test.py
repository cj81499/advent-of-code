import aoc_cj.aoc2021.day05 as d

EXAMPLE_INPUT = """
0,9 -> 5,9
8,0 -> 0,8
9,4 -> 3,4
2,2 -> 2,1
7,0 -> 7,4
6,4 -> 2,0
0,9 -> 2,9
3,4 -> 1,4
0,0 -> 8,8
5,5 -> 8,2
""".strip()


def test_part_1() -> None:
    assert d.part_1(EXAMPLE_INPUT) == 5


def test_part_2() -> None:
    assert d.part_2(EXAMPLE_INPUT) == 12

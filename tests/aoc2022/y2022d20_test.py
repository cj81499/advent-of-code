import aoc_cj.aoc2022.day20 as d

EXAMPLE_INPUT = """
1
2
-3
3
-2
0
4
""".strip()


def test_part_1() -> None:
    assert d.part_1(EXAMPLE_INPUT) == 3


def test_part_2() -> None:
    assert d.part_2(EXAMPLE_INPUT) == 1623178306

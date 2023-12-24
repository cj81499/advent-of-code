import aoc_cj.aoc2022.day04 as d

EXAMPLE_INPUT = """
2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8
""".strip()


def test_part_1() -> None:
    assert d.part_1(EXAMPLE_INPUT) == 2


def test_part_2() -> None:
    assert d.part_2(EXAMPLE_INPUT) == 4

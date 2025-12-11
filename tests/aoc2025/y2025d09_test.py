import aoc_cj.aoc2025.day09 as d

EXAMPLE_INPUT = """
7,1
11,1
11,7
9,7
9,5
2,5
2,3
7,3
""".strip("\n")


def test_part_1() -> None:
    assert d.part_1(EXAMPLE_INPUT) == 50


def test_part_2() -> None:
    assert d.part_2(EXAMPLE_INPUT) == 24

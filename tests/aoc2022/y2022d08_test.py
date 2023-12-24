import aoc_cj.aoc2022.day08 as d

EXAMPLE_INPUT = """
30373
25512
65332
33549
35390
""".strip()


def test_part_1() -> None:
    assert d.part_1(EXAMPLE_INPUT) == 21


def test_part_2() -> None:
    assert d.part_2(EXAMPLE_INPUT) == 8

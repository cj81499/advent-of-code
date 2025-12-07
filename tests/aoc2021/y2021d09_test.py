import aoc_cj.aoc2021.day09 as d

EXAMPLE_INPUT = """
2199943210
3987894921
9856789892
8767896789
9899965678
""".strip()


def test_part_1() -> None:
    assert d.part_1(EXAMPLE_INPUT) == 15


def test_part_2() -> None:
    assert d.part_2(EXAMPLE_INPUT) == 1134

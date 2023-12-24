import aoc_cj.aoc2023.day24 as d

EXAMPLE_INPUT = """
19, 13, 30 @ -2,  1, -2
18, 19, 22 @ -1, -1, -2
20, 25, 34 @ -2, -2, -4
12, 31, 28 @ -1, -2, -1
20, 19, 15 @  1, -5, -3
""".strip()


def test_part_1() -> None:
    assert d.part_1(EXAMPLE_INPUT, range_endpoints=(7, 27)) == 2


def test_part_2() -> None:
    assert d.part_2(EXAMPLE_INPUT) == 47

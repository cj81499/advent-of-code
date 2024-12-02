import aoc_cj.aoc2024.day02 as d

EXAMPLE_INPUT = """
7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9
""".strip()


def test_part_1() -> None:
    assert d.part_1(EXAMPLE_INPUT) == 2


def test_part_2() -> None:
    assert d.part_2(EXAMPLE_INPUT) == 4

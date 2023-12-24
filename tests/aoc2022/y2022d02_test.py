import aoc_cj.aoc2022.day02 as d

EXAMPLE_INPUT = """
A Y
B X
C Z
""".strip()


def test_part_1() -> None:
    assert d.part_1(EXAMPLE_INPUT) == 15


def test_part_2() -> None:
    assert d.part_2(EXAMPLE_INPUT) == 12

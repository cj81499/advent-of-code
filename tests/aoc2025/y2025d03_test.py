import aoc_cj.aoc2025.day03 as d

EXAMPLE_INPUT = """
987654321111111
811111111111119
234234234234278
818181911112111
""".strip()


def test_part_1() -> None:
    assert d.part_1(EXAMPLE_INPUT) == 357


def test_part_2() -> None:
    assert d.part_2(EXAMPLE_INPUT) == 3121910778619

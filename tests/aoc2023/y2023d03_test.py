import aoc_cj.aoc2023.day03 as d

EXAMPLE_INPUT = """
467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..
""".strip()


def test_part_1() -> None:
    assert d.part_1(EXAMPLE_INPUT) == 4361


def test_part_2() -> None:
    assert d.part_2(EXAMPLE_INPUT) == 467835

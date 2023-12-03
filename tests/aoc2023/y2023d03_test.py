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


def test_a() -> None:
    assert d.parta(EXAMPLE_INPUT) == 4361


def test_b() -> None:
    assert d.partb(EXAMPLE_INPUT) == 467835

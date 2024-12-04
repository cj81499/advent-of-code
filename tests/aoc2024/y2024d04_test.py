import aoc_cj.aoc2024.day04 as d

EXAMPLE_INPUT = """
MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX
""".strip()


def test_part_1() -> None:
    assert d.part_1(EXAMPLE_INPUT) == 18


def test_part_2() -> None:
    assert d.part_2(EXAMPLE_INPUT) == 9

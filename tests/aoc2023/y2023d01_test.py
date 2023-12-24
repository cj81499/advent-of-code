import aoc_cj.aoc2023.day01 as d

EXAMPLE_INPUT_1 = """
1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet
""".strip()


EXAMPLE_INPUT_2 = """
two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen
""".strip()


def test_part_1() -> None:
    assert d.part_1(EXAMPLE_INPUT_1) == 142


def test_part_2() -> None:
    assert d.part_2(EXAMPLE_INPUT_2) == 281

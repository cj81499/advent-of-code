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


def test_a() -> None:
    assert d.parta(EXAMPLE_INPUT_1) == 142


def test_b() -> None:
    assert d.partb(EXAMPLE_INPUT_2) == 281

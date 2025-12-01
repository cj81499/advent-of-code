import aoc_cj.aoc2025.day01 as d

EXAMPLE_INPUT = """
L68
L30
R48
L5
R60
L55
L1
L99
R14
L82
""".strip()


def test_part_1() -> None:
    assert d.part_1(EXAMPLE_INPUT) == 3


def test_part_2() -> None:
    assert d.part_2(EXAMPLE_INPUT) == 6

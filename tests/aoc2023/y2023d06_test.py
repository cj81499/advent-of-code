import aoc_cj.aoc2023.day06 as d

EXAMPLE_INPUT = """
Time:      7  15   30
Distance:  9  40  200
""".strip()


def test_part_1() -> None:
    assert d.part_1(EXAMPLE_INPUT) == 288


def test_part_2() -> None:
    assert d.part_2(EXAMPLE_INPUT) == 71503

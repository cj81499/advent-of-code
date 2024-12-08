import aoc_cj.aoc2016.day03 as d

EXAMPLE_INPUT = "5 10 25"


def test_is_valid_triangle() -> None:
    assert d.is_valid_triangle(map(int, EXAMPLE_INPUT.split())) is False


def test_part_1() -> None:
    assert d.part_1(EXAMPLE_INPUT) == 0

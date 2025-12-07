import aoc_cj.aoc2021.day17 as d

EXAMPLE_INPUT = "target area: x=20..30, y=-10..-5"


def test_part_1() -> None:
    assert d.part_1(EXAMPLE_INPUT) == 45


def test_part_2() -> None:
    assert d.part_2(EXAMPLE_INPUT) == 112

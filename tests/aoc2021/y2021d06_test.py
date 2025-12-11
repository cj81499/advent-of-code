import aoc_cj.aoc2021.day06 as d

EXAMPLE_INPUT = "3,4,3,1,2"


def test_part_1() -> None:
    assert d.part_1(EXAMPLE_INPUT) == 5934


def test_part_2() -> None:
    assert d.part_2(EXAMPLE_INPUT) == 26984457539

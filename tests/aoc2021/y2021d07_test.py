import aoc_cj.aoc2021.day07 as d

EXAMPLE_INPUT = "16,1,2,0,4,2,7,1,2,14"


def test_part_1() -> None:
    assert d.part_1(EXAMPLE_INPUT) == 37


def test_part_2() -> None:
    assert d.part_2(EXAMPLE_INPUT) == 168

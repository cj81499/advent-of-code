import aoc_cj.aoc2018.day05 as d

EXAMPLE_INPUT = "dabAcCaCBAcCcaDA"


def test_part_1() -> None:
    assert d.part_1(EXAMPLE_INPUT) == 10


def test_part_2() -> None:
    assert d.part_2(EXAMPLE_INPUT) == 4

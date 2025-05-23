import aoc_cj.aoc2015.day24 as d

EXAMPLE_INPUT = "1 2 3 4 5 7 8 9 10 11".replace(" ", "\n")


def test_part_1() -> None:
    assert d.part_1(EXAMPLE_INPUT) == 99


def test_part_2() -> None:
    assert d.part_2(EXAMPLE_INPUT) == 44

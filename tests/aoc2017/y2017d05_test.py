import aoc_cj.aoc2017.day05 as d

EXAMPLE_INPUT_0 = "0 3 0 1 -3".replace(" ", "\n")


def test_part_1() -> None:
    assert d.part_1(EXAMPLE_INPUT_0) == 5


def test_part_2() -> None:
    assert d.part_2(EXAMPLE_INPUT_0) == 10

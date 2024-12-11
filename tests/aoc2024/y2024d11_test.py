import aoc_cj.aoc2024.day11 as d

EXAMPLE_INPUT = "125 17"


def test_solve() -> None:
    assert d.solve(EXAMPLE_INPUT, blinks=6) == 22


def test_part_1() -> None:
    assert d.part_1(EXAMPLE_INPUT) == 55312

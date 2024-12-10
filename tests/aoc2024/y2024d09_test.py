import aoc_cj.aoc2024.day09 as d

EXAMPLE_INPUT = "2333133121414131402"


def test_part_1() -> None:
    assert d.part_1(EXAMPLE_INPUT) == 1928


def test_part_2() -> None:
    assert d.part_2(EXAMPLE_INPUT) == 2858

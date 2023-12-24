import aoc_cj.aoc2018.day08 as d

EXAMPLE_INPUT = "2 3 0 3 10 11 12 1 1 0 1 99 2 1 1 2"


def test_part_1():
    assert d.part_1(EXAMPLE_INPUT) == 138


def test_part_2():
    assert d.part_2(EXAMPLE_INPUT) == 66

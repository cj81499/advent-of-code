import aoc_cj.aoc2015.day02 as d


def test_part_1():
    assert d.part_1("2x3x4") == 58
    assert d.part_1("1x1x10") == 43


def test_part_2():
    assert d.part_2("2x3x4") == 34
    assert d.part_2("1x1x10") == 14

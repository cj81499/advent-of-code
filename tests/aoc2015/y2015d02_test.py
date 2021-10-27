import aoc_cj.aoc2015.day02 as d


def test_a():
    assert d.parta("2x3x4") == 58
    assert d.parta("1x1x10") == 43


def test_b():
    assert d.partb("2x3x4") == 34
    assert d.partb("1x1x10") == 14

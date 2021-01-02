import advent.aoc2015.day03 as d


def test_a():
    assert d.parta(">") == 2
    assert d.parta("^>v<") == 4
    assert d.parta("^v^v^v^v^v") == 2


def test_b():
    assert d.partb("^v") == 3
    assert d.partb("^>v<") == 3
    assert d.partb("^v^v^v^v^v") == 11

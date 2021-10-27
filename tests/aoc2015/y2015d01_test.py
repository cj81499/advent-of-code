import aoc_cj.aoc2015.day01 as d


def test_a():
    assert d.parta("(())") == 0
    assert d.parta("()()") == 0

    assert d.parta("(((") == 3
    assert d.parta("(()(()(") == 3
    assert d.parta("))(((((") == 3

    assert d.parta("())") == -1
    assert d.parta("))(") == -1

    assert d.parta(")))") == -3
    assert d.parta(")())())") == -3

    assert d.parta(")))") == -3
    assert d.parta(")())())") == -3


def test_b():
    assert d.partb(")") == 1
    assert d.partb("()())") == 5

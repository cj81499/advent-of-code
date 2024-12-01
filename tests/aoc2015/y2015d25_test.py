import aoc_cj.aoc2015.day25 as d


def test_next_code():
    assert d.next_code(d.FIRST_CODE) == 31916031


def test_code_at():
    assert d.code_at(1, 1) == d.FIRST_CODE
    assert d.code_at(1, 2) == 31916031
    assert d.code_at(1, 3) == 16080970
    assert d.code_at(1, 4) == 24592653

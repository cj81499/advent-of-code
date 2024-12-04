import aoc_cj.aoc2015.day03 as d


def test_part_1() -> None:
    assert d.part_1(">") == 2
    assert d.part_1("^>v<") == 4
    assert d.part_1("^v^v^v^v^v") == 2


def test_part_2() -> None:
    assert d.part_2("^v") == 3
    assert d.part_2("^>v<") == 3
    assert d.part_2("^v^v^v^v^v") == 11

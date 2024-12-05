import aoc_cj.aoc2015.day01 as d


def test_part_1() -> None:
    assert d.part_1("(())") == 0
    assert d.part_1("()()") == 0

    assert d.part_1("(((") == 3
    assert d.part_1("(()(()(") == 3
    assert d.part_1("))(((((") == 3

    assert d.part_1("())") == -1
    assert d.part_1("))(") == -1

    assert d.part_1(")))") == -3
    assert d.part_1(")())())") == -3

    assert d.part_1(")))") == -3
    assert d.part_1(")())())") == -3


def test_part_2() -> None:
    assert d.part_2(")") == 1
    assert d.part_2("()())") == 5

import aoc_cj.aoc2015.day05 as d


def test_part_1():
    assert d.is_nice1("ugknbfddgicrmopn") is True
    assert d.is_nice1("aaa") is True
    assert d.is_nice1("jchzalrnumimnmhp") is False
    assert d.is_nice1("haegwjzuvuyypxyu") is False
    assert d.is_nice1("dvszwmarrgswjxmb") is False


def test_part_2():
    assert d.is_nice2("qjhvhtzxzqqjkmpb") is True
    assert d.is_nice2("xxyxx") is True
    assert d.is_nice2("uurcxstgmygtbstg") is False
    assert d.is_nice2("ieodomkazucvgmuy") is False

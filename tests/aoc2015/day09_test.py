import advent.aoc2015.day09 as d


def test_a():
    lines = """London to Dublin = 464
London to Belfast = 518
Dublin to Belfast = 141""".splitlines()
    assert 605, d.find_paths(lines)[0]


def test_b():
    lines = """London to Dublin = 464
London to Belfast = 518
Dublin to Belfast = 141""".splitlines()
    assert 982, d.find_paths(lines)[1]

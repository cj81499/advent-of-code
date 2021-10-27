import aoc_cj.aoc2015.day09 as d

EXAMPLE_INPUT = """
London to Dublin = 464
London to Belfast = 518
Dublin to Belfast = 141
""".strip()


def test_a():
    assert d.parta(EXAMPLE_INPUT) == 605


def test_b():
    assert d.partb(EXAMPLE_INPUT) == 982

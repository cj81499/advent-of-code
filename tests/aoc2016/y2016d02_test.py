import aoc_cj.aoc2016.day02 as d

EXAMPLE_INPUT = """
ULL
RRDDD
LURDL
UUUUD
""".strip()


def test_a():
    assert d.parta(EXAMPLE_INPUT) == "1985"


def test_b():
    assert d.partb(EXAMPLE_INPUT) == "5DB3"

import aoc_cj.aoc2016.day02 as d

EXAMPLE_INPUT = """
ULL
RRDDD
LURDL
UUUUD
""".strip()


def test_part_1() -> None:
    assert d.part_1(EXAMPLE_INPUT) == "1985"


def test_part_2() -> None:
    assert d.part_2(EXAMPLE_INPUT) == "5DB3"

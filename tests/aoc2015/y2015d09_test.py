import aoc_cj.aoc2015.day09 as d

EXAMPLE_INPUT = """
London to Dublin = 464
London to Belfast = 518
Dublin to Belfast = 141
""".strip()


def test_part_1() -> None:
    assert d.part_1(EXAMPLE_INPUT) == 605


def test_part_2() -> None:
    assert d.part_2(EXAMPLE_INPUT) == 982

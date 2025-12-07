import aoc_cj.aoc2020.day12 as d

EXAMPLE_INPUT = """
F10
N3
F7
R90
F11
""".strip()


def test_part_1() -> None:
    assert d.part_1(EXAMPLE_INPUT) == 25


def test_part_2() -> None:
    assert d.part_2(EXAMPLE_INPUT) == 286

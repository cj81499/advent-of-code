import aoc_cj.aoc2022.day14 as d

EXAMPLE_INPUT = """
498,4 -> 498,6 -> 496,6
503,4 -> 502,4 -> 502,9 -> 494,9
""".strip()


def test_part_1() -> None:
    assert d.part_1(EXAMPLE_INPUT) == 24


def test_part_2() -> None:
    assert d.part_2(EXAMPLE_INPUT) == 93

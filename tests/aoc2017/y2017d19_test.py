import aoc_cj.aoc2017.day19 as d

EXAMPLE_INPUT = "    |         \n    |  +--+   \n    A  |  C   \nF---|----E|--+\n    |  |  |  D\n    +B-+  +--+"


def test_part_1() -> None:
    assert d.part_1(EXAMPLE_INPUT) == "ABCDEF"


def test_part_2() -> None:
    assert d.part_2(EXAMPLE_INPUT) == 38

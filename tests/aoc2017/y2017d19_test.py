import aoc_cj.aoc2017.day19 as d

EXAMPLE_INPUT = (
    "    |         \n" "    |  +--+   \n" "    A  |  C   \n" "F---|----E|--+\n" "    |  |  |  D\n" "    +B-+  +--+"
)


def test_part_1():
    assert d.part_1(EXAMPLE_INPUT) == "ABCDEF"


def test_part_2():
    assert d.part_2(EXAMPLE_INPUT) == 38

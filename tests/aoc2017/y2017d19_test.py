import aoc_cj.aoc2017.day19 as d

EXAMPLE_INPUT = (
    "    |         \n" "    |  +--+   \n" "    A  |  C   \n" "F---|----E|--+\n" "    |  |  |  D\n" "    +B-+  +--+"
)


def test_a():
    assert d.parta(EXAMPLE_INPUT) == "ABCDEF"


def test_b():
    assert d.partb(EXAMPLE_INPUT) == 38

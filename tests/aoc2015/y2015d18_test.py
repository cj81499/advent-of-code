import advent.aoc2015.day18 as d

EXAMPLE_INPUT = """
.#.#.#
...##.
#....#
..#...
#.#..#
####..
""".strip()


def test_a():
    assert d.parta(EXAMPLE_INPUT, steps=4) == 4


def test_b():
    assert d.partb(EXAMPLE_INPUT, steps=5) == 17

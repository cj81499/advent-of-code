import aoc_cj.aoc2015.day18 as d

EXAMPLE_INPUT = """
.#.#.#
...##.
#....#
..#...
#.#..#
####..
""".strip()


def test_part_1():
    assert d.part_1(EXAMPLE_INPUT, steps=4) == 4


def test_part_2():
    assert d.part_2(EXAMPLE_INPUT, steps=5) == 17

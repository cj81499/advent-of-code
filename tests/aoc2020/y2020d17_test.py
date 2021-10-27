import aoc_cj.aoc2020.day17 as d

EXAMPLE_INPUT = """
.#.
..#
###
""".strip()


def test_a():
    assert d.parta(EXAMPLE_INPUT) == 112


def test_b():
    assert d.partb(EXAMPLE_INPUT) == 848

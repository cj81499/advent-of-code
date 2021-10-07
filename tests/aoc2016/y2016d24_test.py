import advent.aoc2016.day24 as d

EXAMPLE_INPUT = """
###########
#0.1.....2#
#.#######.#
#4.......3#
###########
""".strip()


def test_a():
    assert d.parta(EXAMPLE_INPUT) == 14

import aoc_cj.aoc2016.day24 as d

EXAMPLE_INPUT = """
###########
#0.1.....2#
#.#######.#
#4.......3#
###########
""".strip()


def test_part_1() -> None:
    assert d.part_1(EXAMPLE_INPUT) == 14

import aoc_cj.aoc2018.day12 as d

EXAMPLE_INPUT = """
initial state: #..#.#..##......###...###

...## => #
..#.. => #
.#... => #
.#.#. => #
.#.## => #
.##.. => #
.#### => #
#.#.# => #
#.### => #
##.#. => #
##.## => #
###.. => #
###.# => #
####. => #
""".strip()


def test_part_1():
    assert d.part_1(EXAMPLE_INPUT) == 325

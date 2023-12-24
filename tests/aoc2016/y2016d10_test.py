import aoc_cj.aoc2016.day10 as d

EXAMPLE_INPUT = """
value 5 goes to bot 2
bot 2 gives low to bot 1 and high to bot 0
value 3 goes to bot 1
bot 1 gives low to output 1 and high to bot 0
bot 0 gives low to output 2 and high to output 0
value 2 goes to bot 2
""".strip()


def test_part_1():
    assert d.part_1(EXAMPLE_INPUT, compare=(5, 2)) == 2

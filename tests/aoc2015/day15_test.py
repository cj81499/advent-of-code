import advent.aoc2015.day15 as d

EXAMPLE_INPUT = """
Butterscotch: capacity -1, durability -2, flavor 6, texture 3, calories 8
Cinnamon: capacity 2, durability 3, flavor -2, texture -1, calories 3
""".strip()


def test_a():
    assert d.parta(EXAMPLE_INPUT) == 62842880


def test_b():
    assert d.partb(EXAMPLE_INPUT) == 57600000

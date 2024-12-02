import aoc_cj.aoc2015.day15 as d

EXAMPLE_INPUT = """
Butterscotch: capacity -1, durability -2, flavor 6, texture 3, calories 8
Cinnamon: capacity 2, durability 3, flavor -2, texture -1, calories 3
""".strip()


def test_part_1() -> None:
    assert d.part_1(EXAMPLE_INPUT) == 62842880


def test_part_2() -> None:
    assert d.part_2(EXAMPLE_INPUT) == 57600000

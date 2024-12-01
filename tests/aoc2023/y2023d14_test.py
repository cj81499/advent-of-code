import aoc_cj.aoc2023.day14 as d

EXAMPLE_INPUT = """
O....#....
O.OO#....#
.....##...
OO.#O....O
.O.....O#.
O.#..O.#.#
..O..#O..O
.......O..
#....###..
#OO..#....
""".strip()


def test_part_1() -> None:
    assert d.part_1(EXAMPLE_INPUT) == 136


def test_part_2() -> None:
    assert d.part_2(EXAMPLE_INPUT) == 64

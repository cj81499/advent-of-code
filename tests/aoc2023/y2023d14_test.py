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


def test_a() -> None:
    assert d.parta(EXAMPLE_INPUT) == 136


def test_b() -> None:
    assert d.partb(EXAMPLE_INPUT) == 64

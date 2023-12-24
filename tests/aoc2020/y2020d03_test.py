import aoc_cj.aoc2020.day03 as d

EXAMPLE_INPUT = """
..##.......
#...#...#..
.#....#..#.
..#.#...#.#
.#...##..#.
..#.##.....
.#.#.#....#
.#........#
#.##...#...
#...##....#
.#..#...#.#
""".strip()


def test_part_1():
    assert 7 == d.part_1(EXAMPLE_INPUT)


def test_part_2():
    assert 336 == d.part_2(EXAMPLE_INPUT)

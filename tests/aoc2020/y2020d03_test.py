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


def test_a():
    assert 7 == d.parta(EXAMPLE_INPUT)


def test_b():
    assert 336 == d.partb(EXAMPLE_INPUT)

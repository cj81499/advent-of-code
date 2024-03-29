import pytest

import aoc_cj.aoc2019.day10 as d

EXAMPLE_0 = """
.#..#
.....
#####
....#
...##
""".strip()


EXAMPLE_1 = """
......#.#.
#..#.#....
..#######.
.#.#.###..
.#..#.....
..#....#.#
#..#....#.
.##.#..###
##...#..#.
.#....####
""".strip()

EXAMPLE_2 = """
#.#...#.#.
.###....#.
.#....#...
##.#.#.#.#
....#.#.#.
.##..###.#
..#...##..
..##....##
......#...
.####.###.
""".strip()

EXAMPLE_3 = """
.#..#..###
####.###.#
....###.#.
..###.##.#
##.##.#.#.
....###..#
..#.#..#.#
#..#.#.###
.##...##.#
.....#.#..
""".strip()

EXAMPLE_4 = """
.#..##.###...#######
##.############..##.
.#.######.########.#
.###.#######.####.#.
#####.##.#.##.###.##
..#####..#.#########
####################
#.####....###.#.#.##
##.#################
#####.##.###..####..
..######..##.#######
####.##.####...##..#
.#####..#.######.###
##...#.##########...
#.##########.#######
.####.#.###.###.#.##
....##.##.###..#####
.#.#.###########.###
#.#.#.#####.####.###
###.##.####.##.#..##
""".strip()


@pytest.mark.parametrize(
    "input_val, expected",
    [
        (EXAMPLE_0, 8),
        (EXAMPLE_1, 33),
        (EXAMPLE_2, 35),
        (EXAMPLE_3, 41),
        (EXAMPLE_4, 210),
    ],
)
def test_part_1(input_val, expected: int) -> None:
    assert d.part_1(input_val) == expected


def test_get_asteroids() -> None:
    asteroids = d.get_asteroids(EXAMPLE_4.splitlines())
    # first row
    assert 0 + 0j not in asteroids
    assert 1 + 0j in asteroids
    assert 2 + 0j not in asteroids
    assert 3 + 0j not in asteroids
    assert 4 + 0j in asteroids
    assert 5 + 0j in asteroids
    assert 6 + 0j not in asteroids
    assert 7 + 0j in asteroids
    assert 8 + 0j in asteroids
    assert 9 + 0j in asteroids
    assert 10 + 0j not in asteroids
    assert 11 + 0j not in asteroids
    assert 12 + 0j not in asteroids
    assert 13 + 0j in asteroids
    assert 14 + 0j in asteroids
    assert 15 + 0j in asteroids
    assert 16 + 0j in asteroids
    assert 17 + 0j in asteroids
    assert 18 + 0j in asteroids
    assert 19 + 0j in asteroids
    # part_2 asteroids
    assert 11 + 12j in asteroids
    assert 12 + 1j in asteroids
    assert 12 + 2j in asteroids
    assert 12 + 8j in asteroids
    assert 16 + 0j in asteroids
    assert 16 + 9j in asteroids
    assert 10 + 16j in asteroids
    assert 9 + 6j in asteroids
    assert 8 + 2j in asteroids
    assert 10 + 9j in asteroids
    assert 11 + 1j in asteroids


def test_part_2() -> None:
    order = d.vaporize_order(EXAMPLE_4.splitlines())

    assert order[1 - 1] == 11 + 12j
    assert order[2 - 1] == 12 + 1j
    assert order[3 - 1] == 12 + 2j
    assert order[10 - 1] == 12 + 8j
    assert order[20 - 1] == 16 + 0j
    assert order[50 - 1] == 16 + 9j
    assert order[100 - 1] == 10 + 16j
    assert order[199 - 1] == 9 + 6j
    assert order[200 - 1] == 8 + 2j
    assert order[201 - 1] == 10 + 9j
    assert order[299 - 1] == 11 + 1j

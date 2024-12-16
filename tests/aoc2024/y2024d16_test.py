import pytest

import aoc_cj.aoc2024.day16 as d

EXAMPLE_INPUT = """
###############
#.......#....E#
#.#.###.#.###.#
#.....#.#...#.#
#.###.#####.#.#
#.#.#.......#.#
#.#.#####.###.#
#...........#.#
###.#.#####.#.#
#...#.....#.#.#
#.#.#.###.#.#.#
#.....#...#.#.#
#.###.#.#.#.#.#
#S..#.....#...#
###############
""".strip()

EXAMPLE_INPUT2 = """
#################
#...#...#...#..E#
#.#.#.#.#.#.#.#.#
#.#.#.#...#...#.#
#.#.#.#.###.#.#.#
#...#.#.#.....#.#
#.#.#.#.#.#####.#
#.#...#.#.#.....#
#.#.#####.#.###.#
#.#.#.......#...#
#.#.###.#####.###
#.#.#...#.....#.#
#.#.#.#####.###.#
#.#.#.........#.#
#.#.#.#########.#
#S#.............#
#################
""".strip()


@pytest.mark.parametrize(
    ("input", "expected"),
    (
        (EXAMPLE_INPUT, 7036),
        (EXAMPLE_INPUT2, 11048),
    ),
)
def test_part_1(input: str, expected: int) -> None:
    assert d.part_1(input) == expected


@pytest.mark.parametrize(
    ("input", "expected"),
    (
        (EXAMPLE_INPUT, 45),
        (EXAMPLE_INPUT2, 64),
    ),
)
def test_part_2(input: str, expected: int) -> None:
    assert d.part_2(input) == expected

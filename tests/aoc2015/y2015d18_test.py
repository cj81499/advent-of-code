import more_itertools as mi
import pytest

import aoc_cj.aoc2015.day18 as d

INITIAL_1 = """
.#.#.#
...##.
#....#
..#...
#.#..#
####..
""".strip()

AFTER_ONE_1 = """
..##..
..##.#
...##.
......
#.....
#.##..
""".strip()

AFTER_TWO_1 = """
..###.
......
..###.
......
.#....
.#....
""".strip()

AFTER_THREE_1 = """
...#..
......
...#..
..##..
......
......
""".strip()

AFTER_FOUR_1 = """
......
......
..##..
..##..
......
......
""".strip()


INITIAL_2 = """
##.#.#
...##.
#....#
..#...
#.#..#
####.#
""".strip()

AFTER_ONE_2 = """
#.##.#
####.#
...##.
......
#...#.
#.####
""".strip()

AFTER_TWO_2 = """
#..#.#
#....#
.#.##.
...##.
.#..##
##.###
""".strip()

AFTER_THREE_2 = """
#...##
####.#
..##.#
......
##....
####.#
""".strip()

AFTER_FOUR_2 = """
#.####
#....#
...#..
.##...
#.....
#.#..#
""".strip()

AFTER_FIVE_2 = """
##.###
.##..#
.##...
.##...
#.#...
##...#
""".strip()


@pytest.mark.parametrize(
    ("initial", "steps", "expected", "corners_stuck_on"),
    (
        # part 1
        (INITIAL_1, 1, AFTER_ONE_1, False),
        (INITIAL_1, 2, AFTER_TWO_1, False),
        (INITIAL_1, 3, AFTER_THREE_1, False),
        (INITIAL_1, 4, AFTER_FOUR_1, False),
        # part 2
        (INITIAL_2, 1, AFTER_ONE_2, True),
        (INITIAL_2, 2, AFTER_TWO_2, True),
        (INITIAL_2, 3, AFTER_THREE_2, True),
        (INITIAL_2, 4, AFTER_FOUR_2, True),
        (INITIAL_2, 5, AFTER_FIVE_2, True),
    ),
)
def test_simulation(initial: str, steps: int, expected: str, corners_stuck_on: bool) -> None:
    simulation = d.lightshow(initial, corners_stuck_on=corners_stuck_on)
    result = mi.nth(simulation, steps)
    assert result is not None, "simulation goes forever"
    assert ["".join(row) for row in result] == [line for line in expected.splitlines()]


def test_part_1() -> None:
    assert d.part_1(INITIAL_1, steps=4) == 4


def test_part_2() -> None:
    assert d.part_2(INITIAL_2, steps=5) == 17

import itertools

import pytest

import aoc_cj.aoc2019.day24 as d

INITIAL = """
....#
#..#.
#..##
..#..
#....
""".strip()

AFTER_1 = """
#..#.
####.
###.#
##.##
.##..
""".strip()

AFTER_2 = """
#####
....#
....#
...#.
#.###
""".strip()

AFTER_3 = """
#....
####.
...##
#.##.
.##.#
""".strip()

AFTER_4 = """
####.
....#
##..#
.....
##...
""".strip()

FIRST_REPEAT = """
.....
.....
.....
#....
.#...
""".strip()


def test_str_to_bugs() -> None:
    assert d.str_to_bugs(INITIAL) == frozenset(
        [
            (4, 0),
            (0, 1),
            (3, 1),
            (0, 2),
            (3, 2),
            (4, 2),
            (2, 3),
            (0, 4),
        ]
    )


@pytest.mark.parametrize(("before", "after"), itertools.pairwise((INITIAL, AFTER_1, AFTER_2, AFTER_3, AFTER_4)))
def test_step(before, after) -> None:
    before = d.str_to_bugs(before)
    after = d.str_to_bugs(after)
    assert d.step(before) == after


def test_first_repeat() -> None:
    assert d.first_repeat(d.str_to_bugs(INITIAL)) == d.str_to_bugs(FIRST_REPEAT)


def test_biodiversity() -> None:
    assert d.biodiversity(d.str_to_bugs(FIRST_REPEAT)) == 2129920


def test_part_1() -> None:
    assert d.part_1(INITIAL) == 2129920


def test_part_2() -> None:
    assert d.part_2(INITIAL, minutes=10) == 99

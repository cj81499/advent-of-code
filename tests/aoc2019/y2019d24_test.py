import itertools

import pytest

import advent.aoc2019.day24 as d

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


def pairwise(iterable):
    "s -> (s0,s1), (s1,s2), (s2, s3), ..."
    a, b = itertools.tee(iterable)
    next(b, None)
    return zip(a, b)


def test_str_to_bugs():
    assert d.str_to_bugs(INITIAL) == frozenset([
        (4, 0),
        (0, 1), (3, 1),
        (0, 2), (3, 2), (4, 2),
        (2, 3),
        (0, 4),
    ])


@pytest.mark.parametrize("before, after", pairwise([
    INITIAL, AFTER_1, AFTER_2, AFTER_3, AFTER_4
]))
def test_step(before, after):
    print(f"{before=}, {after=}")
    before = d.str_to_bugs(before)
    after = d.str_to_bugs(after)
    print(f"{before=}, {after=}")
    assert d.step(before) == after


def test_first_repeat():
    assert d.first_repeat(d.str_to_bugs(INITIAL)) == d.str_to_bugs(FIRST_REPEAT)


def test_biodiversity():
    assert d.biodiversity(d.str_to_bugs(FIRST_REPEAT)) == 2129920


def test_a():
    assert d.parta(INITIAL) == 2129920


def test_b():
    assert d.partb(INITIAL, minutes=10) == 99

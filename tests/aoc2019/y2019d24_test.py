import advent.aoc2019.day24 as d

INITIAL = """....#
#..#.
#..##
..#..
#...."""


AFTER_1_MINS = """#..#.
####.
###.#
##.##
.##.."""

AFTER_2_MINS = """#####
....#
....#
...#.
#.###"""

AFTER_3_MINS = """#....
####.
...##
#.##.
.##.#"""

AFTER_4_MINS = """####.
....#
##..#
.....
##..."""

FIRST_REPEAT = """.....
.....
.....
#....
.#..."""


def test_parse_bugs() -> None:
    bugs = d.parse_bugs(INITIAL.splitlines())

    assert 0 + 0j not in bugs
    assert 1 + 0j not in bugs
    assert 2 + 0j not in bugs
    assert 3 + 0j not in bugs
    assert 4 + 0j in bugs
    assert 0 + 1j in bugs
    assert 1 + 1j not in bugs
    assert 2 + 1j not in bugs
    assert 3 + 1j in bugs
    assert 4 + 1j not in bugs
    assert 0 + 2j in bugs
    assert 1 + 2j not in bugs
    assert 2 + 2j not in bugs
    assert 3 + 2j in bugs
    assert 4 + 2j in bugs
    assert 0 + 3j not in bugs
    assert 1 + 3j not in bugs
    assert 2 + 3j in bugs
    assert 3 + 3j not in bugs
    assert 4 + 3j not in bugs
    assert 0 + 4j in bugs
    assert 1 + 4j not in bugs
    assert 2 + 4j not in bugs
    assert 3 + 4j not in bugs
    assert 4 + 4j not in bugs


def test_step() -> None:
    initial = d.parse_bugs(INITIAL.splitlines())
    one = d.step(initial)
    assert one == d.parse_bugs(AFTER_1_MINS.splitlines())
    two = d.step(one)
    assert two == d.parse_bugs(AFTER_2_MINS.splitlines())
    three = d.step(two)
    assert three == d.parse_bugs(AFTER_3_MINS.splitlines())
    four = d.step(three)
    assert four == d.parse_bugs(AFTER_4_MINS.splitlines())


def test_find_first_repeat() -> None:
    bugs = d.parse_bugs(INITIAL.splitlines())
    repeat = d.find_first_repeat(bugs)
    assert repeat == d.parse_bugs(FIRST_REPEAT.splitlines())


def test_biodiversity() -> None:
    bugs = d.parse_bugs(FIRST_REPEAT.splitlines())
    assert d.biodiversity(bugs) == 2129920


def test_parta() -> None:
    assert d.parta(INITIAL) == 2129920


# def test_partb() -> None:
#     assert d.partb([]) == 0

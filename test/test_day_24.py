import src.day_24 as d

INITIAL = """....#
#..#.
#..##
..#..
#....""".splitlines()


AFTER_1_MINS = """#..#.
####.
###.#
##.##
.##..""".splitlines()

AFTER_2_MINS = """#####
....#
....#
...#.
#.###""".splitlines()

AFTER_3_MINS = """#....
####.
...##
#.##.
.##.#""".splitlines()

AFTER_4_MINS = """####.
....#
##..#
.....
##...""".splitlines()

FIRST_REPEAT = """.....
.....
.....
#....
.#...""".splitlines()


def test_parse_bugs():
    bugs = d.parse_bugs(INITIAL)

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


def test_step():
    initial = d.parse_bugs(INITIAL)
    one = d.step(initial)
    assert one == d.parse_bugs(AFTER_1_MINS)
    two = d.step(one)
    assert two == d.parse_bugs(AFTER_2_MINS)
    three = d.step(two)
    assert three == d.parse_bugs(AFTER_3_MINS)
    four = d.step(three)
    assert four == d.parse_bugs(AFTER_4_MINS)


def test_find_first_repeat():
    bugs = d.parse_bugs(INITIAL)
    repeat = d.find_first_repeat(bugs)
    assert repeat == d.parse_bugs(FIRST_REPEAT)


def test_biodiversity():
    bugs = d.parse_bugs(FIRST_REPEAT)
    assert d.biodiversity(bugs) == 2129920


def test_part1():
    assert d.part1(INITIAL) == 2129920


# def test_part2():
#     assert d.part2([]) == 0

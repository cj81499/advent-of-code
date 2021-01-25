import pytest

import advent.aoc2019.day18 as d

EXAMPLE_INPUT_0 = """
#########
#b.A.@.a#
#########
""".strip()

EXAMPLE_INPUT_1 = """
########################
#f.D.E.e.C.b.A.@.a.B.c.#
######################.#
#d.....................#
########################
""".strip()

EXAMPLE_INPUT_2 = """
########################
#...............b.C.D.f#
#.######################
#.....@.a.B.c.d.A.e.F.g#
########################
""".strip()

EXAMPLE_INPUT_3 = """
#################
#i.G..c...e..H.p#
########.########
#j.A..b...f..D.o#
########@########
#k.E..a...g..B.n#
########.########
#l.F..d...h..C.m#
#################
""".strip()

EXAMPLE_INPUT_4 = """
########################
#@..............ac.GI.b#
###d#e#f################
###A#B#C################
###g#h#i################
########################
""".strip()

EXAMPLE_INPUT_5 = """
#######
#a.#Cd#
##...##
##.@.##
##...##
#cB#Ab#
#######
""".strip()

EXAMPLE_INPUT_6 = """
###############
#d.ABC.#.....a#
######@#@######
###############
######@#@######
#b.....#.....c#
###############
""".strip()

EXAMPLE_INPUT_7 = """
#############
#DcBa.#.GhKl#
#.###@#@#I###
#e#d#####j#k#
###C#@#@###J#
#fEbA.#.FgHi#
#############
""".strip()

EXAMPLE_INPUT_8 = """
#############
#g#f.D#..h#l#
#F###e#E###.#
#dCba@#@BcIJ#
#############
#nK.L@#@G...#
#M###N#H###.#
#o#m..#i#jk.#
#############
""".strip()


@pytest.mark.parametrize("input, expected", [
    (EXAMPLE_INPUT_0, 8),
    (EXAMPLE_INPUT_1, 86),
    (EXAMPLE_INPUT_2, 132),
    (EXAMPLE_INPUT_3, 136),
    (EXAMPLE_INPUT_4, 81),
])
def test_a(input, expected):
    assert d.parta(input) == expected


@pytest.mark.parametrize("input, expected", [
    (EXAMPLE_INPUT_5, 8),
    (EXAMPLE_INPUT_6, 24),
    (EXAMPLE_INPUT_7, 32),
    (EXAMPLE_INPUT_8, 72),
])
def test_b(input, expected):
    assert d.partb(input) == expected

import pytest

import aoc_cj.aoc2019.day18 as d

EXAMPLE_INPUT_A0 = """
#########
#b.A.@.a#
#########
""".strip()

EXAMPLE_INPUT_A1 = """
########################
#f.D.E.e.C.b.A.@.a.B.c.#
######################.#
#d.....................#
########################
""".strip()

EXAMPLE_INPUT_A2 = """
########################
#...............b.C.D.f#
#.######################
#.....@.a.B.c.d.A.e.F.g#
########################
""".strip()

EXAMPLE_INPUT_A3 = """
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

EXAMPLE_INPUT_A4 = """
########################
#@..............ac.GI.b#
###d#e#f################
###A#B#C################
###g#h#i################
########################
""".strip()

EXAMPLE_INPUT_B1 = """
#######
#a.#Cd#
##...##
##.@.##
##...##
#cB#Ab#
#######
""".strip()

EXAMPLE_INPUT_B2 = """
###############
#d.ABC.#.....a#
######...######
######.@.######
######...######
#b.....#.....c#
###############
""".strip()

EXAMPLE_INPUT_B3 = """
#############
#DcBa.#.GhKl#
#.###...#I###
#e#d#.@.#j#k#
###C#...###J#
#fEbA.#.FgHi#
#############
""".strip()

EXAMPLE_INPUT_B4 = """
#############
#g#f.D#..h#l#
#F###e#E###.#
#dCba...BcIJ#
#####.@.#####
#nK.L...G...#
#M###N#H###.#
#o#m..#i#jk.#
#############
""".strip()


@pytest.mark.parametrize(
    "input, expected",
    [
        (EXAMPLE_INPUT_A0, 8),
        (EXAMPLE_INPUT_A1, 86),
        (EXAMPLE_INPUT_A2, 132),
        (EXAMPLE_INPUT_A3, 136),
        (EXAMPLE_INPUT_A4, 81),
    ],
)
def test_part_1(input, expected):
    assert d.part_1(input) == expected


@pytest.mark.parametrize(
    "input, expected",
    [
        (EXAMPLE_INPUT_B1, 8),
        (EXAMPLE_INPUT_B2, 24),
        (EXAMPLE_INPUT_B3, 32),
        (EXAMPLE_INPUT_B4, 72),
    ],
)
def test_part_2(input, expected):
    assert d.part_2(input) == expected

import aoc_cj.aoc2021.day23 as d

EXAMPLE_INPUT = """
#############
#...........#
###B#C#B#D###
  #A#D#C#A#
  #########
""".strip()


def test_a():
    assert d.parta(EXAMPLE_INPUT) == 12521


def test_b():
    assert d.partb(EXAMPLE_INPUT) is None

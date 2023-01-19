import pytest

import aoc_cj.aoc2021.day23 as d

EXAMPLE_INPUT = """
#############
#...........#
###B#C#B#D###
  #A#D#C#A#
  #########
""".strip(
    "\n"
)


@pytest.mark.parametrize(
    ("burrow", "expected"),
    (
        (d.GOAL_STATE_STR, 0),
        (EXAMPLE_INPUT, 12521),
    ),
)
def test_a(burrow: str, expected: int):
    assert d.parta(burrow) == expected


@pytest.mark.parametrize(
    ("burrow", "expected"),
    ((EXAMPLE_INPUT, 44169),),
)
def test_b(burrow: str, expected: int):
    assert d.partb(burrow) == expected

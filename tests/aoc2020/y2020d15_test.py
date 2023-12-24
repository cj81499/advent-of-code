import pytest

import aoc_cj.aoc2020.day15 as d

EXAMPLE_INPUT_0 = "0,3,6"
EXAMPLE_INPUT_1 = "1,3,2"
EXAMPLE_INPUT_2 = "2,1,3"
EXAMPLE_INPUT_3 = "1,2,3"
EXAMPLE_INPUT_4 = "2,3,1"
EXAMPLE_INPUT_5 = "3,2,1"
EXAMPLE_INPUT_6 = "3,1,2"


@pytest.mark.parametrize(
    "input, expected",
    [
        (EXAMPLE_INPUT_0, 436),
        (EXAMPLE_INPUT_1, 1),
        (EXAMPLE_INPUT_2, 10),
        (EXAMPLE_INPUT_3, 27),
        (EXAMPLE_INPUT_4, 78),
        (EXAMPLE_INPUT_5, 438),
        (EXAMPLE_INPUT_6, 1836),
    ],
)
def test_part_1(input, expected):
    assert d.part_1(input) == expected


@pytest.mark.slow
@pytest.mark.parametrize(
    "input, expected",
    [
        (EXAMPLE_INPUT_0, 175594),
        (EXAMPLE_INPUT_1, 2578),
        (EXAMPLE_INPUT_2, 3544142),
        (EXAMPLE_INPUT_3, 261214),
        (EXAMPLE_INPUT_4, 6895259),
        (EXAMPLE_INPUT_5, 18),
        (EXAMPLE_INPUT_6, 362),
    ],
)
def test_part_2(input, expected):
    assert d.part_2(input) == expected

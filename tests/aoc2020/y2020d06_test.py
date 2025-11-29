import pytest

import aoc_cj.aoc2020.day06 as d

EXAMPLE_INPUT = """
abc

a
b
c

ab
ac

a
a
a
a

b
""".strip()

GROUPS = d.get_group_of_people(EXAMPLE_INPUT)


@pytest.mark.parametrize(
    "input, expected",
    [
        (GROUPS[0], 3),
        (GROUPS[1], 3),
        (GROUPS[2], 3),
        (GROUPS[3], 1),
        (GROUPS[4], 1),
    ],
)
def test_part_1_helper(input, expected):
    assert expected == d.part_1_helper(input)


def test_part_1():
    assert 11 == d.part_1(EXAMPLE_INPUT)


@pytest.mark.parametrize(
    "input, expected",
    [
        (GROUPS[0], 3),
        (GROUPS[1], 0),
        (GROUPS[2], 1),
        (GROUPS[3], 1),
        (GROUPS[4], 1),
    ],
)
def test_part_2_helper(input, expected):
    assert expected == d.part_2_helper(input)


def test_part_2():
    assert 6 == d.part_2(EXAMPLE_INPUT)

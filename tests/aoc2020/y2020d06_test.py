import advent.aoc2020.day06 as d
import pytest

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


@pytest.mark.parametrize("input, expected", [
    (GROUPS[0], 3),
    (GROUPS[1], 3),
    (GROUPS[2], 3),
    (GROUPS[3], 1),
    (GROUPS[4], 1),
])
def test_a_helper(input, expected):
    assert expected == d.parta_helper(input)


def test_a():
    assert 11 == d.parta(EXAMPLE_INPUT)


@pytest.mark.parametrize("input, expected", [
    (GROUPS[0], 3),
    (GROUPS[1], 0),
    (GROUPS[2], 1),
    (GROUPS[3], 1),
    (GROUPS[4], 1),
])
def test_b_helper(input, expected):
    assert expected == d.partb_helper(input)


def test_b():
    assert 6 == d.partb(EXAMPLE_INPUT)

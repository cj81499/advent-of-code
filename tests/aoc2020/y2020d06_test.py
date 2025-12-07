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
    ("example", "expected"),
    [
        (GROUPS[0], 3),
        (GROUPS[1], 3),
        (GROUPS[2], 3),
        (GROUPS[3], 1),
        (GROUPS[4], 1),
    ],
)
def test_part_1_helper(example: str, expected) -> None:
    assert expected == d.part_1_helper(example)


def test_part_1() -> None:
    assert d.part_1(EXAMPLE_INPUT) == 11


@pytest.mark.parametrize(
    ("example", "expected"),
    [
        (GROUPS[0], 3),
        (GROUPS[1], 0),
        (GROUPS[2], 1),
        (GROUPS[3], 1),
        (GROUPS[4], 1),
    ],
)
def test_part_2_helper(example: str, expected) -> None:
    assert expected == d.part_2_helper(example)


def test_part_2() -> None:
    assert d.part_2(EXAMPLE_INPUT) == 6

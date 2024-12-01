import pytest

import aoc_cj.aoc2016.day18 as d

EXAMPLE_INPUT_1 = "..^^."
EXAMPLE_INPUT_2 = ".^^.^.^^^^"

EXAMPLE_MAP_1 = """
..^^.
.^^^^
^^..^
""".strip()


EXAMPLE_MAP_2 = """
.^^.^.^^^^
^^^...^..^
^.^^.^.^^.
..^^...^^^
.^^^^.^^.^
^^..^.^^..
^^^^..^^^.
^..^^^^.^^
.^^^..^.^^
^^.^^^..^^
""".strip()


@pytest.mark.parametrize(
    "first_row, expected",
    (
        (EXAMPLE_INPUT_1, EXAMPLE_MAP_1),
        (EXAMPLE_INPUT_2, EXAMPLE_MAP_2),
    ),
)
def test_next_row(first_row, expected):
    prev = first_row
    for row in expected.splitlines():
        assert row == prev
        prev = d.next_row(row)


def test_part_1():
    assert d.part_1(EXAMPLE_INPUT_2, num_rows=10) == 38

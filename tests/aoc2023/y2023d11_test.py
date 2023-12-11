import pytest

import aoc_cj.aoc2023.day11 as d

EXAMPLE_INPUT = """
...#......
.......#..
#.........
..........
......#...
.#........
.........#
..........
.......#..
#...#.....
""".strip()


def test_a() -> None:
    assert d.parta(EXAMPLE_INPUT) == 374


@pytest.mark.parametrize(
    ("expand_by", "expected"),
    (
        (10, 1030),
        (100, 8410),
    ),
)
def test_b(expand_by: int, expected: int) -> None:
    assert d.partb(EXAMPLE_INPUT, expand_by=expand_by) == expected

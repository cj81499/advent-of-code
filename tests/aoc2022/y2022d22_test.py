import pytest

import aoc_cj.aoc2022.day22 as d

EXAMPLE_INPUT = """
        ...#
        .#..
        #...
        ....
...#.......#
........#...
..#....#....
..........#.
        ...#....
        .....#..
        .#......
        ......#.

10R5L5R10L4R5L5
""".strip(
    "\n"
)


def test_a() -> None:
    assert d.parta(EXAMPLE_INPUT) == 6032


@pytest.mark.skip("unsolved")
def test_b() -> None:
    assert d.partb(EXAMPLE_INPUT) == 5031

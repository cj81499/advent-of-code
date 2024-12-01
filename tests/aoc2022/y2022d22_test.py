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
""".strip("\n")


def test_part_1() -> None:
    assert d.part_1(EXAMPLE_INPUT) == 6032


@pytest.mark.skip("unsolved")
def test_part_2() -> None:
    assert d.part_2(EXAMPLE_INPUT) == 5031

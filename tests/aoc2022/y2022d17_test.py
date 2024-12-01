import pytest

import aoc_cj.aoc2022.day17 as d

EXAMPLE_INPUT = ">>><<><>><<<>><>>><<<>>><<<><<<>><>><<>>"


def test_part_1() -> None:
    assert d.part_1(EXAMPLE_INPUT) == 3068


@pytest.mark.skip("unsolved")
def test_part_2() -> None:
    assert d.part_2(EXAMPLE_INPUT) == 1514285714288  # type: ignore[func-returns-value]

import pytest

import aoc_cj.aoc2022.day17 as d

EXAMPLE_INPUT = ">>><<><>><<<>><>>><<<>>><<<><<<>><>><<>>"


def test_a() -> None:
    assert d.parta(EXAMPLE_INPUT) == 3068


@pytest.mark.skip("unsolved")
def test_b() -> None:
    assert d.partb(EXAMPLE_INPUT) == 1514285714288

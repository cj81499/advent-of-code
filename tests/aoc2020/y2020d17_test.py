import pytest
import advent.aoc2020.day17 as d

EXAMPLE_INPUT = """
.#.
..#
###
""".strip()


def test_a():
    assert d.parta(EXAMPLE_INPUT) == 112


@pytest.mark.slow
def test_b():
    assert d.partb(EXAMPLE_INPUT) == 848

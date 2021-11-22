import pytest

import aoc_cj.aoc2017.day15 as d

EXAMPLE_INPUT = """
Generator A starts with 65
Generator B starts with 8921
""".strip()


@pytest.mark.parametrize(
    "num_loops, expected",
    [
        (2, 0),
        (3, 1),
        (5, 1),
    ],
)
def test_a(num_loops, expected):
    assert d.parta(EXAMPLE_INPUT, num_loops) == expected


@pytest.mark.slow
def test_a_slow():
    assert d.parta(EXAMPLE_INPUT) == 588


@pytest.mark.parametrize(
    "num_loops, expected",
    [
        (5, 0),
        (1055, 0),
        (1056, 1),
    ],
)
def test_b(num_loops, expected):
    assert d.partb(EXAMPLE_INPUT, num_loops) == expected


@pytest.mark.slow
def test_b_slow():
    assert d.partb(EXAMPLE_INPUT) == 309

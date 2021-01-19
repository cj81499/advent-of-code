import pytest

import advent.aoc2017.day22 as d

EXAMPLE_INPUT = """
..#
#..
...
""".strip()


def test_a():
    assert d.parta(EXAMPLE_INPUT, burst_count=70) == 41


def test_b():
    assert d.partb(EXAMPLE_INPUT, burst_count=100) == 26


@pytest.mark.slow
def test_b_slow():
    assert d.partb(EXAMPLE_INPUT) == 2511944

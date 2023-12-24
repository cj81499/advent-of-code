import pytest

import aoc_cj.aoc2017.day22 as d

EXAMPLE_INPUT = """
..#
#..
...
""".strip()


def test_part_1():
    assert d.part_1(EXAMPLE_INPUT, burst_count=70) == 41


def test_part_2():
    assert d.part_2(EXAMPLE_INPUT, burst_count=100) == 26


@pytest.mark.slow
def test_b_slow():
    assert d.part_2(EXAMPLE_INPUT) == 2511944

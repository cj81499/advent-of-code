import pytest

import aoc_cj.aoc2020.day23 as d

EXAMPLE_INPUT = "389125467"


def test_a():
    assert d.parta(EXAMPLE_INPUT) == 67384529


@pytest.mark.slow
def test_b():
    assert d.partb(EXAMPLE_INPUT) == 149245887792

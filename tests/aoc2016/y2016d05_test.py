import pytest

import advent.aoc2016.day05 as d

EXAMPLE_INPUT = "abc"


@pytest.mark.slow
def test_a():
    assert d.parta(EXAMPLE_INPUT) == "18f47a30"


@pytest.mark.slow
def test_b():
    assert d.partb(EXAMPLE_INPUT) == "05ace8e3"

import pytest

import aoc_cj.aoc2016.day05 as d

EXAMPLE_INPUT = "abc"


@pytest.mark.slow
def test_part_1() -> None:
    assert d.part_1(EXAMPLE_INPUT) == "18f47a30"


@pytest.mark.slow
def test_part_2() -> None:
    assert d.part_2(EXAMPLE_INPUT) == "05ace8e3"

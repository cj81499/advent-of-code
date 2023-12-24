import pytest

import aoc_cj.aoc2020.day23 as d

EXAMPLE_INPUT = "389125467"


def test_part_1():
    assert d.part_1(EXAMPLE_INPUT) == 67384529


@pytest.mark.slow
def test_part_2():
    assert d.part_2(EXAMPLE_INPUT) == 149245887792

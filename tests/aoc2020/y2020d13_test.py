import pytest

import aoc_cj.aoc2020.day13 as d

EXAMPLE_INPUT = """
939
7,13,x,x,59,x,31,19
""".strip()


def test_a():
    assert d.parta(EXAMPLE_INPUT) == 295


@pytest.mark.parametrize(
    "input, expected",
    [
        ("0\n17,x,13,19", 3417),
        ("0\n67,7,59,61", 754018),
        ("0\n67,x,7,59,61", 779210),
        ("0\n67,7,x,59,61", 1261476),
        ("0\n1789,37,47,1889", 1202161486),
        (EXAMPLE_INPUT, 1068781),
    ],
)
def test_b(input, expected):
    assert d.partb(input) == expected

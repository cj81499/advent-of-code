import pytest

import aoc_cj.aoc2023.day24 as d

EXAMPLE_INPUT = """
19, 13, 30 @ -2,  1, -2
18, 19, 22 @ -1, -1, -2
20, 25, 34 @ -2, -2, -4
12, 31, 28 @ -1, -2, -1
20, 19, 15 @  1, -5, -3
""".strip()


def test_a() -> None:
    assert d.parta(EXAMPLE_INPUT, range_endpoints=(7, 27)) == 2


@pytest.mark.skip("not implemented")
def test_b() -> None:
    assert d.partb(EXAMPLE_INPUT) == 47

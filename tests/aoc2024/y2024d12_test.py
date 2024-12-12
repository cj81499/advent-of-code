import pytest

import aoc_cj.aoc2024.day12 as d

EXAMPLE_INPUT = """
AAAA
BBCD
BBCC
EEEC
""".strip()

EXAMPLE_INPUT2 = """
OOOOO
OXOXO
OOOOO
OXOXO
OOOOO
""".strip()

EXAMPLE_INPUT3 = """
RRRRIICCFF
RRRRIICCCF
VVRRRCCFFF
VVRCCCJFFF
VVVVCJJCFE
VVIVCCJJEE
VVIIICJJEE
MIIIIIJJEE
MIIISIJEEE
MMMISSJEEE
""".strip()

EXAMPLE_INPUT4 = """
EEEEE
EXXXX
EEEEE
EXXXX
EEEEE
""".strip()

EXAMPLE_INPUT5 = """
AAAAAA
AAABBA
AAABBA
ABBAAA
ABBAAA
AAAAAA
""".strip()


@pytest.mark.parametrize(
    ("input", "expected"),
    (
        (EXAMPLE_INPUT, 140),
        (EXAMPLE_INPUT2, 772),
        (EXAMPLE_INPUT3, 1930),
    ),
)
def test_part_1(input: str, expected: int) -> None:
    assert d.part_1(input) == expected


@pytest.mark.parametrize(
    ("input", "expected"),
    (
        (EXAMPLE_INPUT, 80),
        (EXAMPLE_INPUT2, 436),
        (EXAMPLE_INPUT3, 1206),
        (EXAMPLE_INPUT4, 236),
        (EXAMPLE_INPUT5, 368),
    ),
)
def test_part_2(input: str, expected: int) -> None:
    assert d.part_2(input) == expected

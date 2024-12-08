import pytest

import aoc_cj.aoc2016.day01 as d


@pytest.mark.parametrize(
    "input, expected",
    [
        ("R2, L3", 5),
        ("R2, R2, R2", 2),
        ("R5, L5, R5, R3", 12),
    ],
)
def test_part_1(input: str, expected: int) -> None:
    assert d.part_1(input) == expected


@pytest.mark.parametrize(
    "input, expected",
    [
        ("R8, R4, R4, R8", 4),
    ],
)
def test_part_2(input: str, expected: int) -> None:
    assert d.part_2(input) == expected

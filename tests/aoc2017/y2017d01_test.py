import pytest

import aoc_cj.aoc2017.day01 as d


@pytest.mark.parametrize(
    ("example", "expected"),
    [
        ("1122", 3),
        ("1111", 4),
        ("1234", 0),
        ("91212129", 9),
    ],
)
def test_part_1(example: str, expected) -> None:
    assert d.part_1(example) == expected


@pytest.mark.parametrize(
    ("example", "expected"),
    [
        ("1212", 6),
        ("1221", 0),
        ("123425", 4),
        ("123123", 12),
        ("12131415", 4),
    ],
)
def test_part_2(example: str, expected) -> None:
    assert d.part_2(example) == expected

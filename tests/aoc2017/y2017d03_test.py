import pytest

import aoc_cj.aoc2017.day03 as d


@pytest.mark.parametrize(
    ("example", "expected"),
    [
        ("1", 0),
        ("12", 3),
        ("23", 2),
        ("1024", 31),
    ],
)
def test_part_1(example: str, expected) -> None:
    assert d.part_1(example) == expected


@pytest.mark.parametrize(
    ("example", "expected"),
    [
        ("-1000", 1),
        ("-1", 1),
        ("0", 1),
        ("1", 2),
        ("2", 4),
        ("4", 5),
        ("5", 10),
        ("10", 11),
        ("11", 23),
        ("362", 747),
        ("747", 806),
    ],
)
def test_part_2(example: str, expected) -> None:
    assert d.part_2(example) == expected

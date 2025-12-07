import pytest

import aoc_cj.aoc2018.day11 as d


@pytest.mark.parametrize(
    ("example", "expected"),
    [
        ("18", "33,45"),
        ("42", "21,61"),
    ],
)
def test_part_1(example: str, expected) -> None:
    assert d.part_1(example) == expected


@pytest.mark.slow
@pytest.mark.parametrize(
    ("example", "expected"),
    [
        ("18", "90,269,16"),
        ("42", "232,251,12"),
    ],
)
def test_part_2(example: str, expected) -> None:
    assert d.part_2(example) == expected


@pytest.mark.parametrize(
    ("example", "expected"),
    [
        ((3, 5, 8), 4),
        ((122, 79, 57), -5),
        ((217, 196, 39), 0),
        ((101, 153, 71), 4),
    ],
)
def test_power_level(example: str, expected) -> None:
    assert d.power_level(*example) == expected

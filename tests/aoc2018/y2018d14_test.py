import pytest

import aoc_cj.aoc2018.day14 as d


@pytest.mark.parametrize(
    ("example", "expected"),
    [
        ("9", "5158916779"),
        ("5", "0124515891"),
        ("18", "9251071085"),
        ("2018", "5941429882"),
    ],
)
def test_part_1(example: str, expected) -> None:
    assert d.part_1(example) == expected


@pytest.mark.parametrize(
    ("example", "expected"),
    [
        ("51589", 9),
        ("01245", 5),
        ("92510", 18),
        ("59414", 2018),
    ],
)
def test_part_2(example: str, expected) -> None:
    assert d.part_2(example) == expected

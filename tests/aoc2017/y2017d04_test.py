import pytest

import aoc_cj.aoc2017.day04 as d


@pytest.mark.parametrize(
    ("example", "expected"),
    [
        ("aa bb cc dd ee", True),
        ("aa bb cc dd aa", False),
        ("aa bb cc dd aaa", True),
    ],
)
def test_is_valid(example: str, expected) -> None:
    assert d.is_valid_1(example) is expected


@pytest.mark.parametrize(
    ("example", "expected"),
    [
        ("abcde fghij", True),
        ("abcde xyz ecdab", False),
        ("a ab abc abd abf", True),
        ("iiii oiii ooii oooi", True),
        ("oiii ioii iioi", False),
    ],
)
def test_part_2(example: str, expected) -> None:
    assert d.is_valid_2(example) == expected

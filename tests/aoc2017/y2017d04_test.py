import pytest

import aoc_cj.aoc2017.day04 as d


@pytest.mark.parametrize(
    "input, expected",
    [
        ("aa bb cc dd ee", True),
        ("aa bb cc dd aa", False),
        ("aa bb cc dd aaa", True),
    ],
)
def test_is_valid(input, expected):
    assert d.is_valid_1(input) is expected


@pytest.mark.parametrize(
    "input, expected",
    [
        ("abcde fghij", True),
        ("abcde xyz ecdab", False),
        ("a ab abc abd abf", True),
        ("iiii oiii ooii oooi", True),
        ("oiii ioii iioi", False),
    ],
)
def test_part_2(input, expected):
    assert d.is_valid_2(input) == expected

import pytest

import advent.aoc2017.day04 as d


@pytest.mark.parametrize("input, expected", [
    ("aa bb cc dd ee", True),
    ("aa bb cc dd aa", False),
    ("aa bb cc dd aaa", True),
])
def test_is_valid(input, expected):
    assert d.is_valid(input) is expected


@pytest.mark.parametrize("input, expected", [
    ("abcde fghij", True),
    ("abcde xyz ecdab", False),
    ("a ab abc abd abf", True),
    ("iiii oiii ooii oooi",  True),
    ("oiii ioii iioi", False),
])
def test_b(input, expected):
    assert d.is_valid_b(input) == expected

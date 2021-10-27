import pytest

import aoc_cj.aoc2016.day07 as d


@pytest.mark.parametrize(
    "input, expected",
    [
        ("abba[mnop]qrst", True),
        ("abcd[bddb]xyyx", False),
        ("aaaa[qwer]tyui", False),
        ("ioxxoj[asdfgh]zxcvbn", True),
    ],
)
def test_supports_tls(input, expected):
    assert d.supports_tls(input) is expected


@pytest.mark.parametrize(
    "input, expected",
    [
        ("aba[bab]xyz", True),
        ("xyx[xyx]xyx", False),
        ("aaa[kek]eke", True),
        ("zazbz[bzb]cdb", True),
    ],
)
def test_supports_ssl(input, expected):
    assert d.supports_ssl(input) is expected

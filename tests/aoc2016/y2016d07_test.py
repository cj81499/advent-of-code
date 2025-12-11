import pytest

import aoc_cj.aoc2016.day07 as d


@pytest.mark.parametrize(
    ("example", "expected"),
    [
        ("abba[mnop]qrst", True),
        ("abcd[bddb]xyyx", False),
        ("aaaa[qwer]tyui", False),
        ("ioxxoj[asdfgh]zxcvbn", True),
    ],
)
def test_supports_tls(example: str, expected: int) -> None:
    assert d.supports_tls(example) is expected


@pytest.mark.parametrize(
    ("example", "expected"),
    [
        ("aba[bab]xyz", True),
        ("xyx[xyx]xyx", False),
        ("aaa[kek]eke", True),
        ("zazbz[bzb]cdb", True),
    ],
)
def test_supports_ssl(example: str, expected: int) -> None:
    assert d.supports_ssl(example) is expected

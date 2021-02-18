import pytest

import advent.aoc2016.day16 as d

EXAMPLE_INPUT = """
sample input
""".strip()


@pytest.mark.parametrize("input, expected", [
    ("1", "100"),
    ("0", "001"),
    ("11111", "11111000000"),
    ("111100001010", "1111000010100101011110000"),
])
def test_step(input, expected):
    assert d.step(input) == expected


def test_checksum():
    assert d.checksum("110010110100") == "100"


def test_a():
    assert d.parta("10000", length=20) == "01100"

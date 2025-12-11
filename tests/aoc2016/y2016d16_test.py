import pytest

import aoc_cj.aoc2016.day16 as d

EXAMPLE_INPUT = """
sample example
""".strip()


@pytest.mark.parametrize(
    ("example", "expected"),
    [
        ("1", "100"),
        ("0", "001"),
        ("11111", "11111000000"),
        ("111100001010", "1111000010100101011110000"),
    ],
)
def test_step(example: str, expected: str) -> None:
    assert d.step(example) == expected


def test_checksum() -> None:
    assert d.checksum("110010110100") == "100"


def test_part_1() -> None:
    assert d.part_1("10000", length=20) == "01100"

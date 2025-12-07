import pytest

import aoc_cj.aoc2020.day05 as d

EXAMPLE_INPUT = """
""".strip()


@pytest.mark.parametrize(
    ("example", "expected"),
    [
        ((0, 127, "F", "B", "FBFBBFF"), 44),
        ((0, 7, "L", "R", "RLR"), 5),
    ],
)
def test_binary_search(example: str, expected) -> None:
    assert expected == d.binary_search(*example)


@pytest.mark.parametrize(
    ("example", "expected"),
    [
        ("BFFFBBFRRR", 567),
        ("FFFBBBFRRR", 119),
        ("BBFFBBFRLL", 820),
    ],
)
def test_part_1(example: str, expected) -> None:
    assert expected == d.seat_id(example)

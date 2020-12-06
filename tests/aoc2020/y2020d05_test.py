import advent.aoc2020.day05 as d
import pytest

EXAMPLE_INPUT = """
""".strip()


@pytest.mark.parametrize("input, expected", [
    ((0, 127, "F", "B", "FBFBBFF"), 44),
    ((0, 7, "L", "R", "RLR"), 5),
])
def test_binary_search(input, expected):
    assert expected == d.binary_search(*input)


@pytest.mark.parametrize("input, expected", [
    ("BFFFBBFRRR", 567),
    ("FFFBBBFRRR", 119),
    ("BBFFBBFRLL", 820),
])
def test_a(input, expected):
    assert expected == d.seat_id(input)

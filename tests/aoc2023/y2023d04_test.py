import pytest

import aoc_cj.aoc2023.day04 as d

EXAMPLE_INPUT = """
Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11
""".strip()


@pytest.mark.parametrize(
    ("card_s", "expected_points"),
    zip(
        EXAMPLE_INPUT.splitlines(),
        (8, 2, 2, 1, 0, 0),
        strict=True,
    ),
)
def test_card_points(card_s: str, expected_points: int) -> None:
    assert d.Card.parse(card_s).points() == expected_points


def test_part_1() -> None:
    assert d.part_1(EXAMPLE_INPUT) == 13


def test_part_2() -> None:
    assert d.part_2(EXAMPLE_INPUT) == 30

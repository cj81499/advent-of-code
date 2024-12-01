import pytest

import aoc_cj.aoc2023.day07 as d

EXAMPLE_INPUT = """
32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483
""".strip()


@pytest.mark.parametrize(
    ("hand", "expected_type"),
    (
        (d.Hand("AAAAA", 1), d.Hand.Type.FIVE_OF_A_KIND),
        (d.Hand("AA8AA", 1), d.Hand.Type.FOUR_OF_A_KIND),
        (d.Hand("23332", 1), d.Hand.Type.FULL_HOUSE),
        (d.Hand("TTT98", 1), d.Hand.Type.THREE_OF_A_KIND),
        (d.Hand("23432", 1), d.Hand.Type.TWO_PAIR),
        (d.Hand("A23A4", 1), d.Hand.Type.ONE_PAIR),
        (d.Hand("23456", 1), d.Hand.Type.HIGH_CARD),
    ),
)
def test_hand_type_1(hand: d.Hand, expected_type: d.Hand.Type) -> None:
    assert hand.type == expected_type


def test_part_1() -> None:
    assert d.part_1(EXAMPLE_INPUT) == 6440


@pytest.mark.parametrize(
    ("hand", "expected_type"),
    (
        (d.HandB("32T3K", 1), d.Hand.Type.ONE_PAIR),
        (d.HandB("T55J5", 1), d.Hand.Type.FOUR_OF_A_KIND),
        (d.HandB("KK677", 1), d.Hand.Type.TWO_PAIR),
        (d.HandB("KTJJT", 1), d.Hand.Type.FOUR_OF_A_KIND),
        (d.HandB("QQQJA", 1), d.Hand.Type.FOUR_OF_A_KIND),
    ),
)
def test_hand_type_2(hand: d.HandB, expected_type: d.Hand.Type) -> None:
    assert hand.type == expected_type


def test_part_2() -> None:
    assert d.part_2(EXAMPLE_INPUT) == 5905

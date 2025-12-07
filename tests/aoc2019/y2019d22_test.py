import pytest

import aoc_cj.aoc2019.day22 as d

EXAMPLE_INPUT_0 = """
deal with increment 7
deal into new stack
deal into new stack
""".strip()

EXAMPLE_INPUT_1 = """
cut 6
deal with increment 7
deal into new stack
""".strip()

EXAMPLE_INPUT_2 = """
deal with increment 7
deal with increment 9
cut -2
""".strip()

EXAMPLE_INPUT_3 = """
deal into new stack
cut -2
deal with increment 7
cut 8
cut -4
deal with increment 7
cut 3
deal with increment 9
deal with increment 3
cut -1
""".strip()


def test_deal_into_new_stack() -> None:
    assert d.deal_into_new_stack(d.deck_of_size(10)) == [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]


def test_cut() -> None:
    assert d.cut(d.deck_of_size(10), 3) == [3, 4, 5, 6, 7, 8, 9, 0, 1, 2]


def test_cut_negative() -> None:
    assert d.cut(d.deck_of_size(10), -4) == [6, 7, 8, 9, 0, 1, 2, 3, 4, 5]


def test_deal_with_increment() -> None:
    assert d.deal_with_increment(d.deck_of_size(10), 3) == [0, 7, 4, 1, 8, 5, 2, 9, 6, 3]


@pytest.mark.parametrize(
    ("example", "expected"),
    [
        (EXAMPLE_INPUT_0, "0 3 6 9 2 5 8 1 4 7"),
        (EXAMPLE_INPUT_1, "3 0 7 4 1 8 5 2 9 6"),
        (EXAMPLE_INPUT_2, "6 3 0 7 4 1 8 5 2 9"),
        (EXAMPLE_INPUT_3, "9 2 5 8 1 4 7 0 3 6"),
    ],
)
def test_perform_shuffle(example: str, expected) -> None:
    assert d.perform_shuffle(example, deck_size=10) == [int(n) for n in expected.split()]

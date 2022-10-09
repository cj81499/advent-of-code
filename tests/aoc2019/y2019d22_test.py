import pytest

import aoc_cj.aoc2019.day22 as d

EXAMPLE_INPUT_0 = """
deal with increment 7
deal into new stack
deal into new stack
Result: 0 3 6 9 2 5 8 1 4 7
""".strip()

EXAMPLE_INPUT_1 = """
cut 6
deal with increment 7
deal into new stack
Result: 3 0 7 4 1 8 5 2 9 6
""".strip()

EXAMPLE_INPUT_2 = """
deal with increment 7
deal with increment 9
cut -2
Result: 6 3 0 7 4 1 8 5 2 9
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
Result: 9 2 5 8 1 4 7 0 3 6
""".strip()

EXAMPLES = (EXAMPLE_INPUT_0, EXAMPLE_INPUT_1, EXAMPLE_INPUT_2, EXAMPLE_INPUT_3)


def test_deal_into_new_stack():
    assert d.deal_into_new_stack(tuple(range(10))) == (9, 8, 7, 6, 5, 4, 3, 2, 1, 0)


@pytest.mark.parametrize(
    ("cut_size", "result"),
    (
        (3, (3, 4, 5, 6, 7, 8, 9, 0, 1, 2)),
        (-4, (6, 7, 8, 9, 0, 1, 2, 3, 4, 5)),
    ),
)
def test_cut(cut_size, result):
    assert d.cut(tuple(range(10)), cut_size) == result


def test_deal_with_increment():
    expected = (0, 7, 4, 1, 8, 5, 2, 9, 6, 3)
    assert d.deal_with_increment(tuple(range(10)), 3) == expected


@pytest.mark.parametrize("example", EXAMPLES)
def test_shuffle(example: str):
    *moves, result = example.splitlines()
    expected = tuple(map(int, result.strip("Result: ").split()))
    assert d.shuffle("\n".join(moves), 10) == expected

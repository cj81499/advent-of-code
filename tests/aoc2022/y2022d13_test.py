import aoc_cj.aoc2022.day13 as d

EXAMPLE_INPUT = """
[1,1,3,1,1]
[1,1,5,1,1]

[[1],[2,3,4]]
[[1],4]

[9]
[[8,7,6]]

[[4,4],4,4]
[[4,4],4,4,4]

[7,7,7,7]
[7,7,7]

[]
[3]

[[[]]]
[[]]

[1,[2,[3,[4,[5,6,7]]]],8,9]
[1,[2,[3,[4,[5,6,0]]]],8,9]
""".strip()


import pytest


@pytest.mark.parametrize(
    "l,r,expected",
    (
        ([1, 1, 3, 1, 1], [1, 1, 5, 1, 1], d.CompareResult.CORRECT),
        ([[1], [2, 3, 4]], [[1], 4], d.CompareResult.CORRECT),
        ([9], [[8, 7, 6]], d.CompareResult.INCORRECT),
        ([[4, 4], 4, 4], [[4, 4], 4, 4, 4], d.CompareResult.CORRECT),
        ([7, 7, 7, 7], [7, 7, 7], d.CompareResult.INCORRECT),
        ([], [3], d.CompareResult.CORRECT),
        ([[[]]], [[]], d.CompareResult.INCORRECT),
        ([1, [2, [3, [4, [5, 6, 7]]]], 8, 9], [1, [2, [3, [4, [5, 6, 0]]]], 8, 9], d.CompareResult.INCORRECT),
    ),
)
def test_compare(l: d.L, r: d.L, expected: d.CompareResult) -> None:
    assert d.compare(l, r) == expected


def test_part_1() -> None:
    assert d.part_1(EXAMPLE_INPUT) == 13


def test_part_2() -> None:
    assert d.part_2(EXAMPLE_INPUT) == 140

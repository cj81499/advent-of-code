from typing import List

import pytest

import advent.aoc2019.day04 as d


@pytest.mark.parametrize("input_val, expected", [
    (1, [1]),
    (123, [1, 2, 3]),
    (290875, [2, 9, 0, 8, 7, 5]),
    (65789543, [6, 5, 7, 8, 9, 5, 4, 3]),
])
def test_get_digits(input_val: int, expected: List[int]) -> None:
    assert d.get_digits(input_val) == expected


@pytest.mark.parametrize("input_val, expected", [
    (122345, True),  # 2
    (123456, False),
    (98234, False),
    (11, True),  # 1
    (111, True),  # 1
    (34928462923759214785230897132461234098, False),
    (349284629237592147855230897132461234098, True),  # 5
])
def test_adj_repeat(input_val: int, expected: bool) -> None:
    assert d.adj_repeat(d.get_digits(input_val)) == expected


@pytest.mark.parametrize("input_val, expected", [
    (111123, True),
    (135679, True),
    (912345, False),
    (123456, True),
    (654321, False),
])
def test_increasing_digits(input_val: int, expected: bool) -> None:
    assert d.increasing_digits(d.get_digits(input_val)) == expected


@pytest.mark.parametrize("input_val, expected", [
    (112233, True),
    (223450, False),  # decreasing pair (50)
    (123789, False),  # no double
])
def test_parta(input_val: int, expected: bool) -> None:
    assert d.is_valid_parta(d.get_digits(input_val)) == expected


@pytest.mark.parametrize("input_val, expected", [
    (112233, True),
    (123444, False),  # triple 4
    (111122, True),
])
def test_partb(input_val: int, expected: bool) -> None:
    assert d.is_valid_partb(d.get_digits(input_val)) == expected

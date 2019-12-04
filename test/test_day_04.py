from test import path_fix
import day_04


def test_adjacent_same():
    assert day_04.adj_repeat(122345) is True


def test_increasing_digits_0():
    assert day_04.increasing_digits(111123) is True


def test_increasing_digits_1():
    assert day_04.increasing_digits(135679) is True


def test_day_04_part1_0():
    assert day_04.is_valid_part1(112233) is True


def test_day_04_part1_1():
    assert day_04.is_valid_part1(223450) is False  # decreasing pair


def test_day_04_part1_2():
    assert day_04.is_valid_part1(123789) is False  # no double


def test_day_04_part2_0():
    assert day_04.is_valid_part2(112233) is True


def test_day_04_part2_1():
    assert day_04.is_valid_part2(123444) is False


def test_day_04_part2_2():
    assert day_04.is_valid_part2(111122) is True

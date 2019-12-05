import path_fix
import day_04


def test_adjacent_same():
    digits = day_04.get_digits(122345)
    assert day_04.adj_repeat(digits) is True


def test_increasing_digits_0():
    digits = day_04.get_digits(111123)
    assert day_04.increasing_digits(digits) is True


def test_increasing_digits_1():
    digits = day_04.get_digits(135679)
    assert day_04.increasing_digits(digits) is True


def test_day_04_part1_0():
    digits = day_04.get_digits(112233)
    assert day_04.is_valid_part1(digits) is True


def test_day_04_part1_1():
    digits = day_04.get_digits(223450)
    assert day_04.is_valid_part1(digits) is False  # decreasing pair


def test_day_04_part1_2():
    digits = day_04.get_digits(123789)
    assert day_04.is_valid_part1(digits) is False  # no double


def test_day_04_part2_0():
    digits = day_04.get_digits(112233)
    assert day_04.is_valid_part2(digits) is True


def test_day_04_part2_1():
    digits = day_04.get_digits(123444)
    assert day_04.is_valid_part2(digits) is False


def test_day_04_part2_2():
    digits = day_04.get_digits(111122)
    assert day_04.is_valid_part2(digits) is True

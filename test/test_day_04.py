import src.day_04 as d


def test_adjacent_same():
    digits = d.get_digits(122345)
    assert d.adj_repeat(digits) is True


def test_increasing_digits_0():
    digits = d.get_digits(111123)
    assert d.increasing_digits(digits) is True


def test_increasing_digits_1():
    digits = d.get_digits(135679)
    assert d.increasing_digits(digits) is True


def test_day_04_part1_0():
    digits = d.get_digits(112233)
    assert d.is_valid_part1(digits) is True


def test_day_04_part1_1():
    digits = d.get_digits(223450)
    assert d.is_valid_part1(digits) is False  # decreasing pair


def test_day_04_part1_2():
    digits = d.get_digits(123789)
    assert d.is_valid_part1(digits) is False  # no double


def test_day_04_part2_0():
    digits = d.get_digits(112233)
    assert d.is_valid_part2(digits) is True


def test_day_04_part2_1():
    digits = d.get_digits(123444)
    assert d.is_valid_part2(digits) is False


def test_day_04_part2_2():
    digits = d.get_digits(111122)
    assert d.is_valid_part2(digits) is True

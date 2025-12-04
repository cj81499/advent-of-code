import aoc_cj.aoc2015.day11 as d


def test_day11_is_valid_password() -> None:
    assert d.is_valid_password("hijklmmn") is False
    assert d.is_valid_password("abbceffg") is False
    assert d.is_valid_password("abbcegjk") is False
    assert d.is_valid_password("abcdffaa") is True
    assert d.is_valid_password("ghjaabcc") is True


def test_day11_increment_password() -> None:
    assert d.increment_password("a") == "b"
    assert d.increment_password("b") == "c"
    assert d.increment_password("c") == "d"
    assert d.increment_password("z") == "aa"
    assert d.increment_password("aa") == "ab"
    assert d.increment_password("ab") == "ac"
    assert d.increment_password("ac") == "ad"
    assert d.increment_password("za") == "zb"
    assert d.increment_password("zy") == "zz"
    assert d.increment_password("zz") == "aaa"


def test_part_1() -> None:
    assert next(d.generate_passwords("abcdefgh")) == "abcdffaa"
    assert next(d.generate_passwords("ghijklmn")) == "ghjaabcc"

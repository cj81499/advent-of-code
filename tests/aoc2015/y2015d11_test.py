import aoc_cj.aoc2015.day11 as d


def test_day11_is_valid_password() -> None:
    assert d.is_valid_password("hijklmmn") is False
    assert d.is_valid_password("abbceffg") is False
    assert d.is_valid_password("abbcegjk") is False
    assert d.is_valid_password("abcdffaa") is True
    assert d.is_valid_password("ghjaabcc") is True


def test_day11_increment_password() -> None:
    assert "b" == d.increment_password("a")
    assert "c" == d.increment_password("b")
    assert "d" == d.increment_password("c")
    assert "aa" == d.increment_password("z")
    assert "ab" == d.increment_password("aa")
    assert "ac" == d.increment_password("ab")
    assert "ad" == d.increment_password("ac")
    assert "zb" == d.increment_password("za")
    assert "zz" == d.increment_password("zy")
    assert "aaa" == d.increment_password("zz")


def test_part_1() -> None:
    assert "abcdffaa" == next(d.generate_passwords("abcdefgh"))
    assert "ghjaabcc" == next(d.generate_passwords("ghijklmn"))

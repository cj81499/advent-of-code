import advent.aoc2015.day11 as d


def test_day11_is_valid_password():
    assert d.is_valid_password("hijklmmn") is False
    assert d.is_valid_password("abbceffg") is False
    assert d.is_valid_password("abbcegjk") is False
    assert d.is_valid_password("abcdffaa") is True
    assert d.is_valid_password("ghjaabcc") is True


def test_day11_increment_password():
    assert "b", d.increment_password("a")
    assert "c", d.increment_password("b")
    assert "d", d.increment_password("c")
    assert "aa", d.increment_password("z")
    assert "ab", d.increment_password("aa")
    assert "ac", d.increment_password("ab")
    assert "ad", d.increment_password("ac")
    assert "zb", d.increment_password("za")
    assert "zz", d.increment_password("zy")
    assert "aaa", d.increment_password("zz")


def test_day11_fast_increment_password():
    assert "b", d.fast_increment_password("a")
    assert "c", d.fast_increment_password("b")
    assert "d", d.fast_increment_password("c")
    assert "aa", d.fast_increment_password("z")
    assert "ab", d.fast_increment_password("aa")
    assert "ac", d.fast_increment_password("ab")
    assert "ad", d.fast_increment_password("ac")
    assert "zb", d.fast_increment_password("za")
    assert "zz", d.fast_increment_password("zy")

    assert "j", d.fast_increment_password("i")
    assert "p", d.fast_increment_password("o")
    assert "m", d.fast_increment_password("l")

    assert "ja", d.fast_increment_password("ib")
    assert "pa", d.fast_increment_password("oa")
    assert "ma", d.fast_increment_password("lz")

    assert "jaaaaaaaaa", d.fast_increment_password("ibheqrmnad")
    assert "paaaaaaaaaa", d.fast_increment_password("omnzvcpqgqe")
    assert "maaaaaaaaa", d.fast_increment_password("lasdfupafj")


def test_a():
    assert "abcdffaa", d.next_valid_password("abcdefgh")
    assert "ghjaabcc", d.next_valid_password("ghijklmn")

# def test_b():
#     assert d.partb([]) == None

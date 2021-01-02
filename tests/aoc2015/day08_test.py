import advent.aoc2015.day08 as d


def test_a():
    assert d.decode("\"\"") == ""
    assert d.decode("\"abc\"") == "abc"
    assert d.decode("\"aaa\\\"aaa\"") == "aaa\"aaa"
    assert d.decode("\"\\x27\"") == "'"


def test_b():
    assert d.encode("\"\"") == "\"\\\"\\\"\""
    assert d.encode("\"abc\"") == "\"\\\"abc\\\"\""
    assert d.encode("\"aaa\\\"aaa\"") == "\"\\\"aaa\\\\\\\"aaa\\\"\""
    assert d.encode("\"\\x27\"") == "\"\\\"\\\\x27\\\"\""


import pytest

import advent.aoc2015.day08 as d


@pytest.mark.parametrize("input, expected", [
    (r""" "" """, r"""  """),
    (r""" "abc" """, r""" abc """),
    (r""" "aaa\"aaa" """, r""" aaa"aaa """),
    (r""" "\x27" """, r""" ' """),
])
def test_a(input, expected):
    assert d.decode(input.strip()) == expected.strip()


@pytest.mark.parametrize("input, expected", [
    (r""" "" """, r""" "\"\"" """),
    (r""" "abc" """, r""" "\"abc\"" """),
    (r""" "aaa\"aaa" """, r""" "\"aaa\\\"aaa\"" """),
    (r""" "\x27" """, r""" "\"\\x27\"" """),
])
def test_b(input, expected):
    assert d.encode(input.strip()) == expected.strip()

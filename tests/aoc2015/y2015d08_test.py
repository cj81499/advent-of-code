import pytest

import aoc_cj.aoc2015.day08 as d


@pytest.mark.parametrize(
    "input, expected",
    [
        (r""" "" """, r"""  """),
        (r""" "abc" """, r""" abc """),
        (r""" "aaa\"aaa" """, r""" aaa"aaa """),
        (r""" "\x27" """, r""" ' """),
    ],
)
def test_part_1(input: str, expected: str) -> None:
    assert d.decode(input.strip()) == expected.strip()


@pytest.mark.parametrize(
    "input, expected",
    [
        (r""" "" """, r""" "\"\"" """),
        (r""" "abc" """, r""" "\"abc\"" """),
        (r""" "aaa\"aaa" """, r""" "\"aaa\\\"aaa\"" """),
        (r""" "\x27" """, r""" "\"\\x27\"" """),
    ],
)
def test_part_2(input: str, expected: str) -> None:
    assert d.encode(input.strip()) == expected.strip()

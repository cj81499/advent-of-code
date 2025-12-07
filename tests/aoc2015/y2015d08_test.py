import pytest

import aoc_cj.aoc2015.day08 as d


@pytest.mark.parametrize(
    ("example", "expected"),
    [
        (r""" "" """, r"""  """),
        (r""" "abc" """, r""" abc """),
        (r""" "aaa\"aaa" """, r""" aaa"aaa """),
        (r""" "\x27" """, r""" ' """),
    ],
)
def test_part_1(example: str, expected: str) -> None:
    assert d.decode(example.strip()) == expected.strip()


@pytest.mark.parametrize(
    ("example", "expected"),
    [
        (r""" "" """, r""" "\"\"" """),
        (r""" "abc" """, r""" "\"abc\"" """),
        (r""" "aaa\"aaa" """, r""" "\"aaa\\\"aaa\"" """),
        (r""" "\x27" """, r""" "\"\\x27\"" """),
    ],
)
def test_part_2(example: str, expected: str) -> None:
    assert d.encode(example.strip()) == expected.strip()

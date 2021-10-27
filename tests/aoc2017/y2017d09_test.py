import pytest

import aoc_cj.aoc2017.day09 as d


@pytest.mark.parametrize(
    "input, expected",
    [
        (r"{}", 1),
        (r"{{{}}}", 6),
        (r"{{},{}}", 5),
        (r"{{{},{},{{}}}}", 16),
        (r"{<a>,<a>,<a>,<a>}", 1),
        (r"{{<ab>},{<ab>},{<ab>},{<ab>}}", 9),
        (r"{{<!!>},{<!!>},{<!!>},{<!!>}}", 9),
        (r"{{<a!>},{<a!>},{<a!>},{<ab>}}", 3),
    ],
)
def test_a(input, expected):
    assert d.parta(input) == expected


@pytest.mark.parametrize(
    "input, expected",
    [
        (r"<>", 0),
        (r"<random characters>", 17),
        (r"<<<<>", 3),
        (r"<{!>}>", 2),
        (r"<!!>", 0),
        (r"<!!!>>", 0),
        (r"""<{o"i!a,<{i<a>""", 10),
    ],
)
def test_b(input, expected):
    assert d.partb(input) == expected

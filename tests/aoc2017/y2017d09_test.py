import pytest

import aoc_cj.aoc2017.day09 as d


@pytest.mark.parametrize(
    ("example", "expected"),
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
def test_part_1(example: str, expected) -> None:
    assert d.part_1(example) == expected


@pytest.mark.parametrize(
    ("example", "expected"),
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
def test_part_2(example: str, expected) -> None:
    assert d.part_2(example) == expected

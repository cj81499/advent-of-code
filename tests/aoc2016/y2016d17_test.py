import pytest

import advent.aoc2016.day17 as d


def test_is_open():
    assert d.is_open("hijkl", "") == (True, True, True, False)


@pytest.mark.parametrize("input, expected", [
    ("hijkl", None),
    ("ihgpwlah", "DDRRRD"),
    ("kglvqrro", "DDUDRLRRUDRD"),
    ("ulqzkmiv", "DRURDRUDDLLDLUURRDULRLDUUDDDRR"),
])
def test_a(input, expected):
    assert d.parta(input) == expected


@pytest.mark.parametrize("input, expected", [
    ("ihgpwlah", 370),
    ("kglvqrro", 492),
    ("ulqzkmiv", 830),
])
def test_b(input, expected):
    assert d.partb(input) == expected

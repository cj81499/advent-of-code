import pytest

import aoc_cj.aoc2015.day19 as d

REPLACEMENTS = """
e => H
e => O
H => HO
H => OH
O => HH
""".strip()

EXAMPLE_INPUT_0 = "HOH"
EXAMPLE_INPUT_1 = "HOHOHO"


@pytest.mark.parametrize(
    "input, expected",
    [
        (EXAMPLE_INPUT_0, 4),
        (EXAMPLE_INPUT_1, 7),
    ],
)
def test_a(input, expected):
    input = f"{REPLACEMENTS}\n\n{input}"
    assert d.parta(input) == expected


@pytest.mark.parametrize(
    "input, expected",
    [
        (EXAMPLE_INPUT_0, 3),
        (EXAMPLE_INPUT_1, 6),
    ],
)
def test_b(input, expected):
    input = f"{REPLACEMENTS}\n\n{input}"
    assert d.partb(input) == expected

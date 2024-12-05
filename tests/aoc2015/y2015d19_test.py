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
def test_part_1(input: str, expected: int) -> None:
    input = f"{REPLACEMENTS}\n\n{input}"
    assert d.part_1(input) == expected


@pytest.mark.parametrize(
    "input, expected",
    [
        (EXAMPLE_INPUT_0, 3),
        (EXAMPLE_INPUT_1, 6),
    ],
)
def test_part_2(input: str, expected: int) -> None:
    input = f"{REPLACEMENTS}\n\n{input}"
    assert d.part_2(input) == expected

import pytest

import aoc_cj.aoc2019.day01 as d

EXAMPLE_0 = 12
EXAMPLE_1 = 14
EXAMPLE_2 = 1969
EXAMPLE_3 = 100756


@pytest.mark.parametrize(
    ("example", "expected"),
    [
        (EXAMPLE_0, 2),
        (EXAMPLE_1, 2),
        (EXAMPLE_2, 654),
        (EXAMPLE_3, 33583),
    ],
)
def test_part_1(example: int, expected: int) -> None:
    assert d.fuel_req(example) == expected


@pytest.mark.parametrize(
    ("example", "expected"),
    [
        (EXAMPLE_0, 2),
        (EXAMPLE_1, 2),
        (EXAMPLE_2, 966),
        (EXAMPLE_3, 50346),
    ],
)
def test_part_2(example: int, expected: int) -> None:
    assert d.fuel_req_rec(example) == expected

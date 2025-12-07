import pytest

import aoc_cj.aoc2017.day10 as d


def test_part_1() -> None:
    assert d.part_1("3, 4, 1, 5", list_size=5) == 12


@pytest.mark.parametrize(
    ("example", "expected"),
    [
        ("", "a2582a3a0e66e6e86e3812dcb672a272"),
        ("AoC 2017", "33efeb34ea91902bb2f59c9920caa6cd"),
        ("1,2,3", "3efbe78a8d82f29979031a4aa0b16a9d"),
        ("1,2,4", "63960835bcdc130f0b66d7ff4f6a5a8e"),
    ],
)
def test_part_2(example: str, expected) -> None:
    assert d.part_2(example) == expected

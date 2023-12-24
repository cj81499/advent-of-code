import pytest

import aoc_cj.aoc2019.day03 as d

EXAMPLE_0 = """
R8,U5,L5,D3
U7,R6,D4,L4
""".strip()

EXAMPLE_1 = """
R75,D30,R83,U83,L12,D49,R71,U7,L72
U62,R66,U55,R34,D71,R55,D58,R83
""".strip()

EXAMPLE_2 = """
R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51
U98,R91,D20,R16,D67,R40,U7,R15,U6,R7
""".strip()


@pytest.mark.parametrize(
    "input_val, expected",
    [
        (EXAMPLE_0, 6),
        (EXAMPLE_1, 159),
        (EXAMPLE_2, 135),
    ],
)
def test_part_1(input_val, expected: int) -> None:
    assert d.part_1(input_val) == expected


@pytest.mark.parametrize(
    "input_val, expected",
    [
        (EXAMPLE_0, 30),
        (EXAMPLE_1, 610),
        (EXAMPLE_2, 410),
    ],
)
def test_part_2(input_val, expected: int) -> None:
    assert d.part_2(input_val) == expected

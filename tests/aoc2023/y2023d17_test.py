import pytest

import aoc_cj.aoc2023.day17 as d

EXAMPLE_INPUT = """
2413432311323
3215453535623
3255245654254
3446585845452
4546657867536
1438598798454
4457876987766
3637877979653
4654967986887
4564679986453
1224686865563
2546548887735
4322674655533
""".strip()

EXAMPLE_INPUT_2 = """
111111111111
999999999991
999999999991
999999999991
999999999991
""".strip()


def test_part_1() -> None:
    assert d.part_1(EXAMPLE_INPUT) == 102


@pytest.mark.parametrize(
    ("example_example", "expected"),
    [
        (EXAMPLE_INPUT, 94),
        (EXAMPLE_INPUT_2, 71),
    ],
)
def test_part_2(example_example: str, expected: int) -> None:
    assert d.part_2(example_example) == expected

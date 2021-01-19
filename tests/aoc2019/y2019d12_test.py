import pytest

import advent.aoc2019.day12 as d

EXAMPLE_0 = """
<x=-1, y=0, z=2>
<x=2, y=-10, z=-7>
<x=4, y=-8, z=8>
<x=3, y=5, z=-1>
""".strip()

EXAMPLE_1 = """
<x=-8, y=-10, z=0>
<x=5, y=5, z=10>
<x=2, y=-7, z=3>
<x=9, y=-8, z=-3>
""".strip()


@pytest.mark.parametrize("input_val, step_count, expected", [
    (EXAMPLE_0, 10, 179),
    (EXAMPLE_1, 100, 1940),
])
def test_energy(input_val, step_count: int, expected: int) -> None:
    assert d.parta(input_val, step_count) == expected


@pytest.mark.parametrize("input_val, required_steps", [
    (EXAMPLE_0, 2772),
    (EXAMPLE_1, 4686774924),
])
def test_partb(input_val, required_steps: int) -> None:
    assert d.partb(input_val) == required_steps

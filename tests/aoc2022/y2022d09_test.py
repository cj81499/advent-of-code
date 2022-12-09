import pytest

import aoc_cj.aoc2022.day09 as d

EXAMPLE_INPUT_1 = """
R 4
U 4
L 3
D 1
R 4
D 1
L 5
R 2
""".strip()

EXAMPLE_INPUT_2 = """
R 5
U 8
L 8
D 3
R 17
D 10
L 25
U 20
""".strip()


@pytest.mark.parametrize(
    ("lead_knot", "trail_knot", "expected"),
    (
        # same position. should not move.
        (d.ORIGIN, d.ORIGIN, d.ORIGIN),
        # 1 away in 1 direction (adjacent). should not move.
        (d.UP, d.ORIGIN, d.ORIGIN),
        (d.DOWN, d.ORIGIN, d.ORIGIN),
        (d.LEFT, d.ORIGIN, d.ORIGIN),
        (d.RIGHT, d.ORIGIN, d.ORIGIN),
        # 1 away in 2 directions (diagonal). should not move.
        (d.UP + d.LEFT, d.ORIGIN, d.ORIGIN),
        (d.UP + d.RIGHT, d.ORIGIN, d.ORIGIN),
        (d.DOWN + d.LEFT, d.ORIGIN, d.ORIGIN),
        (d.DOWN + d.RIGHT, d.ORIGIN, d.ORIGIN),
        # 2 away in 1 direction. should move 1 space.
        (2 * d.UP, d.ORIGIN, d.UP),
        (2 * d.DOWN, d.ORIGIN, d.DOWN),
        (2 * d.LEFT, d.ORIGIN, d.LEFT),
        (2 * d.RIGHT, d.ORIGIN, d.RIGHT),
        # 2 away in 1 direction, 1 away in another direction. should move 2 spaces.
        (2 * d.UP + d.LEFT, d.ORIGIN, d.UP + d.LEFT),
        (2 * d.UP + d.RIGHT, d.ORIGIN, d.UP + d.RIGHT),
        (2 * d.DOWN + d.LEFT, d.ORIGIN, d.DOWN + d.LEFT),
        (2 * d.DOWN + d.RIGHT, d.ORIGIN, d.DOWN + d.RIGHT),
        (2 * d.LEFT + d.UP, d.ORIGIN, d.LEFT + d.UP),
        (2 * d.LEFT + d.DOWN, d.ORIGIN, d.LEFT + d.DOWN),
        (2 * d.RIGHT + d.UP, d.ORIGIN, d.RIGHT + d.UP),
        (2 * d.RIGHT + d.DOWN, d.ORIGIN, d.RIGHT + d.DOWN),
    ),
)
def test_pull(lead_knot: complex, trail_knot: complex, expected: complex) -> None:
    assert d.pull(lead_knot, trail_knot) == expected


def test_a() -> None:
    assert d.parta(EXAMPLE_INPUT_1) == 13


@pytest.mark.parametrize(
    ("example", "expected"),
    (
        (EXAMPLE_INPUT_1, 1),
        (EXAMPLE_INPUT_2, 36),
    ),
)
def test_b(example: str, expected: int) -> None:
    assert d.partb(example) == expected

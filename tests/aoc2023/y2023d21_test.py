import pytest

import aoc_cj.aoc2023.day21 as d

EXAMPLE_INPUT = """
...........
.....###.#.
.###.##..#.
..#.#...#..
....#.#....
.##..S####.
.##..#...#.
.......##..
.##.#.####.
.##..##.##.
...........
""".strip()


@pytest.mark.parametrize(
    ("steps", "expected"),
    (
        (1, 2),
        (2, 4),
        (3, 6),
        (6, 16),
        (10, 50),
        (50, 1594),
        (100, 6536),
        # FIXME: this is the point where simulating gets quite slow.
        # Enabling these will require solving part 2/b
        # (500, 167004),
        # (1000, 668697),
        # (5000, 16733044),
    ),
)
def test_solve(steps: int, expected: int) -> None:
    assert d.solve(EXAMPLE_INPUT, steps) == expected

from collections import Counter

import pytest

import aoc_cj.aoc2024.day20 as d

EXAMPLE_INPUT = """
###############
#...#...#.....#
#.#.#.#.#.###.#
#S#...#.#.#...#
#######.#.#.###
#######.#.#...#
#######.#.###.#
###..E#...#...#
###.#######.###
#...###...#...#
#.#####.#.###.#
#.#...#.#.#...#
#.#.#.#.#.#.###
#...#...#...###
###############
""".strip()

EXPECTED_SAVINGS_1 = {2: 14, 4: 14, 6: 2, 8: 4, 10: 2, 12: 3, 20: 1, 36: 1, 38: 1, 40: 1, 64: 1}
EXPECTED_SAVINGS_2 = {
    50: 32,
    52: 31,
    54: 29,
    56: 39,
    58: 25,
    60: 23,
    62: 20,
    64: 19,
    66: 12,
    68: 14,
    70: 12,
    72: 22,
    74: 4,
    76: 3,
}


@pytest.mark.parametrize(
    ("min_savings", "max_cheat_duration", "expected_savings_counts"),
    [
        (1, 2, EXPECTED_SAVINGS_1),
        (50, 20, EXPECTED_SAVINGS_2),
    ],
)
def test_cheat_generator(min_savings: int, max_cheat_duration: int, expected_savings_counts: dict[int, int]) -> None:
    cheats = d.cheat_generator(EXAMPLE_INPUT, max_cheat_duration=max_cheat_duration)
    counts = Counter(c for c in cheats if c >= min_savings)
    assert counts == expected_savings_counts

import pytest

import aoc_cj.aoc2018.day15 as d

EXAMPLE_INPUT_0 = """
#######
#.G...#
#...EG#
#.#.#G#
#..G#E#
#.....#
#######
""".strip()

EXAMPLE_INPUT_1 = """
#######
#G..#E#
#E#E.E#
#G.##.#
#...#E#
#...E.#
#######
""".strip()

EXAMPLE_INPUT_2 = """
#######
#E..EG#
#.#G.E#
#E.##E#
#G..#.#
#..E#.#
#######
""".strip()

EXAMPLE_INPUT_3 = """
#######
#E.G#.#
#.#G..#
#G.#.G#
#G..#.#
#...E.#
#######
""".strip()

EXAMPLE_INPUT_4 = """
#######
#.E...#
#.#..G#
#.###.#
#E#G#G#
#...#G#
#######
""".strip()

EXAMPLE_INPUT_5 = """
#########
#G......#
#.E.#...#
#..##..G#
#...##..#
#...#...#
#.G...G.#
#.....G.#
#########
""".strip()


@pytest.mark.parametrize(
    ("example", "expected"),
    [
        (EXAMPLE_INPUT_0, 27730),
        (EXAMPLE_INPUT_1, 36334),
        (EXAMPLE_INPUT_2, 39514),
        (EXAMPLE_INPUT_3, 27755),
        (EXAMPLE_INPUT_4, 28944),
        (EXAMPLE_INPUT_5, 18740),
    ],
)
def test_part_1(example: str, expected) -> None:
    assert d.part_1(example) == expected


@pytest.mark.parametrize(
    ("example", "expected"),
    [
        (EXAMPLE_INPUT_0, 4988),
        (EXAMPLE_INPUT_2, 31284),
        (EXAMPLE_INPUT_3, 3478),
        (EXAMPLE_INPUT_4, 6474),
        (EXAMPLE_INPUT_5, 1140),
    ],
)
def test_part_2(example: str, expected) -> None:
    assert d.part_2(example) == expected

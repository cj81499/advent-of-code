import pytest

import aoc_cj.aoc2023.day10 as d

EXAMPLE_INPUT_1 = """
.....
.S-7.
.|.|.
.L-J.
.....
""".strip()

EXAMPLE_INPUT_2 = """
..F7.
.FJ|.
SJ.L7
|F--J
LJ...
""".strip()

EXAMPLE_INPUT_3 = """
...........
.S-------7.
.|F-----7|.
.||.....||.
.||.....||.
.|L-7.F-J|.
.|..|.|..|.
.L--J.L--J.
...........
""".strip()

EXAMPLE_INPUT_4 = """
..........
.S------7.
.|F----7|.
.||OOOO||.
.||OOOO||.
.|L-7F-J|.
.|II||II|.
.L--JL--J.
..........
""".strip()

EXAMPLE_INPUT_5 = """
.F----7F7F7F7F-7....
.|F--7||||||||FJ....
.||.FJ||||||||L7....
FJL7L7LJLJ||LJ.L-7..
L--J.L7...LJS7F-7L7.
....F-J..F7FJ|L7L7L7
....L7.F7||L7|.L7L7|
.....|FJLJ|FJ|F7|.LJ
....FJL-7.||.||||...
....L---J.LJ.LJLJ...
""".strip()


EXAMPLE_INPUT_6 = """
FF7FSF7F7F7F7F7F---7
L|LJ||||||||||||F--J
FL-7LJLJ||||||LJL-77
F--JF--7||LJLJ7F7FJ-
L---JF-JLJ.||-FJLJJ7
|F|F-JF---7F7-L7L|7|
|FFJF7L7F-JF7|JL---7
7-L-JL7||F7|L7F-7F7|
L.L7LFJ|||||FJL7||LJ
L7JLJL-JLJLJL--JLJ.L
""".strip()


@pytest.mark.parametrize(
    ("example_input", "expected"),
    (
        (EXAMPLE_INPUT_1, 4),
        (EXAMPLE_INPUT_2, 8),
    ),
)
def test_part_1(example_input: str, expected: int) -> None:
    assert d.part_1(example_input) == expected


@pytest.mark.parametrize(
    ("example_input", "expected"),
    (
        (EXAMPLE_INPUT_3, 4),
        (EXAMPLE_INPUT_4, 4),
        (EXAMPLE_INPUT_5, 8),
        (EXAMPLE_INPUT_6, 10),
    ),
)
def test_part_2(example_input: str, expected: int) -> None:
    assert d.part_2(example_input) == expected

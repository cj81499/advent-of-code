import aoc_cj.aoc2023.day16 as d

EXAMPLE_INPUT = """
.|...\\....
|.-.\\.....
.....|-...
........|.
..........
.........\\
..../.\\\\..
.-.-/..|..
.|....-|.\\
..//.|....
""".strip()


def test_part_1() -> None:
    assert d.part_1(EXAMPLE_INPUT) == 46


def test_part_2() -> None:
    assert d.part_2(EXAMPLE_INPUT) == 51

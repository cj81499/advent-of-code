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


def test_a() -> None:
    assert d.parta(EXAMPLE_INPUT) == 46


def test_b() -> None:
    assert d.partb(EXAMPLE_INPUT) == 51

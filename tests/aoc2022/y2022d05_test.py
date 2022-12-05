import aoc_cj.aoc2022.day05 as d

EXAMPLE_INPUT = """
    [D]
[N] [C]
[Z] [M] [P]
 1   2   3

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2
""".rstrip()


def test_a() -> None:
    assert d.parta(EXAMPLE_INPUT) == "CMZ"


def test_b() -> None:
    assert d.partb(EXAMPLE_INPUT) == "MCD"

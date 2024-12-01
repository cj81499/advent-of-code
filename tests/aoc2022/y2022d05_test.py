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


def test_part_1() -> None:
    assert d.part_1(EXAMPLE_INPUT) == "CMZ"


def test_part_2() -> None:
    assert d.part_2(EXAMPLE_INPUT) == "MCD"

import aoc_cj.aoc2022.day12 as d

EXAMPLE_INPUT = """
Sabqponm
abcryxxl
accszExk
acctuvwj
abdefghi
""".strip()


def test_part_1() -> None:
    assert d.part_1(EXAMPLE_INPUT) == 31


def test_part_2() -> None:
    assert d.part_2(EXAMPLE_INPUT) == 29

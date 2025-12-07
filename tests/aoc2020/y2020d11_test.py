import aoc_cj.aoc2020.day11 as d

EXAMPLE_INPUT = """
L.LL.LL.LL
LLLLLLL.LL
L.L.L..L..
LLLL.LL.LL
L.LL.LL.LL
L.LLLLL.LL
..L.L.....
LLLLLLLLLL
L.LLLLLL.L
L.LLLLL.LL
""".strip()


def test_part_1() -> None:
    assert d.part_1(EXAMPLE_INPUT) == 37


def test_part_2() -> None:
    assert d.part_2(EXAMPLE_INPUT) == 26

import aoc_cj.aoc2018.day06 as d

EXAMPLE_INPUT = """
1, 1
1, 6
8, 3
3, 4
5, 5
8, 9
""".strip()


def test_part_1() -> None:
    assert d.part_1(EXAMPLE_INPUT) == 17


def test_part_2() -> None:
    assert d.part_2(EXAMPLE_INPUT, total_dist=32) == 16

import aoc_cj.aoc2024.day10 as d

EXAMPLE_INPUT = """
89010123
78121874
87430965
96549874
45678903
32019012
01329801
10456732
""".strip()


def test_part_1() -> None:
    assert d.part_1(EXAMPLE_INPUT) == 36


def test_part_2() -> None:
    assert d.part_2(EXAMPLE_INPUT) == 81

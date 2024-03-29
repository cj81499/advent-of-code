import aoc_cj.aoc2021.day15 as d

EXAMPLE_INPUT = """
1163751742
1381373672
2136511328
3694931569
7463417111
1319128137
1359912421
3125421639
1293138521
2311944581
""".strip()


def test_part_1():
    assert d.part_1(EXAMPLE_INPUT) == 40


def test_part_2():
    assert d.part_2(EXAMPLE_INPUT) == 315

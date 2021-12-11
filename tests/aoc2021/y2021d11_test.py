import aoc_cj.aoc2021.day11 as d

EXAMPLE_INPUT = """
5483143223
2745854711
5264556173
6141336146
6357385478
4167524645
2176841721
6882881134
4846848554
5283751526
""".strip()

INITIAL = """
11111
19991
19191
19991
11111
""".strip()

AFTER_1 = """
34543
40004
50005
40004
34543
""".strip()

AFTER_2 = """
45654
51115
61116
51115
45654
""".strip()


def test_step():
    initial_grid = d.parse(INITIAL)
    after_1_grid = d.parse(AFTER_1)
    after_2_grid = d.parse(AFTER_2)
    assert d.step(initial_grid)[1] == after_1_grid
    assert d.step(after_1_grid)[1] == after_2_grid


def test_a():
    assert d.parta(EXAMPLE_INPUT) == 1656


def test_b():
    assert d.partb(EXAMPLE_INPUT) == 195

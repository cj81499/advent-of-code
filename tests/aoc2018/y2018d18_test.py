import aoc_cj.aoc2018.day18 as d

EXAMPLE_INPUT = """
.#.#...|#.
.....#|##|
.|..|...#.
..|#.....#
#.#|||#|#|
...#.||...
.|....|...
||...#|.#|
|.||||..|.
...#.|..|.
""".strip()


def test_part_1():
    assert d.part_1(EXAMPLE_INPUT) == 1147


def test_part_2():
    assert d.part_2(EXAMPLE_INPUT) == 0

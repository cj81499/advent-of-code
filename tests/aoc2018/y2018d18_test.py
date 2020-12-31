import advent.aoc2018.day18 as d

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


def test_a():
    assert d.parta(EXAMPLE_INPUT) == 1147


def test_b():
    assert d.partb(EXAMPLE_INPUT) == 0

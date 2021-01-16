import advent.aoc2017.day21 as d

EXAMPLE_INPUT = """
../.# => ##./#../...
.#./..#/### => #..#/..../..../#..#
""".strip()


def test_a():
    assert d.parta(EXAMPLE_INPUT, iterations=2) == 12

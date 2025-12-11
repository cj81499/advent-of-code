import aoc_cj.aoc2017.day21 as d

EXAMPLE_INPUT = """
../.# => ##./#../...
.#./..#/### => #..#/..../..../#..#
""".strip()


def test_part_1() -> None:
    assert d.part_1(EXAMPLE_INPUT, iterations=2) == 12

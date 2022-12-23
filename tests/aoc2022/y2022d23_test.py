import aoc_cj.aoc2022.day23 as d

EXAMPLE_INPUT = """
....#..
..###.#
#...#.#
.#...##
#.###..
##.#.##
.#..#..
""".strip()


def test_a() -> None:
    assert d.parta(EXAMPLE_INPUT) == 110


def test_b() -> None:
    assert d.partb(EXAMPLE_INPUT) == 20

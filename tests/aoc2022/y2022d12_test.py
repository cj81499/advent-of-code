import aoc_cj.aoc2022.day12 as d

EXAMPLE_INPUT = """
Sabqponm
abcryxxl
accszExk
acctuvwj
abdefghi
""".strip()


def test_a() -> None:
    assert d.parta(EXAMPLE_INPUT) == 31


def test_b() -> None:
    assert d.partb(EXAMPLE_INPUT) == 29

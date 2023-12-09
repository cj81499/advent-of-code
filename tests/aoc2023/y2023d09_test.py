import aoc_cj.aoc2023.day09 as d

EXAMPLE_INPUT = """
0 3 6 9 12 15
1 3 6 10 15 21
10 13 16 21 30 45
""".strip()


def test_a() -> None:
    assert d.parta(EXAMPLE_INPUT) == 114


def test_b() -> None:
    assert d.partb(EXAMPLE_INPUT) == 2

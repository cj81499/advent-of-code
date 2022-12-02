import aoc_cj.aoc2022.day02 as d

EXAMPLE_INPUT = """
A Y
B X
C Z
""".strip()


def test_a() -> None:
    assert d.parta(EXAMPLE_INPUT) == 15


def test_b() -> None:
    assert d.partb(EXAMPLE_INPUT) == 12

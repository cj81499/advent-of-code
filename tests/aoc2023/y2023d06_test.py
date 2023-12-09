import aoc_cj.aoc2023.day06 as d

EXAMPLE_INPUT = """
Time:      7  15   30
Distance:  9  40  200
""".strip()


def test_a() -> None:
    assert d.parta(EXAMPLE_INPUT) == 288


def test_b() -> None:
    assert d.partb(EXAMPLE_INPUT) == 71503

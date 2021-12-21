import aoc_cj.aoc2021.day21 as d

EXAMPLE_INPUT = """
Player 1 starting position: 4
Player 2 starting position: 8
""".strip()


def test_a():
    assert d.parta(EXAMPLE_INPUT) == 739785


def test_b():
    assert d.partb(EXAMPLE_INPUT) == 444356092776315

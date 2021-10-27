import aoc_cj.aoc2020.day22 as d

EXAMPLE_INPUT = """
Player 1:
9
2
6
3
1

Player 2:
5
8
4
7
10
""".strip()


def test_a():
    assert d.parta(EXAMPLE_INPUT) == 306


def test_b():
    assert d.partb(EXAMPLE_INPUT) == 291

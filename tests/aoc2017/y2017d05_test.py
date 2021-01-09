import advent.aoc2017.day05 as d

EXAMPLE_INPUT_0 = "0 3 0 1 -3".replace(" ", "\n")

# EXAMPLE_INPUT_1 = """
# 5 9 2 8
# 9 4 7 3
# 3 8 6 5
# """.strip()


def test_a():
    assert d.parta(EXAMPLE_INPUT_0) == 5


def test_b():
    assert d.partb(EXAMPLE_INPUT_0) == 10

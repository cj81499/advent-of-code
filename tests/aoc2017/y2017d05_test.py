import advent.aoc2017.day05 as d

EXAMPLE_INPUT_0 = "0 3 0 1 -3".replace(" ", "\n")


def test_a():
    assert d.parta(EXAMPLE_INPUT_0) == 5


def test_b():
    assert d.partb(EXAMPLE_INPUT_0) == 10

import aoc_cj.aoc2017.day08 as d

EXAMPLE_INPUT = """
b inc 5 if a > 1
a inc 1 if b < 5
c dec -10 if a >= 1
c inc -20 if c == 10
""".strip()


def test_a():
    assert d.parta(EXAMPLE_INPUT) == 1


def test_b():
    assert d.partb(EXAMPLE_INPUT) == 10

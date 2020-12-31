import advent.aoc2018.day22 as d

EXAMPLE_INPUT = """
depth: 510
target: 10,10
""".strip()


def test_a():
    assert d.parta(EXAMPLE_INPUT) == 114


# def test_b():
#     assert d.partb(EXAMPLE_INPUT) == 45

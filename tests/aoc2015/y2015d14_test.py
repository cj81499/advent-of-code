import advent.aoc2015.day14 as d

EXAMPLE_INPUT = """
Comet can fly 14 km/s for 10 seconds, but then must rest for 127 seconds.
Dancer can fly 16 km/s for 11 seconds, but then must rest for 162 seconds.
""".strip()


def test_a():
    assert d.parta(EXAMPLE_INPUT, 1000) == 1120


def test_b():
    assert d.partb(EXAMPLE_INPUT, 1000) == 689

import aoc_cj.aoc2015.day14 as d

EXAMPLE_INPUT = """
Comet can fly 14 km/s for 10 seconds, but then must rest for 127 seconds.
Dancer can fly 16 km/s for 11 seconds, but then must rest for 162 seconds.
""".strip()


def test_part_1():
    assert d.part_1(EXAMPLE_INPUT, 1000) == 1120


def test_part_2():
    assert d.part_2(EXAMPLE_INPUT, 1000) == 689

import advent.aoc2020.day01 as d

EXAMPLE_INPUT = """1721
979
366
299
675
1456
"""


def test_a():
    assert 514579 == d.parta(EXAMPLE_INPUT)


def test_b():
    assert 241861950 == d.partb(EXAMPLE_INPUT)

import advent.aoc2020.day09 as d

EXAMPLE_INPUT = """
35
20
15
25
47
40
62
55
65
95
102
117
150
182
127
219
299
277
309
576
""".strip()


def test_a():
    assert d.parta(EXAMPLE_INPUT, preamble_size=5) == 127


def test_b():
    assert d.partb(EXAMPLE_INPUT, preamble_size=5) == 62

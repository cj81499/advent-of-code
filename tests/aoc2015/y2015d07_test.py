import advent.aoc2015.day07 as d

EXAMPLE_INPUT = """
123 -> x
456 -> y
x AND y -> d
x OR y -> e
x LSHIFT 2 -> f
y RSHIFT 2 -> g
NOT x -> h
NOT y -> i
""".strip()


def test_a():
    wires = {}
    d.run(d.build_instructions_deque(EXAMPLE_INPUT), wires)

    expected = {"d": 72, "e": 507, "f": 492, "g": 114, "h": 65412, "i": 65079, "x": 123, "y": 456}

    assert wires == expected

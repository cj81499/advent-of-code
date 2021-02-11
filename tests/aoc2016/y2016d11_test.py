import advent.aoc2016.day11 as d

EXAMPLE_INPUT = """
The first floor contains a hydrogen-compatible microchip and a lithium-compatible microchip.
The second floor contains a hydrogen generator.
The third floor contains a lithium generator.
The fourth floor contains nothing relevant.
""".strip()


def test_a():
    assert d.parta(EXAMPLE_INPUT) == 11

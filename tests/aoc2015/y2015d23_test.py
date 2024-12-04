import aoc_cj.aoc2015.day23 as d

EXAMPLE_INPUT = """
inc a
jio a, +2
tpl a
inc a
""".strip()


def test_simulate() -> None:
    registers = d.simulate(EXAMPLE_INPUT)
    assert registers["a"] == 2

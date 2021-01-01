import advent.aoc2020.day08 as d

EXAMPLE_INPUT = """
nop +0
acc +1
jmp +4
acc +3
jmp -3
acc -99
acc +1
jmp -4
acc +6
""".strip()


def test_a():
    assert d.parta(EXAMPLE_INPUT) == 5


def test_b():
    assert d.partb(EXAMPLE_INPUT) == 8

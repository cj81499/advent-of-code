import aoc_cj.aoc2020.day08 as d

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


def test_part_1():
    assert d.part_1(EXAMPLE_INPUT) == 5


def test_part_2():
    assert d.part_2(EXAMPLE_INPUT) == 8

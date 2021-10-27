import aoc_cj.aoc2020.day14 as d

EXAMPLE_INPUT_0 = """
mask = XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X
mem[8] = 11
mem[7] = 101
mem[8] = 0
""".strip()

EXAMPLE_INPUT_1 = """
mask = 000000000000000000000000000000X1001X
mem[42] = 100
mask = 00000000000000000000000000000000X0XX
mem[26] = 1
""".strip()


def test_a():
    assert d.parta(EXAMPLE_INPUT_0) == 165


def test_b():
    assert d.partb(EXAMPLE_INPUT_1) == 208

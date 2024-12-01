import aoc_cj.aoc2017.day18 as d

EXAMPLE_INPUT_0 = """
set a 1
add a 2
mul a a
mod a 5
snd a
set a 0
rcv a
jgz a -1
set a 1
jgz a -2
""".strip()

EXAMPLE_INPUT_1 = """
snd 1
snd 2
snd p
rcv a
rcv b
rcv c
rcv d
""".strip()


def test_part_1():
    assert d.part_1(EXAMPLE_INPUT_0) == 4


def test_part_2():
    assert d.part_2(EXAMPLE_INPUT_1) == 3

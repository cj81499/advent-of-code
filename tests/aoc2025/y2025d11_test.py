import aoc_cj.aoc2025.day11 as d

EXAMPLE_INPUT_1 = """
aaa: you hhh
you: bbb ccc
bbb: ddd eee
ccc: ddd eee fff
ddd: ggg
eee: out
fff: out
ggg: out
hhh: ccc fff iii
iii: out
""".strip("\n")

EXAMPLE_INPUT_2 = """
svr: aaa bbb
aaa: fft
fft: ccc
bbb: tty
tty: ccc
ccc: ddd eee
ddd: hub
hub: fff
eee: dac
dac: fff
fff: ggg hhh
ggg: out
hhh: out
""".strip("\n")


def test_part_1() -> None:
    assert d.part_1(EXAMPLE_INPUT_1) == 5


def test_part_2() -> None:
    assert d.part_2(EXAMPLE_INPUT_2) == 2

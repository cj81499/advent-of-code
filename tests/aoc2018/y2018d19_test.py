import aoc_cj.aoc2018.day19 as d

EXAMPLE_INPUT = """
# ip 0
seti 5 0 1
seti 6 0 2
addi 0 1 0
addr 1 2 3
setr 1 0 0
seti 8 0 4
seti 9 0 5
""".strip()


def test_a() -> None:
    assert d.parta(EXAMPLE_INPUT) == 7

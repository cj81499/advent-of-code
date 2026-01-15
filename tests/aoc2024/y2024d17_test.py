import aoc_cj.aoc2024.day17 as d

EXAMPLE_INPUT = """
Register A: 729
Register B: 0
Register C: 0

Program: 0,1,5,4,3,0
""".strip()

EXAMPLE_INPUT2 = """
Register A: 2024
Register B: 0
Register C: 0

Program: 0,3,5,4,3,0
""".strip()


def test_part_1() -> None:
    assert d.part_1(EXAMPLE_INPUT) == "4,6,3,5,6,3,5,2,1,0"


def test_part_2() -> None:
    assert d.part_2(EXAMPLE_INPUT2) == 117440

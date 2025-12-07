import aoc_cj.aoc2017.day24 as d

EXAMPLE_INPUT = """
0/2
2/2
2/3
3/4
3/5
0/1
10/1
9/10
""".strip()


def test_part_1() -> None:
    assert d.part_1(EXAMPLE_INPUT) == 31


def test_part_2() -> None:
    assert d.part_2(EXAMPLE_INPUT) == 19

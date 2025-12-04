import aoc_cj.aoc2025.day05 as d

EXAMPLE_INPUT = """
3-5
10-14
16-20
12-18

1
5
8
11
17
32
""".strip()


def test_part_1() -> None:
    assert d.part_1(EXAMPLE_INPUT) == 3


def test_part_2() -> None:
    assert d.part_2(EXAMPLE_INPUT) == 14

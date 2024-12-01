import aoc_cj.aoc2024.day01 as d

EXAMPLE_INPUT = """
3   4
4   3
2   5
1   3
3   9
3   3
""".strip()


def test_part_1() -> None:
    assert d.part_1(EXAMPLE_INPUT) == 11


def test_part_2() -> None:
    assert d.part_2(EXAMPLE_INPUT) == 31

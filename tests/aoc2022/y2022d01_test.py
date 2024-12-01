import aoc_cj.aoc2022.day01 as d

EXAMPLE_INPUT = """
1000
2000
3000

4000

5000
6000

7000
8000
9000

10000
""".strip()


def test_part_1() -> None:
    assert d.part_1(EXAMPLE_INPUT) == 24000


def test_part_2() -> None:
    assert d.part_2(EXAMPLE_INPUT) == 45000

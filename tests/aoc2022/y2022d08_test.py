import aoc_cj.aoc2022.day08 as d

EXAMPLE_INPUT = """
30373
25512
65332
33549
35390
""".strip()


def test_a() -> None:
    assert d.parta(EXAMPLE_INPUT) == 21


def test_b() -> None:
    assert d.partb(EXAMPLE_INPUT) == 8

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


def test_a() -> None:
    assert d.parta(EXAMPLE_INPUT) == 24000


def test_b() -> None:
    assert d.partb(EXAMPLE_INPUT) == 45000

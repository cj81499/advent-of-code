import aoc_cj.aoc2022.day18 as d

EXAMPLE_INPUT_1 = """
1,1,1
2,1,1
""".strip()

EXAMPLE_INPUT_2 = """
2,2,2
1,2,2
3,2,2
2,1,2
2,3,2
2,2,1
2,2,3
2,2,4
2,2,6
1,2,5
3,2,5
2,1,5
2,3,5
""".strip()


def test_a() -> None:
    assert d.parta(EXAMPLE_INPUT_1) == 10
    assert d.parta(EXAMPLE_INPUT_2) == 64


def test_b() -> None:
    assert d.partb(EXAMPLE_INPUT_1) == 10
    assert d.partb(EXAMPLE_INPUT_2) == 58

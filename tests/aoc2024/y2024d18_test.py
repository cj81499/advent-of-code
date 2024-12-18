import aoc_cj.aoc2024.day18 as d

EXAMPLE_INPUT = """
5,4
4,2
4,5
3,0
2,1
6,3
2,4
1,5
0,6
3,3
2,6
5,1
1,2
5,5
2,5
6,5
1,4
0,4
6,4
1,1
6,1
1,0
0,5
1,6
2,0
""".strip()


def test_part_1() -> None:
    assert d.part_1(EXAMPLE_INPUT, max_dim=6, simulate=12) == 22


def test_part_2() -> None:
    assert d.part_2(EXAMPLE_INPUT, max_dim=6) == "6,1"

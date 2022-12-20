import aoc_cj.aoc2022.day20 as d

EXAMPLE_INPUT = """
1
2
-3
3
-2
0
4
""".strip()


def test_a() -> None:
    assert d.parta(EXAMPLE_INPUT) == 3


# @pytest.mark.skip("unimplemented")
def test_b() -> None:
    assert d.partb(EXAMPLE_INPUT) == 1623178306

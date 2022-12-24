import aoc_cj.aoc2022.day24 as d

EXAMPLE_INPUT = """
#.######
#>>.<^<#
#.<..<<#
#>v.><>#
#<^v^^>#
######.#
""".strip()


def test_a() -> None:
    assert d.parta(EXAMPLE_INPUT) == 18


def test_b() -> None:
    assert d.partb(EXAMPLE_INPUT) == 54

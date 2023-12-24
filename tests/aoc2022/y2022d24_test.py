import aoc_cj.aoc2022.day24 as d

EXAMPLE_INPUT = """
#.######
#>>.<^<#
#.<..<<#
#>v.><>#
#<^v^^>#
######.#
""".strip()


def test_part_1() -> None:
    assert d.part_1(EXAMPLE_INPUT) == 18


def test_part_2() -> None:
    assert d.part_2(EXAMPLE_INPUT) == 54

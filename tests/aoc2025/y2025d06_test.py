import aoc_cj.aoc2025.day06 as d

EXAMPLE_INPUT = """
123 328  51 64 
 45 64  387 23 
  6 98  215 314
*   +   *   +  
""".strip("\n")  # noqa: W291


def test_part_1() -> None:
    assert d.part_1(EXAMPLE_INPUT) == 4277556


def test_part_2() -> None:
    assert d.part_2(EXAMPLE_INPUT) == 3263827

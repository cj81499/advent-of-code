import aoc_cj.aoc2018.day16 as d

EXAMPLE_INPUT = """
Before: [3, 2, 1, 1]
9 2 1 2
After:  [3, 2, 2, 1]



IGNORE ME
""".strip()


def test_part_1() -> None:
    assert d.part_1(EXAMPLE_INPUT) == 1

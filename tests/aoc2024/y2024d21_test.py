import aoc_cj.aoc2024.day21 as d

EXAMPLE_INPUT = """
029A
980A
179A
456A
379A
""".strip()


def test_part_1() -> None:
    assert d.part_1(EXAMPLE_INPUT) == 126384

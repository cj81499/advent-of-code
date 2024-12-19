import aoc_cj.aoc2024.day19 as d

EXAMPLE_INPUT = """
r, wr, b, g, bwu, rb, gb, br

brwrr
bggr
gbbr
rrbgbr
ubwu
bwurrg
brgr
bbrgwb
""".strip()


def test_part_1() -> None:
    assert d.part_1(EXAMPLE_INPUT) == 6


def test_part_2() -> None:
    assert d.part_2(EXAMPLE_INPUT) == 16

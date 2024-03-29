import aoc_cj.aoc2020.day02 as d

EXAMPLE_INPUT = """
1-3 a: abcde
1-3 b: cdefg
2-9 c: ccccccccc
""".strip()


def test_part_1():
    assert 2 == d.part_1(EXAMPLE_INPUT)


def test_part_2():
    assert 1 == d.part_2(EXAMPLE_INPUT)

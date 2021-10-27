import aoc_cj.aoc2020.day02 as d

EXAMPLE_INPUT = """
1-3 a: abcde
1-3 b: cdefg
2-9 c: ccccccccc
""".strip()


def test_a():
    assert 2 == d.parta(EXAMPLE_INPUT)


def test_b():
    assert 1 == d.partb(EXAMPLE_INPUT)

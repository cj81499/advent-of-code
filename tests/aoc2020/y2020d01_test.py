import aoc_cj.aoc2020.day01 as d

EXAMPLE_INPUT = """
1721
979
366
299
675
1456
""".strip()


def test_part_1():
    assert 514579 == d.part_1(EXAMPLE_INPUT)


def test_part_2():
    assert 241861950 == d.part_2(EXAMPLE_INPUT)

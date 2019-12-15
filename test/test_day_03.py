import src.day_03 as d

INPUT_0 = """R8,U5,L5,D3
U7,R6,D4,L4""".splitlines()


INPUT_1 = """R75,D30,R83,U83,L12,D49,R71,U7,L72
U62,R66,U55,R34,D71,R55,D58,R83 """.splitlines()


INPUT_2 = """R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51
U98,R91,D20,R16,D67,R40,U7,R15,U6,R7""".splitlines()


def test_day_03_part1_0():
    assert d.part1(INPUT_0) == 6


def test_day_03_part1_1():
    assert d.part1(INPUT_1) == 159


def test_day_03_part1_2():
    assert d.part1(INPUT_2) == 135


def test_day_03_part2_0():
    assert d.part2(INPUT_0) == 30


def test_day_03_part2_1():
    assert d.part2(INPUT_1) == 610


def test_day_03_part2_2():
    assert d.part2(INPUT_2) == 410

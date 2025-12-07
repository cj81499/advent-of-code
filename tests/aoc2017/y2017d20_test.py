import aoc_cj.aoc2017.day20 as d

EXAMPLE_INPUT_0 = """
p=< 3,0,0>, v=< 2,0,0>, a=<-1,0,0>
p=< 4,0,0>, v=< 0,0,0>, a=<-2,0,0>
""".strip()

EXAMPLE_INPUT_1 = """
p=<-6,0,0>, v=< 3,0,0>, a=< 0,0,0>
p=<-4,0,0>, v=< 2,0,0>, a=< 0,0,0>
p=<-2,0,0>, v=< 1,0,0>, a=< 0,0,0>
p=< 3,0,0>, v=<-1,0,0>, a=< 0,0,0>
""".strip()


def test_part_1() -> None:
    assert d.part_1(EXAMPLE_INPUT_0) == 0


def test_part_2() -> None:
    assert d.part_2(EXAMPLE_INPUT_1) == 1

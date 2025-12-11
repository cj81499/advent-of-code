import aoc_cj.aoc2017.day16 as d

EXAMPLE_INPUT = "s1,x3/4,pe/b"


def test_part_1() -> None:
    assert d.part_1(EXAMPLE_INPUT, num_programs=5) == "baedc"


def test_part_2() -> None:
    assert d.part_1(EXAMPLE_INPUT, num_programs=5, repetitions=2) == "ceadb"

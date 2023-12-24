import aoc_cj.aoc2023.day15 as d

EXAMPLE_INPUT = """
rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7
""".strip()


def test_part_1() -> None:
    assert d.part_1(EXAMPLE_INPUT) == 1320


def test_part_2() -> None:
    assert d.part_2(EXAMPLE_INPUT) == 145

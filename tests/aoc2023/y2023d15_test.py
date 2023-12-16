import aoc_cj.aoc2023.day15 as d

EXAMPLE_INPUT = """
rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7
""".strip()


def test_a() -> None:
    assert d.parta(EXAMPLE_INPUT) == 1320


def test_b() -> None:
    assert d.partb(EXAMPLE_INPUT) == 145

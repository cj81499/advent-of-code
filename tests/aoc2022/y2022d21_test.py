import aoc_cj.aoc2022.day21 as d

EXAMPLE_INPUT = """
root: pppw + sjmn
dbpl: 5
cczh: sllz + lgvd
zczc: 2
ptdq: humn - dvpt
dvpt: 3
lfqf: 4
humn: 5
ljgn: 2
sjmn: drzm * dbpl
sllz: 4
pppw: cczh / lfqf
lgvd: ljgn * ptdq
drzm: hmdt - zczc
hmdt: 32
""".strip()


def test_part_1() -> None:
    assert d.part_1(EXAMPLE_INPUT) == 152


def test_part_2() -> None:
    assert d.part_2(EXAMPLE_INPUT) == 301

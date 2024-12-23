import aoc_cj.aoc2024.day23 as d

EXAMPLE_INPUT = """
kh-tc
qp-kh
de-cg
ka-co
yn-aq
qp-ub
cg-tb
vc-aq
tb-ka
wh-tc
yn-cg
kh-ub
ta-co
de-co
tc-td
tb-wq
wh-td
ta-ka
td-qp
aq-cg
wq-ub
ub-vc
de-ta
wq-aq
wq-vc
wh-yn
ka-de
kh-ta
co-tc
wh-qp
tb-vc
td-yn
""".strip()


def test_part_1() -> None:
    assert d.part_1(EXAMPLE_INPUT) == 7


def test_part_2() -> None:
    assert d.part_2(EXAMPLE_INPUT) == "co,de,ka,ta"

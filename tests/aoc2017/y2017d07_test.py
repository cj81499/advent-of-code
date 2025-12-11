import aoc_cj.aoc2017.day07 as d

EXAMPLE_INPUT = """
pbga (66)
xhth (57)
ebii (61)
havc (66)
ktlj (57)
fwft (72) -> ktlj, cntj, xhth
qoyq (66)
padx (45) -> pbga, havc, qoyq
tknk (41) -> ugml, padx, fwft
jptl (61)
ugml (68) -> gyxo, ebii, jptl
gyxo (61)
cntj (57)
""".strip()


def test_part_1() -> None:
    assert d.part_1(EXAMPLE_INPUT) == "tknk"


def test_part_2() -> None:
    assert d.part_2(EXAMPLE_INPUT) == 60

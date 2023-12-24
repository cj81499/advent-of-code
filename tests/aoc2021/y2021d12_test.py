import aoc_cj.aoc2021.day12 as d

EXAMPLE_INPUT_1 = """
start-A
start-b
A-c
A-b
b-d
A-end
b-end
""".strip()

EXAMPLE_INPUT_2 = """
dc-end
HN-start
start-kj
dc-start
dc-HN
LN-dc
HN-end
kj-sa
kj-HN
kj-dc
""".strip()

EXAMPLE_INPUT_3 = """
fs-end
he-DX
fs-he
start-DX
pj-DX
end-zg
zg-sl
zg-pj
pj-he
RW-he
fs-DX
pj-RW
zg-RW
start-pj
he-WI
zg-he
pj-fs
start-RW
""".strip()


def test_part_1():
    assert d.part_1(EXAMPLE_INPUT_1) == 10
    assert d.part_1(EXAMPLE_INPUT_2) == 19
    assert d.part_1(EXAMPLE_INPUT_3) == 226


def test_part_2():
    assert d.part_2(EXAMPLE_INPUT_1) == 36
    assert d.part_2(EXAMPLE_INPUT_2) == 103
    assert d.part_2(EXAMPLE_INPUT_3) == 3509

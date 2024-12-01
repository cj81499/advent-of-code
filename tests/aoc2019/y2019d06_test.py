import aoc_cj.aoc2019.day06 as d

EXAMPLE_0 = """
COM)B
B)C
C)D
D)E
E)F
B)G
G)H
D)I
E)J
J)K
K)L
""".strip()


EXAMPLE_1 = """
COM)B
B)C
C)D
D)E
E)F
B)G
G)H
D)I
E)J
J)K
K)L
K)YOU
I)SAN
""".strip()


def test_part_1() -> None:
    assert d.part_1(EXAMPLE_0) == 42


def test_part_2() -> None:
    assert d.part_2(EXAMPLE_1) == 4

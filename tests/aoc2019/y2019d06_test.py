import advent.aoc2019.day06 as d

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


def test_parta() -> None:
    assert d.parta(EXAMPLE_0) == 42


def test_partb() -> None:
    assert d.partb(EXAMPLE_1) == 4

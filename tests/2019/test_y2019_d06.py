import y2019_d06 as d

EXAMPLE_0 = """COM)B
B)C
C)D
D)E
E)F
B)G
G)H
D)I
E)J
J)K
K)L""".splitlines()

EXAMPLE_1 = """COM)B
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
I)SAN""".splitlines()


def test_parta() -> None:
    assert d.parta(EXAMPLE_0) == 42


def test_partb() -> None:
    assert d.partb(EXAMPLE_1) == 4

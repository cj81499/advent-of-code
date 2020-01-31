import src.day_06 as d

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


def test_part1() -> None:
    assert d.part1(EXAMPLE_0) == 42


def test_part2() -> None:
    assert d.part2(EXAMPLE_1) == 4

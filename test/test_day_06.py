import path_fix
import day_06

INPUT_1 = """COM)B
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

INPUT_2 = """COM)B
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


def test_day_06_part1_0():
    assert day_06.part1(INPUT_1) == 42


def test_day_06_part2_0():
    assert day_06.part2(INPUT_2) == 4

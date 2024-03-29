import aoc_cj.aoc2018.day24 as d

EXAMPLE_INPUT = """
Immune System:
17 units each with 5390 hit points (weak to radiation, bludgeoning) with an attack that does 4507 fire damage at initiative 2
989 units each with 1274 hit points (immune to fire; weak to bludgeoning, slashing) with an attack that does 25 slashing damage at initiative 3

Infection:
801 units each with 4706 hit points (weak to radiation) with an attack that does 116 bludgeoning damage at initiative 1
4485 units each with 2961 hit points (immune to radiation; weak to fire, cold) with an attack that does 12 slashing damage at initiative 4
""".strip()


def test_part_1():
    assert d.part_1(EXAMPLE_INPUT) == 5216


def test_part_2():
    assert d.part_2(EXAMPLE_INPUT) == 51

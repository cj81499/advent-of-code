import unittest

import advent.aoc2018.day24 as day24

s = """
Immune System:
17 units each with 5390 hit points (weak to radiation, bludgeoning) with an attack that does 4507 fire damage at initiative 2
989 units each with 1274 hit points (immune to fire; weak to bludgeoning, slashing) with an attack that does 25 slashing damage at initiative 3

Infection:
801 units each with 4706 hit points (weak to radiation) with an attack that does 116 bludgeoning damage at initiative 1
4485 units each with 2961 hit points (immune to radiation; weak to fire, cold) with an attack that does 12 slashing damage at initiative 4
"""


class TestDay24(unittest.TestCase):
    def test_day24_parta(self):
        self.assertEqual(5216, day24.Battle.parseBattle(s).fight()[1])

    def test_day24_partb(self):
        self.assertEqual(51, day24.remaining_immune_with_min_boost(s))


if __name__ == "__main__":
    unittest.main()

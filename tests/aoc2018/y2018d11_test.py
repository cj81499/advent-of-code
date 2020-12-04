import unittest

import advent.aoc2018.day11 as day11


class TestDay11(unittest.TestCase):
    def test_day11_power_level_0(self):
        self.assertEqual(4, day11.power_level(3, 5, 8))

    def test_day11_power_level_1(self):
        self.assertEqual(-5, day11.power_level(122, 79, 57))

    def test_day11_power_level_2(self):
        self.assertEqual(0, day11.power_level(217, 196, 39))

    def test_day11_power_level_3(self):
        self.assertEqual(4, day11.power_level(101, 153, 71))

    def test_day11_parta_0(self):
        self.assertEqual("33,45", day11.parta(18))

    def test_day11_parta_1(self):
        self.assertEqual("21,61", day11.parta(42))

    # Unpolished day 11 runs super slow
    # def test_day11_partb_0(self):
    #     self.assertEqual("90,269,16", day11.partb(18))

    # def test_day11_partb_1(self):
    #     self.assertEqual("232,251,12", day11.partb(42))

    def test_day11_partb_polished_0(self):
        self.assertEqual("90,269,16", day11.partb_polished(18))

    def test_day11_partb_polished_1(self):
        self.assertEqual("232,251,12", day11.partb_polished(42))


if __name__ == "__main__":
    unittest.main()

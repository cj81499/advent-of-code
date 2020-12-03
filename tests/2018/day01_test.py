import unittest

import day01


class TestDay01(unittest.TestCase):
    def test_day01_parta_0(self):
        self.assertEqual(3, day01.parta([+1, -2, +3, +1]))

    def test_day01_parta_1(self):
        self.assertEqual(3, day01.parta([+1, +1, +1]))

    def test_day01_parta_2(self):
        self.assertEqual(0, day01.parta([+1, +1, -2]))

    def test_day01_parta_3(self):
        self.assertEqual(-6, day01.parta([-1, -2, -3]))

    def test_day01_partb_0(self):
        self.assertEqual(2, day01.partb([+1, -2, +3, +1]))

    def test_day01_partb_1(self):
        self.assertEqual(0, day01.partb([+1, -1]))

    def test_day01_partb_2(self):
        self.assertEqual(10, day01.partb([+3, +3, +4, -2, -4]))

    def test_day01_partb_3(self):
        self.assertEqual(5, day01.partb([-6, +3, +8, +5, -6]))

    def test_day01_partb_4(self):
        self.assertEqual(14, day01.partb([+7, +7, -2, -7, -4]))


if __name__ == "__main__":
    unittest.main()

import unittest

import day02


class TestDay02(unittest.TestCase):
    def test_day02_part1(self):
        self.assertEqual(58, day02.part1(["2x3x4"]))
        self.assertEqual(43, day02.part1(["1x1x10"]))

    def test_day02_part2(self):
        self.assertEqual(34, day02.part2(["2x3x4"]))
        self.assertEqual(14, day02.part2(["1x1x10"]))


if __name__ == "__main__":
    unittest.main()

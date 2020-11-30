import unittest

import day05


class TestDay05(unittest.TestCase):
    def test_day05_part1(self):
        self.assertEqual(10, day05.part1("dabAcCaCBAcCcaDA"))

    def test_day05_part2(self):
        self.assertEqual(4, day05.part2("dabAcCaCBAcCcaDA"))

    def test_day05_part2_polished(self):
        self.assertEqual(4, day05.part2_polished("dabAcCaCBAcCcaDA"))


if __name__ == "__main__":
    unittest.main()

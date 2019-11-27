import unittest

import day03


class TestDay03(unittest.TestCase):
    def test_day03_part1(self):
        self.assertEqual(2, day03.part1(">"))
        self.assertEqual(4, day03.part1("^>v<"))
        self.assertEqual(2, day03.part1("^v^v^v^v^v"))

    def test_day03_part2(self):
        self.assertEqual(3, day03.part2("^v"))
        self.assertEqual(3, day03.part2("^>v<"))
        self.assertEqual(11, day03.part2("^v^v^v^v^v"))


if __name__ == "__main__":
    unittest.main()

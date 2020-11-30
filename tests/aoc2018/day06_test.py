import unittest

import day06

lines = """1, 1
1, 6
8, 3
3, 4
5, 5
8, 9""".split("\n")


class TestDay06(unittest.TestCase):
    def test_day06_part1(self):
        self.assertEqual(17, day06.part1(lines))

    def test_day06_part2(self):
        self.assertEqual(16, day06.part2(lines, 32))


if __name__ == "__main__":
    unittest.main()

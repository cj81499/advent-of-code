import unittest

import advent.aoc2018.day06 as day06

lines = """1, 1
1, 6
8, 3
3, 4
5, 5
8, 9""".split("\n")


class TestDay06(unittest.TestCase):
    def test_day06_parta(self):
        self.assertEqual(17, day06.parta(lines))

    def test_day06_partb(self):
        self.assertEqual(16, day06.partb(lines, 32))


if __name__ == "__main__":
    unittest.main()

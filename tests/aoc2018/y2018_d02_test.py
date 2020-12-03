import unittest

import advent.aoc2018.day02 as day02


class TestDay02(unittest.TestCase):
    def test_day02_parta(self):
        self.assertEqual(12, day02.parta(
            ["abcdef", "bababc", "abbcde", "abcccd", "aabcdd", "abcdee", "ababab"]))

    def test_day02_partb(self):
        self.assertEqual("fgij", day02.partb(
            ["abcde", "fghij", "klmno", "pqrst", "fguij", "axcye", "wvxyz"]))


if __name__ == "__main__":
    unittest.main()

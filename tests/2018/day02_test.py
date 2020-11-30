import unittest

import day02


class TestDay02(unittest.TestCase):
    def test_day02_part1(self):
        self.assertEqual(12, day02.part1(
            ["abcdef", "bababc", "abbcde", "abcccd", "aabcdd", "abcdee", "ababab"]))

    def test_day02_part2(self):
        self.assertEqual("fgij", day02.part2(
            ["abcde", "fghij", "klmno", "pqrst", "fguij", "axcye", "wvxyz"]))


if __name__ == "__main__":
    unittest.main()

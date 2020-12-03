import unittest

import advent.aoc2018.day08 as day08

s = "2 3 0 3 10 11 12 1 1 0 1 99 2 1 1 2"


class TestDay08(unittest.TestCase):
    def test_day08_parta(self):
        self.assertEqual(138, day08.parta(s))

    def test_day08_partb(self):
        self.assertEqual(66, day08.partb(s))


if __name__ == "__main__":
    unittest.main()

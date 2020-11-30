import unittest

import day08

s = "2 3 0 3 10 11 12 1 1 0 1 99 2 1 1 2"


class TestDay08(unittest.TestCase):
    def test_day08_part1(self):
        self.assertEqual(138, day08.part1(s))

    def test_day08_part2(self):
        self.assertEqual(66, day08.part2(s))


if __name__ == "__main__":
    unittest.main()

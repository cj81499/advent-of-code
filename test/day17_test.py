import unittest

import path_fix
import day17


class TestDay17(unittest.TestCase):
    def test_day17_part1(self):
        self.assertEqual(4, day17.part1(25, ["20", "15", "10", "5", "5"]))

    def test_day17_part2(self):
        self.assertEqual(3, day17.part2(25, ["20", "15", "10", "5", "5"]))


if __name__ == "__main__":
    unittest.main()

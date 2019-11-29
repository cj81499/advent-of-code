import unittest

import path_fix
import day09


class TestDay09(unittest.TestCase):
    def test_day09_part1(self):
        lines = """London to Dublin = 464
London to Belfast = 518
Dublin to Belfast = 141""".splitlines()
        self.assertEqual(605, day09.find_paths(lines)[0])

    def test_day09_part2(self):
        lines = """London to Dublin = 464
London to Belfast = 518
Dublin to Belfast = 141""".splitlines()
        self.assertEqual(982, day09.find_paths(lines)[1])


if __name__ == "__main__":
    unittest.main()

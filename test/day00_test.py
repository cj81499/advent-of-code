import unittest

import path_fix
import day00


class TestDay00(unittest.TestCase):
    def test_day00_part1(self):
        self.assertEqual(None, day00.part1("", []))

    def test_day00_part2(self):
        self.assertEqual(None, day00.part2("", []))


if __name__ == "__main__":
    unittest.main()

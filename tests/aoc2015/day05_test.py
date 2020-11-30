import unittest

import path_fix
import day05


class TestDay05(unittest.TestCase):
    def test_day05_part1(self):
        self.assertTrue(day05.is_nice1("ugknbfddgicrmopn"))
        self.assertTrue(day05.is_nice1("aaa"))
        self.assertFalse(day05.is_nice1("jchzalrnumimnmhp"))
        self.assertFalse(day05.is_nice1("haegwjzuvuyypxyu"))
        self.assertFalse(day05.is_nice1("dvszwmarrgswjxmb"))

    def test_day05_part2(self):
        self.assertTrue(day05.is_nice2("qjhvhtzxzqqjkmpb"))
        self.assertTrue(day05.is_nice2("xxyxx"))
        self.assertFalse(day05.is_nice2("uurcxstgmygtbstg"))
        self.assertFalse(day05.is_nice2("ieodomkazucvgmuy"))


if __name__ == "__main__":
    unittest.main()

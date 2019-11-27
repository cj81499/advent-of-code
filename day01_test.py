import unittest

import day01


class TestDay01(unittest.TestCase):
    def test_day01_part1(self):
        self.assertEqual(0, day01.part1("(())"))
        self.assertEqual(0, day01.part1("()()"))

        self.assertEqual(3, day01.part1("((("))
        self.assertEqual(3, day01.part1("(()(()("))
        self.assertEqual(3, day01.part1("))((((("))

        self.assertEqual(-1, day01.part1("())"))
        self.assertEqual(-1, day01.part1("))("))

        self.assertEqual(-3, day01.part1(")))"))
        self.assertEqual(-3, day01.part1(")())())"))

        self.assertEqual(-3, day01.part1(")))"))
        self.assertEqual(-3, day01.part1(")())())"))

    def test_day01_part2(self):
        self.assertEqual(1, day01.part2(")"))
        self.assertEqual(5, day01.part2("()())"))


if __name__ == "__main__":
    unittest.main()

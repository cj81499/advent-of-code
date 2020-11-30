import unittest

import day14


class TestDay14(unittest.TestCase):
    def test_day14_part1_0(self):
        self.assertEqual("5158916779", day14.part1("9"))

    def test_day14_part1_1(self):
        self.assertEqual("0124515891", day14.part1("5"))

    def test_day14_part1_2(self):
        self.assertEqual("9251071085", day14.part1("18"))

    def test_day14_part1_3(self):
        self.assertEqual("5941429882", day14.part1("2018"))

    def test_day14_part2_0(self):
        self.assertEqual(9, day14.part2("51589"))

    def test_day14_part2_1(self):
        self.assertEqual(5, day14.part2("01245"))

    def test_day14_part2_2(self):
        self.assertEqual(18, day14.part2("92510"))

    def test_day14_part2_3(self):
        self.assertEqual(2018, day14.part2("59414"))


if __name__ == "__main__":
    unittest.main()

import unittest

import day14


class TestDay14(unittest.TestCase):
    def test_day14_parta_0(self):
        self.assertEqual("5158916779", day14.parta("9"))

    def test_day14_parta_1(self):
        self.assertEqual("0124515891", day14.parta("5"))

    def test_day14_parta_2(self):
        self.assertEqual("9251071085", day14.parta("18"))

    def test_day14_parta_3(self):
        self.assertEqual("5941429882", day14.parta("2018"))

    def test_day14_partb_0(self):
        self.assertEqual(9, day14.partb("51589"))

    def test_day14_partb_1(self):
        self.assertEqual(5, day14.partb("01245"))

    def test_day14_partb_2(self):
        self.assertEqual(18, day14.partb("92510"))

    def test_day14_partb_3(self):
        self.assertEqual(2018, day14.partb("59414"))


if __name__ == "__main__":
    unittest.main()

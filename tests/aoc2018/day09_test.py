import unittest

import day09


class TestDay09(unittest.TestCase):
    def test_day09_0(self):
        self.assertEqual(32, day09.run(9, 25))

    def test_day09_1(self):
        self.assertEqual(8317, day09.run(10, 1618))

    def test_day09_2(self):
        self.assertEqual(146373, day09.run(13, 7999))

    def test_day09_3(self):
        self.assertEqual(2764, day09.run(17, 1104))

    def test_day09_4(self):
        self.assertEqual(54718, day09.run(21, 6111))

    def test_day09_5(self):
        self.assertEqual(37305, day09.run(30, 5807))

    def test_day09_polished_0(self):
        self.assertEqual(32, day09.run_polished(9, 25))

    def test_day09_polished_1(self):
        self.assertEqual(8317, day09.run_polished(10, 1618))

    def test_day09_polished_2(self):
        self.assertEqual(146373, day09.run_polished(13, 7999))

    def test_day09_polished_3(self):
        self.assertEqual(2764, day09.run_polished(17, 1104))

    def test_day09_polished_4(self):
        self.assertEqual(54718, day09.run_polished(21, 6111))

    def test_day09_polished_5(self):
        self.assertEqual(37305, day09.run_polished(30, 5807))


if __name__ == "__main__":
    unittest.main()

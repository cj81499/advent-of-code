import unittest

import day03
import day03_polished

s = ["#1 @ 1,3: 4x4", "#2 @ 3,1: 4x4", "#3 @ 5,5: 2x2"]

claims = [day03_polished.Claim(x) for x in s]


class TestDay03(unittest.TestCase):
    def test_day03_parta(self):
        self.assertEqual(4, day03.parta(s))

    def test_day03_partb(self):
        self.assertEqual(3, day03.partb(s))

    def test_day03_polished_parta(self):
        self.assertEqual(4, day03_polished.parta(claims))

    def test_day03_polished_partb(self):
        self.assertEqual(3, day03_polished.partb(claims))


if __name__ == "__main__":
    unittest.main()

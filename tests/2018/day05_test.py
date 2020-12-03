import unittest

import day05


class TestDay05(unittest.TestCase):
    def test_day05_parta(self):
        self.assertEqual(10, day05.parta("dabAcCaCBAcCcaDA"))

    def test_day05_partb(self):
        self.assertEqual(4, day05.partb("dabAcCaCBAcCcaDA"))

    def test_day05_partb_polished(self):
        self.assertEqual(4, day05.partb_polished("dabAcCaCBAcCcaDA"))


if __name__ == "__main__":
    unittest.main()

import unittest

import day04


class TestDay04(unittest.TestCase):
    def test_day04(self):
        self.assertEqual(609043, day04.part1("abcdef"))
        self.assertEqual(1048970, day04.part1("pqrstuv"))


if __name__ == "__main__":
    unittest.main()

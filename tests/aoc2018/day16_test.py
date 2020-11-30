import unittest

import day16


class TestDay16(unittest.TestCase):
    def test_day16_part1(self):
        self.assertEqual(1, day16.part1("""Before: [3, 2, 1, 1]
9 2 1 2
After:  [3, 2, 2, 1]"""))


if __name__ == "__main__":
    unittest.main()

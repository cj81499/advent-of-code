import unittest

import day08


class TestDay08(unittest.TestCase):
    def test_day08_part1(self):
        self.assertEqual("", day08.decode("\"\""))
        self.assertEqual("abc", day08.decode("\"abc\""))
        self.assertEqual("aaa\"aaa", day08.decode("\"aaa\\\"aaa\""))
        self.assertEqual("'", day08.decode("\"\\x27\""))

    def test_day08_part2(self):
        self.assertEqual("\"\\\"\\\"\"", day08.encode("\"\""))
        self.assertEqual("\"\\\"abc\\\"\"", day08.encode("\"abc\""))
        self.assertEqual("\"\\\"aaa\\\\\\\"aaa\\\"\"", day08.encode("\"aaa\\\"aaa\""))
        self.assertEqual("\"\\\"\\\\x27\\\"\"", day08.encode("\"\\x27\""))


if __name__ == "__main__":
    unittest.main()

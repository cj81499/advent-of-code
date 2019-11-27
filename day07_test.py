import unittest

import day07


class TestDay07(unittest.TestCase):
    def test_day07(self):
        input_str = """123 -> x
456 -> y
x AND y -> d
x OR y -> e
x LSHIFT 2 -> f
y RSHIFT 2 -> g
NOT x -> h
NOT y -> i"""

        expected = {"d": 72, "e": 507, "f": 492, "g": 114, "h": 65412, "i": 65079, "x": 123, "y": 456}
        ans = day07.part1(input_str.splitlines())

        self.assertEqual(expected, ans)


if __name__ == "__main__":
    unittest.main()

import unittest

import day13


class TestDay13(unittest.TestCase):
    def test_day13_part1(self):
        lines = "/->-\\        \n|   |  /----\\\n| /-+--+-\\  |\n| | |  | v  |\n\\-+-/  \\-+--/\n  \\------/   ".split("\n")  # noqa
        self.assertEqual((7, 3), day13.part1(lines))

    def test_day13_part2(self):
        lines = "/>-<\\  \n|   |  \n| /<+-\\\n| | | v\n\\>+</ |\n  |   ^\n  \\<->/".split("\n")
        self.assertEqual((6, 4), day13.part2(lines))


if __name__ == "__main__":
    unittest.main()

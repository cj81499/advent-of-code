import unittest

import advent.aoc2018.day13 as day13


class TestDay13(unittest.TestCase):
    def test_day13_parta(self):
        lines = "/->-\\        \n|   |  /----\\\n| /-+--+-\\  |\n| | |  | v  |\n\\-+-/  \\-+--/\n  \\------/   ".splitlines()
        self.assertEqual((7, 3), day13.parta(lines))

    def test_day13_partb(self):
        lines = "/>-<\\  \n|   |  \n| /<+-\\\n| | | v\n\\>+</ |\n  |   ^\n  \\<->/".splitlines()
        self.assertEqual((6, 4), day13.partb(lines))


if __name__ == "__main__":
    unittest.main()

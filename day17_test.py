import day17
import unittest

lines = """
x=495, y=2..7
y=7, x=495..501
x=501, y=3..7
x=498, y=2..4
x=506, y=1..2
x=498, y=10..13
x=504, y=10..13
y=13, x=498..504
""".strip().split("\n")


class TestDay17(unittest.TestCase):
    def test_day17_part1(self):
        self.assertEqual(57, day17.part1(lines))

    def test_day17_part2(self):
        self.assertEqual(29, day17.part2(lines))


if __name__ == "__main__":
    unittest.main()

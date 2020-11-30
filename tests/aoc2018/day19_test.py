import unittest
import day19

lines = """
seti 5 0 1
seti 6 0 2
addi 0 1 0
addr 1 2 3
setr 1 0 0
seti 8 0 4
seti 9 0 5
""".strip().split("\n")


class TestDay19(unittest.TestCase):

    def test_day19_part1(self):
        self.assertEqual(7, day19.part1(lines, 0))


if __name__ == "__main__":
    unittest.main()

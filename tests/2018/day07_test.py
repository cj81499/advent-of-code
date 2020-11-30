import unittest

import day07

input_lines = """Step C must be finished before step A can begin.
Step C must be finished before step F can begin.
Step A must be finished before step B can begin.
Step A must be finished before step D can begin.
Step B must be finished before step E can begin.
Step D must be finished before step E can begin.
Step F must be finished before step E can begin.""".split("\n")


class TestDay07(unittest.TestCase):
    def test_day07_part1(self):
        self.assertEqual("CABDFE", day07.part1(input_lines))

    def test_day07_part2(self):
        self.assertEqual(15, day07.part2(input_lines, 0, 1))


if __name__ == "__main__":
    unittest.main()

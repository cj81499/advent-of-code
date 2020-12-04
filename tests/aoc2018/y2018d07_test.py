import unittest

import advent.aoc2018.day07 as day07

input_lines = """Step C must be finished before step A can begin.
Step C must be finished before step F can begin.
Step A must be finished before step B can begin.
Step A must be finished before step D can begin.
Step B must be finished before step E can begin.
Step D must be finished before step E can begin.
Step F must be finished before step E can begin.""".split("\n")


class TestDay07(unittest.TestCase):
    def test_day07_parta(self):
        self.assertEqual("CABDFE", day07.parta(input_lines))

    def test_day07_partb(self):
        self.assertEqual(15, day07.partb(input_lines, 0, 1))


if __name__ == "__main__":
    unittest.main()

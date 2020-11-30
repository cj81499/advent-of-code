import unittest
from collections import deque

import day23


def str_to_swarm(s):
    nanobots = deque()
    for line in s.strip().split("\n"):
        x, y, z, r = day23.parser.parse(line).fixed
        nanobots.append(day23.Nanobot(day23.Point(x, y, z), r))
    return day23.Swarm(nanobots)


class TestDay23(unittest.TestCase):
    def test_day23_part1(self):
        s = """
pos=<0,0,0>, r=4
pos=<1,0,0>, r=1
pos=<4,0,0>, r=3
pos=<0,2,0>, r=1
pos=<0,5,0>, r=3
pos=<0,0,3>, r=1
pos=<1,1,1>, r=1
pos=<1,1,2>, r=1
pos=<1,3,1>, r=1
"""

        self.assertEqual(7, str_to_swarm(s).in_range_of_strongest())

    def test_day23_part2(self):
        s = """
pos=<10,12,12>, r=2
pos=<12,14,12>, r=2
pos=<16,12,12>, r=4
pos=<14,14,14>, r=6
pos=<50,50,50>, r=200
pos=<10,10,10>, r=5
"""

        self.assertEqual(36, day23.Point.manhattan_dist(str_to_swarm(
            s).coords_in_range_of_most_bots(), day23.Point.ORIGIN))


if __name__ == "__main__":
    unittest.main()

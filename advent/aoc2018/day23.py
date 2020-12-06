from collections import deque
from dataclasses import dataclass
from functools import total_ordering

import parse

parser = parse.compile("pos=<{:d},{:d},{:d}>, r={:d}")


@dataclass
@total_ordering
class Point:
    x: int
    y: int
    z: int

    @staticmethod
    def manhattan_dist(p0, p1):
        return abs(p0.x - p1.x) + abs(p0.y - p1.y) + abs(p0.z - p1.z)

    def __hash__(self):
        return hash((self.x, self.y, self.z))

    def __eq__(self, other):
        return (self.x, self.y, self.z) == (other.x, other.y, other.z)

    def __lt__(self, other):
        return Point.manhattan_dist(self, Point.ORIGIN) < Point.manhattan_dist(other, Point.ORIGIN)

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y, self.z + other.z)

    def adjacent(self):
        return set([self + transform for transform in Point.TRANSFORMS])


Point.ORIGIN = Point(0, 0, 0)
Point.UP = Point(0, 0, 1)
Point.DOWN = Point(0, 0, -1)
Point.LEFT = Point(-1, 0, 0)
Point.RIGHT = Point(1, 0, 0)
Point.FRONT = Point(0, 1, 0)
Point.BACK = Point(0, -1, 0)
Point.TRANSFORMS = set([Point.UP, Point.DOWN, Point.LEFT,
                        Point.RIGHT, Point.FRONT, Point.BACK])


@dataclass
class Nanobot:
    p: Point
    r: int

    def __lt__(self, other):
        return self.r < other.r

    def can_reach(self, p: Point):
        return Point.manhattan_dist(self.p, p) <= self.r


@dataclass
class Swarm:
    nanobots: list

    def in_range_of_strongest(self):
        strongest = max(self.nanobots)
        return [strongest.can_reach(bot.p) for bot in self.nanobots].count(True)

    def coords_in_range_of_most_bots(self):
        min_corner = (min([bot.p.x for bot in self.nanobots]), min(
            [bot.p.y for bot in self.nanobots]), min([bot.p.z for bot in self.nanobots]))
        max_corner = (max([bot.p.x for bot in self.nanobots]), max(
            [bot.p.y for bot in self.nanobots]), max([bot.p.z for bot in self.nanobots]))
        print(min_corner, max_corner)
        best_in_range_of = 0
        best_points = set()
        from tqdm import tqdm

        for x in tqdm(range(min_corner[0], max_corner[0]), leave=False):
            for y in tqdm(range(min_corner[1], max_corner[1]), leave=False):
                for z in tqdm(range(min_corner[2], max_corner[2]), leave=False):
                    point = Point(x, y, z)  # print(x, y, z)
                    in_range_of = [bot.can_reach(point)
                                   for bot in self.nanobots].count(True)
                    if in_range_of > best_in_range_of:
                        best_in_range_of = in_range_of
                        best_points = set([point])
                    elif in_range_of == best_in_range_of:
                        best_points.add(point)
        # print(best_in_range_of, best_points)
        return min(best_points)


def main():
    _, input_lines = helpers.load_input(23)

    # input_lines = """pos=<10,12,12>, r=2\npos=<12,14,12>, r=2\npos=<16,12,12>, r=4\npos=<14,14,14>, r=6\npos=<50,50,50>, r=200\npos=<10,10,10>, r=5""".strip().split("\n")  # noqa

    nanobots = deque()
    for line in input_lines:
        x, y, z, r = parser.parse(line).fixed
        nanobots.append(Nanobot(Point(x, y, z), r))

    swarm = Swarm(nanobots)

    print(f"parta: {swarm.in_range_of_strongest()}")
    print(f"partb: {swarm.coords_in_range_of_most_bots()}")


if __name__ == "__main__":
    import advent.aoc2018.helpers as helpers

    main()

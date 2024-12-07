import re
from dataclasses import dataclass

import z3


def z3_abs(n):
    return z3.If(n >= 0, n, -n)


def z3_man_dist(p1, p2):
    return sum(z3_abs(x1 - x2) for x1, x2 in zip(p1, p2))


@dataclass
class Point:
    x: int
    y: int
    z: int

    def manhattan_dist(self, other):
        return abs(self.x - other.x) + abs(self.y - other.y) + abs(self.z - other.z)

    def __hash__(self):
        return hash((self.x, self.y, self.z))

    def __eq__(self, other):
        return (self.x, self.y, self.z) == (other.x, other.y, other.z)

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y, self.z + other.z)

    def to_tuple(self):
        return (self.x, self.y, self.z)


ORIGIN = Point(0, 0, 0)


@dataclass
class Nanobot:
    p: Point
    r: int

    _REGEX = re.compile(r"pos=<(-?\d+),(-?\d+),(-?\d+)>, r=(-?\d+)")

    def in_range(self, p: Point):
        return self.p.manhattan_dist(p) <= self.r

    @staticmethod
    def parse(nanobot_str):
        x, y, z, r = map(int, Nanobot._REGEX.match(nanobot_str).groups())
        return Nanobot(Point(x, y, z), r)


@dataclass
class Swarm:
    nanobots: list

    def in_range_of_strongest(self):
        strongest = max(self.nanobots, key=lambda n: n.r)
        return sum(strongest.in_range(bot.p) for bot in self.nanobots)

    def optimal_point(self):
        # https://www.reddit.com/r/adventofcode/comments/a8s17l/2018_day_23_solutions/ecdcbin

        p = tuple(z3.Int(c) for c in "xyz")  # optimal (x, y, z)

        # the number of bots that can reach position p
        reachable_bot_count = sum(z3.If(z3_man_dist(p, b.p.to_tuple()) <= b.r, 1, 0) for b in self.nanobots)

        # man distance between p and origin
        origin_distance = z3_man_dist(p, ORIGIN.to_tuple())

        # create optimization problem
        opt = z3.Optimize()

        # add constraints
        opt.maximize(reachable_bot_count)
        opt.minimize(origin_distance)

        # solve the problem
        opt.check()
        model = opt.model()

        # get the values we care about from the model
        return Point(*(model[c].as_long() for c in p))

    @staticmethod
    def parse_swarm(swarm_str):
        return Swarm([Nanobot.parse(line) for line in swarm_str.splitlines()])


def part_1(txt):
    return Swarm.parse_swarm(txt).in_range_of_strongest()


def part_2(txt):
    point = Swarm.parse_swarm(txt).optimal_point()
    return point.manhattan_dist(ORIGIN)


if __name__ == "__main__":
    import aocd

    print(f"part_1: {part_1(aocd.data)}")
    print(f"part_2: {part_2(aocd.data)}")

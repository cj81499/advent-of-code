import itertools


class Point:
    def __init__(self, s: str):
        self.pos = tuple([int(x) for x in s.split(",")])

    def __hash__(self):
        return self.pos.__hash__()

    def __repr__(self):
        return str(self.pos)

    def dist(self, other):
        return sum([abs(self.pos[i] - other.pos[i]) for i in range(len(self.pos))])


class Constellation:
    number = 0

    def __init__(self, point):
        self.number = Constellation.number
        Constellation.number += 1
        self.points = set([point])

    def __hash__(self):
        return self.number

    def __repr__(self):
        return f"{self.number}-{self.points}"

    def join(self, other):
        connected = False
        if self.points is not None and other.points is not None:
            for p1 in self.points:
                for p2 in other.points:
                    if p1.dist(p2) <= 3:
                        connected = True
                        break
            if connected:
                self.points.update(other.points)
                other.points = None
        return connected


def parta(lines: list):
    constellations = set([Constellation(Point(line)) for line in lines])
    combinations_made = True
    while combinations_made:
        combinations_made = False
        for a, b in itertools.combinations(constellations, 2):
            success = a.join(b)
            if success:
                combinations_made = True
    constellations = set([c for c in constellations if c.points is not None])
    return len(constellations)


def partb(lines: list):
    raise NotImplementedError


def main():
    _, input_lines = helpers.load_input(25, "Four-Dimensional Adventure")

    print(f"parta: {parta(input_lines)}")
    # print(f"partb: {partb(input_lines)}")


if __name__ == "__main__":
    import advent.aoc2018.helpers as helpers

    main()

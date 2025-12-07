import itertools


class Point:
    def __init__(self, s: str) -> None:
        self.pos = tuple(int(x) for x in s.split(","))

    def __hash__(self):
        return hash(self.pos)

    def __repr__(self) -> str:
        return str(self.pos)

    def dist(self, other):
        return sum(abs(x1 - x2) for x1, x2 in zip(self.pos, other.pos, strict=True))


class Constellation:
    number = 0

    def __init__(self, point) -> None:
        self.number = Constellation.number
        Constellation.number += 1
        self.points = {point}

    def __hash__(self):
        return hash(self.number)

    def __repr__(self) -> str:
        return f"{self.number}-{self.points}"

    def join(self, other):
        connected = False
        if self.points is not None and other.points is not None:
            connected = any(p1.dist(p2) <= 3 for p1, p2 in itertools.product(self.points, other.points))
            if connected:
                self.points.update(other.points)
                other.points = None
        return connected


def part_1(txt):
    constellations = {Constellation(Point(line)) for line in txt.splitlines()}
    combinations_made = True
    while combinations_made:
        combinations_made = False
        for a, b in itertools.combinations(constellations, 2):
            combinations_made = a.join(b) or combinations_made
        constellations = {c for c in constellations if c.points is not None}
    return len(constellations)


if __name__ == "__main__":
    import aocd

    print(f"part_1: {part_1(aocd.data)}")

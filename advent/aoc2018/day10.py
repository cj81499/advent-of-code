import collections  # noqa
import itertools  # noqa
import re  # noqa


class Point:
    _PARSE_REGEX = re.compile(r"position=< *(-?\d+), +(-?\d+)> velocity=< *(-?\d+), +(-?\d+)>")

    def __init__(self, x, y, dx, dy):
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy

    @staticmethod
    def parse(point: str):
        match = Point._PARSE_REGEX.match(point)
        nums = map(int, match.groups())
        return Point(*nums)

    def __repr__(self):
        return f"Point(pos({self.x},{self.y}), vel({self.dx},{self.dy}))"

    def after(self, s=1):
        new_x = self.x + s*self.dx
        new_y = self.y + s*self.dy
        return Point(new_x, new_y, self.dx, self.dy)


class Cluster:
    def __init__(self, points):
        self.points = points
        self._min_x = min(self.points, key=lambda p: p.x).x
        self._max_x = max(self.points, key=lambda p: p.x).x
        self._min_y = min(self.points, key=lambda p: p.y).y
        self._max_y = max(self.points, key=lambda p: p.y).y
        self.area = (self._max_x - self._min_x) * (self._max_y - self._min_y)

    @staticmethod
    def parse(cluster: str):
        points = [Point.parse(line) for line in cluster.splitlines()]
        return Cluster(points)

    def after(self, s=1):
        if s == 0:
            return self
        new_points = [p.after(s) for p in self.points]
        return Cluster(new_points)

    def __str__(self):
        point_locations = {(p.x, p.y) for p in self.points}
        rows = []
        for y in range(self._min_y, self._max_y + 1):
            row = []
            for x in range(self._min_x, self._max_x + 1):
                row.append("#" if (x, y) in point_locations else ".")
            rows.append("".join(row))
        return "\n".join(rows)


def parta(txt):
    start_cluster = Cluster.parse(txt)

    prev_area = start_cluster.area
    for t in itertools.count():
        area = start_cluster.after(t).area
        if area > prev_area:
            break
        prev_area = area

    optimal_t = t - 1
    optimal_cluster = start_cluster.after(optimal_t)
    return f"\n{optimal_cluster}"


def partb(txt):
    start_cluster = Cluster.parse(txt)

    prev_area = start_cluster.area
    for t in itertools.count():
        area = start_cluster.after(t).area
        if area > prev_area:
            break
        prev_area = area

    optimal_t = t - 1
    return optimal_t


def main(txt):
    print(f"parta: {parta(txt)}")
    print(f"partb: {partb(txt)}")


if __name__ == "__main__":
    from aocd import data
    main(data)

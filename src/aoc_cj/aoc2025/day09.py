import itertools

import shapely

type Point = tuple[int, int]
type Rectangle = tuple[Point, Point]


def parse_point(line: str) -> Point:
    left, sep, right = line.partition(",")
    assert sep == ",", f"Invalid point: '{line}'"

    return int(left), int(right)


def area(r: Rectangle) -> int:
    return (abs(r[0][0] - r[1][0]) + 1) * (abs(r[0][1] - r[1][1]) + 1)


def rectangle(r: Rectangle) -> shapely.Polygon:
    (x1, y1), (x2, y2) = r
    return shapely.box(min(x1, x2), min(y1, y2), max(x1, x2), max(y1, y2))


def part_1(txt: str) -> int:
    points = set(map(parse_point, txt.splitlines()))
    return max(area(r) for r in itertools.combinations(points, r=2))


def part_2(txt: str) -> int:
    # inspired by https://aoc.csokavar.hu/2025/9/
    points = tuple(map(parse_point, txt.splitlines()))
    region = shapely.Polygon(points)
    return max(area(r) for r in itertools.combinations(points, r=2) if region.contains(rectangle(r)))


if __name__ == "__main__":
    import aocd

    print(f"part_1: {part_1(aocd.data)}")
    print(f"part_2: {part_2(aocd.data)}")

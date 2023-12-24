import collections
import itertools


def man_dist(p1, p2):
    return sum(abs(a - b) for a, b in zip(p1, p2))


def corners(points):
    xs, ys = zip(*points)
    return min(xs), max(xs), min(ys), max(ys)


def nearest_points(point, points):
    min_dist = float("inf")
    closest = []
    for p in points:
        d = man_dist(point, p)
        if d < min_dist:
            min_dist = d
            closest = [p]
        elif d == min_dist:
            closest.append(p)
    return closest


def part_1(txt):
    points = {tuple(map(int, line.split(", "))) for line in txt.splitlines()}
    min_x, max_x, min_y, max_y = corners(points)

    areas = collections.Counter()
    inf_area_points = set()
    for p in itertools.product(range(min_x, max_x + 1), range(min_y, max_y + 1)):
        x, y = p

        nearest = nearest_points(p, points)
        if len(nearest) == 1:
            areas[nearest[0]] += 1
            # if we're on an edge, this is an inf area point
            if x == min_x or x == max_x or y == min_y or y == max_y:
                inf_area_points.add(nearest[0])

    # remove inf area points from areas
    finite_areas = {k: v for k, v in areas.items() if k not in inf_area_points}

    return max(finite_areas.values())


def dist_to_all(point, points):
    return sum(man_dist(point, p) for p in points)


def part_2(txt, total_dist=10000):
    points = {tuple(map(int, line.split(", "))) for line in txt.splitlines()}
    min_x, max_x, min_y, max_y = corners(points)
    return sum(
        dist_to_all(p, points) < total_dist for p in itertools.product(range(min_x, max_x + 1), range(min_y, max_y + 1))
    )


if __name__ == "__main__":
    from aocd import data

    print(f"part_1: {part_1(data)}")
    print(f"part_2: {part_2(data)}")

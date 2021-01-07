import collections  # noqa
import itertools  # noqa
import re  # noqa


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


def parta(txt):
    points = set(tuple(map(int, line.split(", "))) for line in txt.splitlines())
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


def partb(txt, total_dist=10000):
    points = set(tuple(map(int, line.split(", "))) for line in txt.splitlines())
    min_x, max_x, min_y, max_y = corners(points)
    return sum(
        dist_to_all(p, points) < total_dist
        for p in itertools.product(range(min_x, max_x + 1), range(min_y, max_y + 1))
    )


def main(txt):
    print(f"parta: {parta(txt)}")
    print(f"partb: {partb(txt)}")


if __name__ == "__main__":
    from aocd import data
    main(data)

from collections.abc import Generator

Point3D = tuple[int, int, int]


def adj(p: Point3D) -> Generator[Point3D, None, None]:
    x, y, z = p
    for dx, dy, dz in ((1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)):
        yield x + dx, y + dy, z + dz


def parta(txt: str) -> int:
    points = {(a, b, c) for a, b, c, in (map(int, line.split(",")) for line in txt.splitlines())}

    return sa(points)


def sa(points: set[Point3D]) -> int:
    surface_area = 0
    for p in points:
        # count exposed faces
        for ap in adj(p):
            if ap not in points:
                surface_area += 1
    return surface_area


def partb(txt: str) -> int:
    points = {(a, b, c) for a, b, c, in (map(int, line.split(",")) for line in txt.splitlines())}

    min_x = min(x for x, y, z in points)
    max_x = max(x for x, y, z in points)
    min_y = min(y for x, y, z in points)
    max_y = max(y for x, y, z in points)
    min_z = min(z for x, y, z in points)
    max_z = max(z for x, y, z in points)

    air_points: set[Point3D] = set()
    for xx in range(min_x, max_x + 1):
        for yy in range(min_y, max_y + 1):
            for zz in range(min_z, max_z + 1):
                p = (xx, yy, zz)
                if p not in points:
                    air_points.add(p)

    # remove air points that are not surrounded fully by points or
    # other air_points until no points are removed
    removed_points = True
    while removed_points:
        to_remove = set()

        for p in air_points:
            for ap in adj(p):
                if ap not in air_points and ap not in points:
                    to_remove.add(p)
                    continue

        if to_remove:
            air_points.difference_update(to_remove)
        else:
            removed_points = False

    return sa(points) - sa(air_points)


if __name__ == "__main__":
    from aocd import data

    print(f"parta: {parta(data)}")
    print(f"partb: {partb(data)}")

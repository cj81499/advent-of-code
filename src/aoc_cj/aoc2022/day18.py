import itertools

from aoc_cj import util


def part_1(txt: str) -> int:
    lava_points = {util.Point3D.parse(line) for line in txt.splitlines()}
    return surface_area(lava_points)


def surface_area(points: set[util.Point3D]) -> int:
    return sum(1 for p in points for ap in p.adj() if ap not in points)


def part_2(txt: str) -> int:
    lava_points = {util.Point3D.parse(line) for line in txt.splitlines()}

    all_points_in_volume = {
        util.Point3D(x, y, z)
        for x, y, z in itertools.product(
            range(min(p.x for p in lava_points), max(p.x for p in lava_points) + 1),
            range(min(p.y for p in lava_points), max(p.y for p in lava_points) + 1),
            range(min(p.z for p in lava_points), max(p.z for p in lava_points) + 1),
        )
    }
    air_points = all_points_in_volume.difference(lava_points)

    # remove points from air_points that are not fully surrounded by points in
    # either lava_points or air_points until no points are removed.
    # only air pockets will remain!
    while True:
        if to_remove := {
            p for p in air_points if any(ap not in air_points and ap not in lava_points for ap in p.adj())
        }:
            air_points.difference_update(to_remove)
        else:
            break

    return surface_area(lava_points) - surface_area(air_points)


if __name__ == "__main__":
    import aocd

    print(f"part_1: {part_1(aocd.data)}")
    print(f"part_2: {part_2(aocd.data)}")

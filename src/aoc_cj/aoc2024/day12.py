import dataclasses
import itertools

from aoc_cj import util


@dataclasses.dataclass(frozen=True, kw_only=True, slots=True)
class Region:
    points: frozenset[complex]

    def area(self) -> int:
        return len(self.points)

    def perimeter(self) -> int:
        return sum(1 for p in self.points for adj_p in util.adj_4(p) if adj_p not in self.points)

    def price(self) -> int:
        return self.area() * self.perimeter()

    def side_count(self) -> int:
        # for a polygon, number of sides == number of corners. We will count corners instead of sides.
        corner_count = 0

        # Scan a 2x2 "grid" over the area of the region.
        # Count corners based on what we see.
        #
        # No edge:
        # ..  ##  ##  .#  ..  #.
        # ..  ##  ..  .#  ##  #.
        #
        # 1 edge:
        # #.  .#  ..  ..  .#  #.  ##  ##
        # ..  ..  .#  #.  ##  ##  #.  .#
        #
        # 2 edges:
        # #.  .#
        # .#  #.

        # The loop body will consider a 2x2 region where `p` is at the top left.
        # Consider a region containing a single point. If we only check at that point,
        # we'll only count the bottom right corner.
        # To fix this, in addition to checking the points in the region, we also check
        # at the points shifted up one, shifted left by one, and shifted left one AND up one.
        to_check = set(
            itertools.chain.from_iterable(
                (
                    p,  # point itself
                    p - 1,  # point shifted left one
                    p - 1j,  # point shifted up one
                    p - 1 - 1j,  # point shifted left one and up one
                )
                for p in self.points
            )
        )
        for p in to_check:
            p_in_region = p in self.points
            below_in_region = p + 1j in self.points
            right_in_region = p + 1 in self.points
            bottom_right_in_region = p + 1 + 1j in self.points

            in_region_count = sum((p_in_region, below_in_region, right_in_region, bottom_right_in_region))
            if in_region_count in (1, 3):
                corner_count += 1
            elif in_region_count == 2 and p_in_region not in (right_in_region, below_in_region):
                corner_count += 2

        return corner_count

    def bulk_price(self) -> int:
        return self.area() * self.side_count()


def part_1(txt: str) -> int:
    return sum(r.price() for r in parse_regions(txt))


def part_2(txt: str) -> int:
    return sum(r.bulk_price() for r in parse_regions(txt))


def parse_regions(txt: str) -> frozenset[Region]:
    grid = {x + y * 1j: c for y, row in enumerate(txt.splitlines()) for x, c in enumerate(row)}
    regions = set[Region]()
    while grid:
        pos, val = grid.popitem()
        to_add = {pos}
        region = set[complex]()
        while to_add:
            adding = to_add.pop()
            region.add(adding)
            grid.pop(adding, None)
            to_add.update(adj_p for adj_p in util.adj_4(adding) if grid.get(adj_p) == val)
        regions.add(Region(points=frozenset(region)))
    return frozenset(regions)


if __name__ == "__main__":
    import aocd

    print(f"part_1: {part_1(aocd.data)}")
    print(f"part_2: {part_2(aocd.data)}")

import dataclasses
from collections.abc import Generator


def adj_4(p: complex) -> Generator[complex, None, None]:
    for delta in (-1, 1, -1j, 1j):
        yield p + delta


@dataclasses.dataclass(frozen=True, kw_only=True, slots=True)
class Region:
    points: frozenset[complex]

    def area(self) -> int:
        return len(self.points)

    def perimeter(self) -> int:
        return sum(1 for p in self.points for adj_p in adj_4(p) if adj_p not in self.points)

    def price(self) -> int:
        return self.area() * self.perimeter()

    def side_count(self) -> int:
        r = self.points
        # number of sides == number of "corners"
        corners = set[complex]()

        # LESS HACKY IDEA: scan a 2x2 "grid" over the area of the region,
        # checking if the intersection of 1x1 squares at the middle of the region is an edge
        #
        # .. -> no edge
        # ..
        #
        # ## -> no edge
        # ..
        #
        #
        # #. -> 1 edge
        # ..
        #
        # #. -> 2 edges
        # .#

        for p in r:
            above_in_r = p - 1j in r
            below_in_r = p + 1j in r
            left_in_r = p - 1 in r
            right_in_r = p + 1 in r
            top_left_in_r = p - 1j - 1 in r
            top_right_in_r = p - 1j + 1 in r
            bottom_left_in_r = p + 1j - 1 in r
            bottom_right_in_r = p + 1j + 1 in r

            if (neither_top_left := not (above_in_r or left_in_r)) or (above_in_r and left_in_r and not top_left_in_r):
                # handles edge case where adjacent positions are not in region, but diagonal position is in region.
                # This is just one corner _position_, but accounts for two corners (and thus, two sides).
                # Wacky hack, but we shift the position slightly such that it won't collide with the corner position we
                # add when we detect the same corner position from the opposite "side"
                if neither_top_left and top_left_in_r:
                    corners.add(p - 0.1 - 0.1j)
                else:
                    corners.add(p)
            if (neither_top_right := not (above_in_r or right_in_r)) or (
                above_in_r and right_in_r and not top_right_in_r
            ):
                if neither_top_right and top_right_in_r:
                    corners.add(p + 0.1 - 0.1j)
                else:
                    corners.add(p + 1)
            if (neither_bottom_left := not (below_in_r or left_in_r)) or (
                below_in_r and left_in_r and not bottom_left_in_r
            ):
                if neither_bottom_left and bottom_left_in_r:
                    corners.add(p - 0.1 + 0.1j)
                else:
                    corners.add(p + 1j)
            if (neither_bottom_right := not (below_in_r or right_in_r)) or (
                below_in_r and right_in_r and not bottom_right_in_r
            ):
                if neither_bottom_right and bottom_right_in_r:
                    corners.add(p + 0.1 + 0.1j)
                else:
                    corners.add(p + 1j + 1)

        return len(corners)

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
            to_add.update(adj_p for adj_p in adj_4(adding) if grid.get(adj_p) == val)
        regions.add(Region(points=frozenset(region)))
    return frozenset(regions)


if __name__ == "__main__":
    import aocd

    print(f"part_1: {part_1(aocd.data)}")
    print(f"part_2: {part_2(aocd.data)}")

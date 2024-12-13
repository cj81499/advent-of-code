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

            if (not (above_in_r or left_in_r)) or (above_in_r and left_in_r and not top_left_in_r):
                corners.add(p)
            if (not (above_in_r or right_in_r)) or (above_in_r and right_in_r and not top_right_in_r):
                corners.add(p + 1)
            if (not (below_in_r or left_in_r)) or (below_in_r and left_in_r and not bottom_left_in_r):
                corners.add(p + 1j)
            if (not (below_in_r or right_in_r)) or (below_in_r and right_in_r and not bottom_right_in_r):
                corners.add(p + 1j + 1)

        # side count is NOT perfectly equal to count of corner points b/c some corner points have TWO corners.
        # For example, the point at the center of the following region should count twice.
        # ######
        # ###..#
        # ###..#
        # #..###
        # #..###
        # ######
        return sum(2 if self._is_double_corner(c) else 1 for c in corners)

    def _is_double_corner(self, p: complex) -> bool:
        in_r = p in self.points
        above_in_r = p - 1j in self.points
        left_in_r = p - 1 in self.points
        top_left_in_r = p - 1j - 1 in self.points
        return in_r == top_left_in_r and above_in_r == left_in_r and in_r != above_in_r

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

from collections.abc import Generator


def adj_4(p: complex) -> Generator[complex, None, None]:
    for delta in (-1, 1, -1j, 1j):
        yield p + delta


def part_1(txt: str) -> int:
    regions = parse_regions(txt)

    # sum of all region's prices
    s = 0

    for r in regions:
        # find area of each region
        area = len(r)
        # find perimeter of each region
        perimeter = 0  # TODO
        for p in r:
            for adj_p in adj_4(p):
                if adj_p not in r:
                    perimeter += 1
        # price of fence for a region is area * perimeter
        price = area * perimeter

        s += price

    return s


def part_2(txt: str) -> int:
    regions = parse_regions(txt)

    # sum of all region's prices
    s = 0

    for r in regions:
        # find area of each region
        area = len(r)

        # find number of sides of each region
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

        side_count = len(corners)

        # price of fence for a region is area * perimeter
        price = area * side_count

        s += price

    return s


def parse_regions(txt: str) -> list[set[complex]]:
    grid = {x + y * 1j: c for y, row in enumerate(txt.splitlines()) for x, c in enumerate(row)}

    regions: list[set[complex]] = []
    to_handle = {p for p in grid}
    while to_handle:
        handling = to_handle.pop()
        val = grid[handling]
        to_add = {handling}
        region = set[complex]()
        while to_add:
            adding = to_add.pop()
            region.add(adding)
            for adj_p in adj_4(adding):
                if adj_p not in region and grid.get(adj_p) == val:
                    to_add.add(adj_p)
        to_handle.difference_update(region)
        regions.append(region)
    return regions


if __name__ == "__main__":
    import aocd

    print(f"part_1: {part_1(aocd.data)}")
    print(f"part_2: {part_2(aocd.data)}")

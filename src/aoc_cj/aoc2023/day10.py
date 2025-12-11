import dataclasses
import functools
from collections import deque
from collections.abc import Generator

import more_itertools as mi

UP = -1j
DOWN = +1j
LEFT = -1
RIGHT = +1


@dataclasses.dataclass(frozen=True, order=True)
class GridPosition:
    x: int
    y: int

    def _add(self, x: int, y: int) -> "GridPosition":
        return GridPosition(self.x + x, self.y + y)

    def up(self) -> "GridPosition":
        return self._add(0, -1)

    def down(self) -> "GridPosition":
        return self._add(0, 1)

    def left(self) -> "GridPosition":
        return self._add(-1, 0)

    def right(self) -> "GridPosition":
        return self._add(1, 0)

    def adj_4(self) -> tuple["GridPosition", "GridPosition", "GridPosition", "GridPosition"]:
        return (self.up(), self.down(), self.left(), self.right())

    def _top_left_corner(self) -> "TopLeftCorner":
        return TopLeftCorner(self)

    def _top_right_corner(self) -> "TopLeftCorner":
        return TopLeftCorner(self.right())

    def _bottom_left_corner(self) -> "TopLeftCorner":
        return TopLeftCorner(self.down())

    def _bottom_right_corner(self) -> "TopLeftCorner":
        return TopLeftCorner(self.down().right())

    def corners(self) -> tuple["TopLeftCorner", "TopLeftCorner", "TopLeftCorner", "TopLeftCorner"]:
        return (
            self._top_left_corner(),
            self._top_right_corner(),
            self._bottom_left_corner(),
            self._bottom_right_corner(),
        )


@dataclasses.dataclass(frozen=True, order=True)
class TopLeftCorner:
    pos: GridPosition

    def up(self) -> "TopLeftCorner":
        return TopLeftCorner(self.pos.up())

    def down(self) -> "TopLeftCorner":
        return TopLeftCorner(self.pos.down())

    def left(self) -> "TopLeftCorner":
        return TopLeftCorner(self.pos.left())

    def right(self) -> "TopLeftCorner":
        return TopLeftCorner(self.pos.right())


@dataclasses.dataclass(frozen=True, order=True)
class Grid:
    contents: dict[GridPosition, str]

    def start_pos(self) -> GridPosition:
        return mi.one(p for p, c in self.contents.items() if c == "S")

    def connections(self, p: GridPosition) -> Generator[GridPosition]:
        pipe_type = self.contents.get(p, ".")

        if pipe_type == ".":
            return

        if pipe_type == "|":
            yield p.up()
            yield p.down()
            return

        if pipe_type == "-":
            yield p.left()
            yield p.right()
            return

        if pipe_type == "L":
            yield p.up()
            yield p.right()
            return

        if pipe_type == "J":
            yield p.up()
            yield p.left()
            return

        if pipe_type == "7":
            yield p.down()
            yield p.left()
            return

        if pipe_type == "F":
            yield p.down()
            yield p.right()
            return

        if pipe_type == "S":
            for adj_p in p.adj_4():
                if p in self.connections(adj_p):
                    yield adj_p
            return

        msg = f"unexpected value in pipe: '{pipe_type}'"
        raise AssertionError(msg)

    @functools.cached_property
    def _max_x(self) -> int:
        return max(p.x for p in self.contents)

    @functools.cached_property
    def _max_y(self) -> int:
        return max(p.y for p in self.contents)

    def corner_in_bounds(self, corner: TopLeftCorner) -> bool:
        return (0 <= corner.pos.x <= self._max_x + 1) and (0 <= corner.pos.y <= self._max_y + 1)

    @functools.cached_property
    def loop(self) -> dict[GridPosition, int]:
        loop_distances: dict[GridPosition, int] = {}
        to_explore = deque([(self.start_pos(), 0)])
        while to_explore:
            p, distance = to_explore.popleft()
            if p in loop_distances:
                continue
            loop_distances[p] = distance
            for adj_p in self.connections(p):
                if adj_p not in loop_distances:
                    to_explore.append((adj_p, distance + 1))
        return loop_distances

    def can_flood(self, from_corner: TopLeftCorner, direction: complex) -> bool:
        # find grid positions to check
        p1 = from_corner.pos
        if direction != DOWN:
            p1 = p1.up()
        if direction != RIGHT:
            p1 = p1.left()

        p2 = from_corner.pos
        if direction == UP:
            p2 = p2.up()
        if direction == LEFT:
            p2 = p2.left()

        # if either position is not in the loop, it can be flooded
        if p1 not in self.loop or p2 not in self.loop:
            return True
        # if the both positions are in the loop, it can be flooded if they're not connected
        return p1 not in self.connections(p2)


def part_1(txt: str) -> int:
    grid = Grid({GridPosition(x, y): c for y, line in enumerate(txt.splitlines()) for x, c in enumerate(line)})
    return max(grid.loop.values())


def part_2(txt: str) -> int:
    grid = Grid({GridPosition(x, y): c for y, line in enumerate(txt.splitlines()) for x, c in enumerate(line)})

    # to find tiles enclosed by the loop, we will flood the corners of each grid position
    # (not the grid positions themselves to allow for flooding to move between disconnected pipes)
    # at the end, grid positions with no flooded corners are enclosed within the loop

    flood_reachable = set[TopLeftCorner]()
    # starting from top left corner of (0, 0), we will "flood" the corners of the grid.
    to_explore = deque([TopLeftCorner(GridPosition(0, 0))])
    while to_explore:
        corner = to_explore.popleft()

        # if corner is out of bounds, skip it
        if not grid.corner_in_bounds(corner):
            continue

        # if we've already flooded corner, skip it
        if corner in flood_reachable:
            continue
        flood_reachable.add(corner)

        if grid.can_flood(corner, UP):  # flood up
            to_explore.append(corner.up())
        if grid.can_flood(corner, DOWN):  # flood down
            to_explore.append(corner.down())
        if grid.can_flood(corner, LEFT):  # flood left
            to_explore.append(corner.left())
        if grid.can_flood(corner, RIGHT):  # flood right
            to_explore.append(corner.right())

    # grid spaces that have no flooded corners are enclosed by the loop
    # count grid positions where no corner was reached during the flooding process
    return sum(1 for p in grid.contents if not any(p in flood_reachable for p in p.corners()))


if __name__ == "__main__":
    import aocd

    print(f"part_1: {part_1(aocd.data)}")
    print(f"part_2: {part_2(aocd.data)}")

import enum
import itertools
import math

import numpy as np


@enum.unique
class Direction(enum.Enum):
    TOP = enum.auto()
    RIGHT = enum.auto()
    BOTTOM = enum.auto()
    LEFT = enum.auto()


OPPOSITE_DIRECTIONS = {
    Direction.TOP: Direction.BOTTOM,
    Direction.RIGHT: Direction.LEFT,
    Direction.BOTTOM: Direction.TOP,
    Direction.LEFT: Direction.RIGHT,
}

SEA_MONSTER = [
    "                  # ",
    "#    ##    ##    ###",
    " #  #  #  #  #  #   ",
]

SEA_MONSTER_POINTS = {(y, x) for y, row in enumerate(SEA_MONSTER) for x, c in enumerate(row) if c == "#"}


class Tile:
    def __init__(self, tile_str) -> None:
        tile_num, *tile = tile_str.splitlines()
        self.n = int(tile_num[5:-1])

        self._grid = np.array([list(row) for row in tile])

        shape = self._grid.shape
        assert shape[0] == shape[1]

        self.connections = dict.fromkeys(Direction)
        self.is_aligned = False

    def border(self, direction):
        return self.borders()[direction]

    def borders(self):
        return {
            Direction.TOP: "".join(self._grid[0, :]),
            Direction.RIGHT: "".join(self._grid[:, -1]),
            Direction.BOTTOM: "".join(self._grid[-1, :]),
            Direction.LEFT: "".join(self._grid[:, 0]),
        }

    def connect(self, other) -> None:
        for (b1_d, b1), (b2_d, b2) in itertools.product(self.borders().items(), other.borders().items()):
            if b1 == b2 or b1 == "".join(reversed(b2)):
                self.connections[b1_d] = other
                other.connections[b2_d] = self

    def empty_connections(self):
        return [*self.connections.values()].count(None)

    def __repr__(self) -> str:
        return f"t#{self.n}"

    def center(self):
        return self._grid[1:-1, 1:-1]

    def _rotate(self) -> None:
        self._grid = np.rot90(self._grid, k=-1)
        self.connections = {
            Direction.TOP: self.connections[Direction.LEFT],
            Direction.RIGHT: self.connections[Direction.TOP],
            Direction.BOTTOM: self.connections[Direction.RIGHT],
            Direction.LEFT: self.connections[Direction.BOTTOM],
        }

    def _flipud(self) -> None:
        self._grid = np.flipud(self._grid)
        c = self.connections
        c[Direction.TOP], c[Direction.BOTTOM] = c[Direction.BOTTOM], c[Direction.TOP]

    def _fliplr(self) -> None:
        self._grid = np.fliplr(self._grid)
        c = self.connections
        c[Direction.LEFT], c[Direction.RIGHT] = c[Direction.RIGHT], c[Direction.LEFT]

    def _is_top_left(self):
        return self.connections[Direction.TOP] is None and self.connections[Direction.LEFT] is None

    def make_top_left(self) -> None:
        assert self.empty_connections() == 2
        while not (self._is_top_left()):
            self._rotate()
        for direction, tile in self.connections.items():
            if tile is not None:
                tile._cascade_match(self, direction)

    def _cascade_match(self, other, direction) -> None:
        self._match(other, direction)
        for direction in (Direction.BOTTOM, Direction.RIGHT):
            t = self.connections[direction]
            if t is not None:
                t._cascade_match(self, direction)

    def _match(self, other, direction) -> None:
        if self.is_aligned:
            return
        # rotate until we match
        while self.connections[OPPOSITE_DIRECTIONS[direction]] != other:
            self._rotate()
        # if the borders don't match, we need to flip
        if other.border(direction) != self.border(OPPOSITE_DIRECTIONS[direction]):
            if direction in (Direction.LEFT, Direction.RIGHT):
                self._flipud()
            else:
                self._fliplr()
        assert other.border(direction) == self.border(OPPOSITE_DIRECTIONS[direction])

        self.is_aligned = True


def parse_tiles(txt):
    tiles = [Tile(t) for t in txt.split("\n\n")]
    connect_tiles(tiles)
    return tiles


def connect_tiles(tiles) -> None:
    for t1, t2 in itertools.combinations(tiles, 2):
        t1.connect(t2)


def sea_monster_at(picture, y, x):
    area = picture[y : y + len(SEA_MONSTER), x : x + len(SEA_MONSTER[0])]
    height, width = area.shape
    if height != len(SEA_MONSTER):
        return False
    if width != len(SEA_MONSTER[0]):
        return False
    return all(area[p] == "#" for p in SEA_MONSTER_POINTS)


def part_1(txt) -> int:
    tiles = parse_tiles(txt)
    corners = [t for t in tiles if t.empty_connections() == 2]
    return math.prod(t.n for t in corners)


def part_2(txt):
    tiles = parse_tiles(txt)

    corners = [t for t in tiles if t.empty_connections() == 2]
    top_left = corners[0]  # pick a corner for top left
    top_left.make_top_left()  # align other tiles to it

    # convert the graph of tiles to a proper grid
    grid = []
    row_traverse = top_left
    while row_traverse is not None:
        col_traverse = row_traverse
        row = []
        while col_traverse is not None:
            row.append(col_traverse)
            col_traverse = col_traverse.connections[Direction.RIGHT]
        row_traverse = row_traverse.connections[Direction.BOTTOM]
        grid.append(row)

    picture = np.vstack([np.hstack([t.center() for t in row]) for row in grid])
    pound_count = sum(c == "#" for c in "".join("".join(row) for row in picture))
    sea_monster_pound_count = count_sea_monsters(picture) * len(SEA_MONSTER_POINTS)
    return pound_count - sea_monster_pound_count


def count_sea_monsters(picture):
    # it's possible the picture gets built with the wrong orientation.
    # try them all until we find the one with sea monsters
    for _ in range(2):
        for _ in range(4):
            height, width = picture.shape
            result = sum(sea_monster_at(picture, y, x) for (y, x) in itertools.product(range(height), range(width)))
            if result > 0:
                return result
            picture = np.rot90(picture)
        picture = np.fliplr(picture)
    return None


if __name__ == "__main__":
    import aocd

    print(f"part_1: {part_1(aocd.data)}")
    print(f"part_2: {part_2(aocd.data)}")

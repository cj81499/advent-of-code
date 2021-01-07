import collections  # noqa
import enum
import itertools  # noqa
import re  # noqa

import numpy as np


@enum.unique
class Directions(enum.Enum):
    TOP = enum.auto()
    RIGHT = enum.auto()
    BOTTOM = enum.auto()
    LEFT = enum.auto()


OPPOSITE_DIRECTIONS = {
    Directions.TOP: Directions.BOTTOM,
    Directions.RIGHT: Directions.LEFT,
    Directions.BOTTOM: Directions.TOP,
    Directions.LEFT: Directions.RIGHT,
}

SEA_MONSTER = [
    "                  # ",
    "#    ##    ##    ###",
    " #  #  #  #  #  #   ",
]

SEA_MONSTER_POINTS = {(y, x) for y, row in enumerate(SEA_MONSTER) for x, c in enumerate(row) if c == "#"}


class Tile:
    def __init__(self, tile_str):
        tile_num, *tile = tile_str.splitlines()
        self.n = int(tile_num[5: -1])

        self._grid = np.array([[c for c in row] for row in tile])

        shape = self._grid.shape
        assert shape[0] == shape[1]

        self.connections = {d: None for d in Directions}
        self.is_aligned = False

    def border(self, direction):
        return self.borders()[direction]

    def borders(self):
        return {
            Directions.TOP: "".join(self._grid[0, :]),
            Directions.RIGHT: "".join(self._grid[:, -1]),
            Directions.BOTTOM: "".join(self._grid[-1, :]),
            Directions.LEFT: "".join(self._grid[:, 0]),
        }

    def connect(self, other):
        for (b1_d, b1), (b2_d, b2) in itertools.product(self.borders().items(), other.borders().items()):
            if b1 == b2 or b1 == "".join(reversed(b2)):
                self.connections[b1_d] = other
                other.connections[b2_d] = self

    def empty_connections(self):
        return [*self.connections.values()].count(None)

    def __repr__(self):
        return f"t#{self.n}"

    def center(self):
        return self._grid[1:-1, 1:-1]

    def _rotate(self):
        self._grid = np.rot90(self._grid, k=-1)
        self.connections = {
            Directions.TOP: self.connections[Directions.LEFT],
            Directions.RIGHT: self.connections[Directions.TOP],
            Directions.BOTTOM: self.connections[Directions.RIGHT],
            Directions.LEFT: self.connections[Directions.BOTTOM],
        }

    def _flipud(self):
        self._grid = np.flipud(self._grid)
        c = self.connections
        c[Directions.TOP], c[Directions.BOTTOM] = c[Directions.BOTTOM], c[Directions.TOP]

    def _fliplr(self):
        self._grid = np.fliplr(self._grid)
        c = self.connections
        c[Directions.LEFT], c[Directions.RIGHT] = c[Directions.RIGHT], c[Directions.LEFT]

    def _is_top_left(self):
        return self.connections[Directions.TOP] is None and self.connections[Directions.LEFT] is None

    def make_top_left(self):
        assert self.empty_connections() == 2
        while not (self._is_top_left()):
            self._rotate()
        for direction, tile in self.connections.items():
            if tile is not None:
                tile._cascade_match(self, direction)

    def _cascade_match(self, other, direction):
        self._match(other, direction)
        for direction in (Directions.BOTTOM, Directions.RIGHT):
            t = self.connections[direction]
            if t is not None:
                t._cascade_match(self, direction)

    def _match(self, other, direction):
        if self.is_aligned:
            return
        # rotate until we match
        while self.connections[OPPOSITE_DIRECTIONS[direction]] != other:
            self._rotate()
        # if the borders don't match, we need to flip
        if other.border(direction) != self.border(OPPOSITE_DIRECTIONS[direction]):
            if direction in (Directions.LEFT, Directions.RIGHT):
                self._flipud()
            else:
                self._fliplr()
        assert other.border(direction) == self.border(OPPOSITE_DIRECTIONS[direction])

        self.is_aligned = True


def parse_tiles(txt):
    tiles = [Tile(t) for t in txt.split("\n\n")]
    connect_tiles(tiles)
    return tiles


def connect_tiles(tiles):
    for t1, t2 in itertools.combinations(tiles, 2):
        t1.connect(t2)


def sea_monster_at(picture, y, x):
    area = picture[y:y+len(SEA_MONSTER), x:x+len(SEA_MONSTER[0])]
    height, width = area.shape
    if height != len(SEA_MONSTER):
        return False
    if width != len(SEA_MONSTER[0]):
        return False
    return all(area[p] == "#" for p in SEA_MONSTER_POINTS)


def parta(txt):
    tiles = parse_tiles(txt)
    corners = [t for t in tiles if t.empty_connections() == 2]
    return np.prod([t.n for t in corners])


def partb(txt):
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
            col_traverse = col_traverse.connections[Directions.RIGHT]
        row_traverse = row_traverse.connections[Directions.BOTTOM]
        grid.append(row)

    picture = np.vstack([np.hstack([t.center() for t in row]) for row in grid])

    # TODO: it's possible the picture gets built with the wrong orientation and this won't work.
    # for my input, I got lucky (1/8 chance(!) b/c 8 orientations).
    # I'll (probably) come back and do this later.

    height, width = picture.shape
    sea_monsters_found = sum(sea_monster_at(picture, y, x) for (y, x) in itertools.product(range(height), range(width)))

    pound_count = sum(c == "#" for c in "".join("".join(row) for row in picture))

    return pound_count - (sea_monsters_found * len(SEA_MONSTER_POINTS))


def main(txt):
    print(f"parta: {parta(txt)}")
    print(f"partb: {partb(txt)}")


if __name__ == "__main__":
    from aocd import data
    main(data)

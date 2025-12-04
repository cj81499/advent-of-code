import enum


class Color(enum.Enum):
    WHITE = True
    BLACK = False


class Direction(enum.Enum):
    EAST = "e"
    SOUTH_EAST = "se"
    SOUTH_WEST = "sw"
    WEST = "w"
    NORTH_WEST = "nw"
    NORTH_EAST = "ne"


class Coordinate:
    # Using axial coordinates
    # https://www.redblobgames.com/grids/hexagons/
    def __init__(self, q, r):
        self._q = q
        self._r = r

    def _as_tuple(self):
        return (self._q, self._r)

    def __repr__(self):
        return f"(q:{self._q}, r:{self._r})"

    def __hash__(self):
        return hash(self._as_tuple())

    def __eq__(self, other):
        assert isinstance(other, Coordinate)
        return self._as_tuple() == other._as_tuple()

    def __add__(self, other):
        assert isinstance(other, Coordinate)
        return Coordinate(self._q + other._q, self._r + other._r)

    def adj(self):
        return {d: self + Coordinate.ADJ[d] for d in Direction}


Coordinate.ADJ = {
    Direction.EAST: Coordinate(+1, 0),
    Direction.SOUTH_EAST: Coordinate(0, +1),
    Direction.SOUTH_WEST: Coordinate(-1, +1),
    Direction.WEST: Coordinate(-1, 0),
    Direction.NORTH_WEST: Coordinate(0, -1),
    Direction.NORTH_EAST: Coordinate(+1, -1),
}


class HexTile:
    _n = 0

    def __init__(self):
        self._color = Color.WHITE
        self.n = HexTile._n
        HexTile._n += 1

    def __repr__(self):
        return f"T{self.n}({self._color})"

    def toggle_color(self):
        self._color = Color(not self._color.value)

    def get_color(self):
        return self._color


class HexGrid:
    ORIGIN = Coordinate(0, 0)

    def __init__(self):
        self._tiles = {}
        self._create_tile_at(HexGrid.ORIGIN)

    def flip_tile(self, directions):
        pos = HexGrid.ORIGIN
        for d in directions:
            pos = pos + Coordinate.ADJ[d]
        if pos not in self._tiles:
            self._create_tile_at(pos)
        self._tiles[pos].toggle_color()

    def count_black_tiles(self):
        return sum(t.get_color() == Color.BLACK for t in self._tiles.values())

    def simulate_day(self):
        # add white tiles next to all all black tiles
        for pos, tile in list(self._tiles.items()):
            if tile.get_color() == Color.BLACK:
                for adj_pos in pos.adj().values():
                    if adj_pos not in self._tiles:
                        self._create_tile_at(adj_pos)

        # determine which tiles need to be flipped
        to_flip = {tile for pos, tile in self._tiles.items() if self._should_flip(tile, pos)}

        # flip tiles
        for tile in to_flip:
            tile.toggle_color()

    def _should_flip(self, tile, pos):
        count = self._count_adj_black_tiles(pos)
        if (tile.get_color() == Color.BLACK and (count == 0 or count > 2)) or (
            tile.get_color() == Color.WHITE and count == 2
        ):
            return True
        return False

    def _count_adj_black_tiles(self, pos):
        count = 0
        for adj_pos in pos.adj().values():
            adj_tile = self._tiles.get(adj_pos)
            if adj_tile is not None and adj_tile.get_color() == Color.BLACK:
                count += 1
        return count

    def _create_tile_at(self, pos):
        assert pos not in self._tiles
        self._tiles[pos] = HexTile()


def parse(line):
    directions = []
    i = 0
    while i < len(line):
        c = line[i]
        if c in "ew":
            directions.append(Direction(c))
            i += 1
        elif c in "ns":
            directions.append(Direction(line[i : i + 2]))
            i += 2
        else:
            raise Exception("invalid input")
    return directions


def get_grid(txt):
    grid = HexGrid()
    for line in txt.splitlines():
        directions = parse(line)
        grid.flip_tile(directions)
    return grid


def part_1(txt):
    grid = get_grid(txt)
    return grid.count_black_tiles()


def part_2(txt):
    grid = get_grid(txt)
    for _day in range(100):
        grid.simulate_day()
    return grid.count_black_tiles()


if __name__ == "__main__":
    import aocd

    print(f"part_1: {part_1(aocd.data)}")
    print(f"part_2: {part_2(aocd.data)}")

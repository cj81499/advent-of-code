import collections

ON = "#"
OFF = "."


class Grid:
    def __init__(self, txt, include_diagonals=False):
        lines = txt.splitlines()

        self.height = len(lines)
        self.width = len(lines[0])
        assert all(len(line) == self.width for line in lines)

        self._grid = {}
        for y, row in enumerate(lines):
            for x, c in enumerate(row):
                self._grid[(x, y)] = c

        self.include_diagonals = include_diagonals

    def at(self, x, y):
        return self._grid.get((x, y), None)

    def put(self, x, y, val):
        old = self.at(x, y)
        self._grid[(x, y)] = val
        return old

    def adj(self, x, y):
        yield from (self.at(x, y) for (x, y) in self.adj_pos(x, y))

    def adj_pos(self, x, y):
        yield from ((x + dx, y + dy) for (dx, dy) in ((0, -1), (0, 1), (-1, 0), (1, 0)))
        if self.include_diagonals:
            yield from ((x + dx, y + dy) for (dx, dy) in ((-1, -1), (1, -1), (1, 1), (-1, 1)))

    def __str__(self):
        rows = []
        for y in range(self.height):
            row = []
            for x in range(self.width):
                row.append(self.at(x, y))
            rows.append("".join(row))
        return "\n".join(rows)


class Lightshow:
    def __init__(self, txt, corners_locked=False):
        self._grid = Grid(txt, include_diagonals=True)
        self.corners_locked = corners_locked
        self.turn_on_corners(self._grid)

    def turn_on_corners(self, grid):
        if self.corners_locked:
            grid.put(0, 0, ON)
            grid.put(grid.width - 1, 0, ON)
            grid.put(grid.width - 1, grid.height - 1, ON)
            grid.put(0, grid.height - 1, ON)

    def simulate(self, steps):
        g = self._grid
        for step in range(steps):
            g = self._next_grid(g)
        return Lightshow(str(g))

    def _next_grid(self, grid):
        rows = []
        for y in range(grid.height):
            row = []
            for x in range(grid.width):
                state = grid.at(x, y)
                new_state = OFF
                on_neighbors = collections.Counter(grid.adj(x, y))[ON]
                if state == ON and on_neighbors in (2, 3):
                    new_state = ON
                elif state == OFF and on_neighbors == 3:
                    new_state = ON
                row.append(new_state)
            rows.append("".join(row))
        g = Grid("\n".join(rows), include_diagonals=True)
        self.turn_on_corners(g)
        return g

    def count(self):
        return collections.Counter(str(self._grid))


def part_1(txt, steps=100):
    return Lightshow(txt).simulate(steps).count()[ON]


def part_2(txt, steps=100):
    return Lightshow(txt, corners_locked=True).simulate(steps).count()[ON]


if __name__ == "__main__":
    from aocd import data

    print(f"part_1: {part_1(data)}")
    print(f"part_2: {part_2(data)}")

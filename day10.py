import numpy as np
import parse

parser = parse.compile("position=<{}> velocity=<{}>")


class grid:
    def __init__(self):
        self.points = []
        self.grid = None
        self.width = 0
        self.height = 0
        self.max_x = 0
        self.max_y = 0
        self.min_x = 0
        self.min_y = 0

    def size(self):
        self.update_dims()
        return self.height * self.width

    def step(self, count):
        for p in self.points:
            p.step(count)

    def update_dims(self):
        self.max_x = self.points[0].pos[0]
        self.max_y = self.points[0].pos[1]
        self.min_x = self.points[0].pos[0]
        self.min_y = self.points[0].pos[1]
        for p in self.points:
            self.max_x = max(p.pos[0], self.max_x)
            self.max_y = max(p.pos[1], self.max_y)
            self.min_x = min(p.pos[0], self.min_x)
            self.min_y = min(p.pos[1], self.min_y)
        self.height = self.max_y - self.min_y
        self.width = self.max_x - self.min_x

    def update_grid(self):
        self.update_dims()
        self.grid = np.zeros((self.max_y - self.min_y + 1, self.max_x - self.min_x + 1), dtype=int)
        for p in self.points:
            self.grid[p.pos[1] - self.min_y, p.pos[0] - self.min_x] = 1

    def __str__(self):
        self.update_grid()
        s = ""
        for row in self.grid:
            s += "".join([("#" if x == 1 else " ") for x in list(row)]) + "\n"
        return s.rstrip()


class Point:
    def __init__(self, pos, vel):
        self.pos = pos
        self.vel = vel

    def step(self, count=1):
        self.pos[0] += count * self.vel[0]
        self.pos[1] += count * self.vel[1]


def run(lines: list):
    g = grid()
    for l in lines:
        pos, vel = [[int(y) for y in x.split(",")] for x in parser.parse(l).fixed]
        g.points.append(Point(pos, vel))
    prev_size = g.size()
    g.step(1)
    part2 = 0
    while prev_size > g.size():
        prev_size = g.size()
        step_size = int(.085 * (prev_size ** (.5)))  # This is kinda weird. Explained in day10.md
        if step_size < 50:
            step_size = 1
        g.step(step_size)
        part2 += step_size

    g.step(-1)
    return f"part1:\n{str(g)}\npart2: {part2}"


def main():
    _, input_lines = helpers.load_input(10, "The Stars Align")

    print(run(input_lines))


if __name__ == "__main__":
    import helpers
    main()

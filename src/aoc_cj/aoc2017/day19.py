from enum import Enum


class Direction(Enum):
    UP = (+0, -1)
    RIGHT = (+1, +0)
    DOWN = (+0, +1)
    LEFT = (-1, +0)

    def turns(self):
        x, y = self.value
        yield Direction((-y, +x))
        yield Direction((+y, -x))


def add_pos(p, direction: Direction):
    return tuple(sum(x) for x in zip(p, direction.value))


def helper(txt: str):
    g = {(x, y): c for y, line in enumerate(txt.splitlines()) for x, c in enumerate(line) if c != " "}
    pos = next((x, y) for x, y in g if y == 0)
    letters = []
    direction = Direction.DOWN
    steps = 0
    while pos in g:
        c = g[pos]
        if c == "+":
            direction = next(d for d in direction.turns() if add_pos(pos, d) in g)
        elif c.isalpha():
            letters.append(c)
        pos = add_pos(pos, direction)
        steps += 1
    return "".join(letters), steps


def part_1(txt: str):
    return helper(txt)[0]


def part_2(txt: str):
    return helper(txt)[1]


if __name__ == "__main__":
    from aocd import data

    print(f"part_1: {part_1(data)}")
    print(f"part_2: {part_2(data)}")

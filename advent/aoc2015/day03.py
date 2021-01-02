from advent.aoc2015.point import Point

MOVES = {
    "^": Point(0, 1),
    "v": Point(0, -1),
    "<": Point(-1, 0),
    ">": Point(1, 0)
}


def parta(directions: str):
    pos = Point(0, 0)
    visited = set()
    visited.add(pos)
    for c in directions:
        pos += MOVES[c]
        visited.add(pos)
    return len(visited)


def partb(directions: str):
    pos = [Point(0, 0), Point(0, 0)]
    i = 0
    visited = set()
    visited.add(pos[0])
    for c in directions:
        pos[i] += MOVES[c]
        visited.add(pos[i])
        i = (i+1) % 2
    return len(visited)


def main(txt):
    print(f"parta: {parta(txt)}")
    print(f"partb: {partb(txt)}")


if __name__ == "__main__":
    from aocd import data
    main(data)

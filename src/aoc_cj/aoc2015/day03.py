MOVES = {"^": (0, 1), "v": (0, -1), "<": (-1, 0), ">": (1, 0)}


def parta(directions: str):
    pos = (0, 0)
    visited = {pos}
    for d in directions:
        pos = (pos[0] + MOVES[d][0], pos[1] + MOVES[d][1])
        visited.add(pos)
    return len(visited)


def partb(directions: str):
    active, inactive = (0, 0), (0, 0)
    visited = {active}
    for d in directions:
        active = (active[0] + MOVES[d][0], active[1] + MOVES[d][1])
        visited.add(active)
        active, inactive = inactive, active
    return len(visited)


def main(txt):
    print(f"parta: {parta(txt)}")
    print(f"partb: {partb(txt)}")


if __name__ == "__main__":
    from aocd import data

    main(data)

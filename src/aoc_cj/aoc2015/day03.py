MOVES = {"^": (0, 1), "v": (0, -1), "<": (-1, 0), ">": (1, 0)}


def part_1(directions: str) -> int:
    pos = (0, 0)
    visited = {pos}
    for d in directions:
        pos = (pos[0] + MOVES[d][0], pos[1] + MOVES[d][1])
        visited.add(pos)
    return len(visited)


def part_2(directions: str) -> int:
    active, inactive = (0, 0), (0, 0)
    visited = {active}
    for d in directions:
        active = (active[0] + MOVES[d][0], active[1] + MOVES[d][1])
        visited.add(active)
        active, inactive = inactive, active
    return len(visited)


if __name__ == "__main__":
    from aocd import data

    print(f"part_1: {part_1(data)}")
    print(f"part_2: {part_2(data)}")

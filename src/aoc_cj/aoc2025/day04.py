from aoc_cj.util import adj_8


def part_1(txt: str) -> int:
    paper = {complex(x, y) for y, line in enumerate(txt.splitlines()) for x, c in enumerate(line) if c == "@"}
    qty = 0
    for pos in paper:
        can_access = sum(p in paper for p in adj_8(pos)) < 4
        if can_access:
            qty += 1
    return qty


def part_2(txt: str) -> int:
    paper = {complex(x, y) for y, line in enumerate(txt.splitlines()) for x, c in enumerate(line) if c == "@"}
    remove = set[complex]()
    go = True
    while go:
        go = False
        paper -= remove
        for pos in paper:
            can_access = sum(p in paper for p in adj_8(pos)) < 4
            if can_access:
                go = True
                remove.add(pos)

    return len(remove)


if __name__ == "__main__":
    import aocd

    print(f"part_1: {part_1(aocd.data)}")
    print(f"part_2: {part_2(aocd.data)}")

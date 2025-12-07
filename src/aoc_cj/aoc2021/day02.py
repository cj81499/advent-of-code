from collections.abc import Iterable


def parse(txt: str) -> Iterable[tuple[str, int]]:
    splits = map(txt.split, txt.splitlines())
    yield from ((cmd, int(x)) for cmd, x in splits)


def part_1(txt: str) -> int:
    horiz = 0
    depth = 0
    for cmd, x in parse(txt):
        if cmd[0] == "f":
            horiz += x
        elif cmd[0] == "d":
            depth += x
        elif cmd[0] == "u":
            depth -= x
    return horiz * depth


def part_2(txt: str) -> int:
    horiz = 0
    depth = 0
    aim = 0
    for cmd, x in parse(txt):
        if cmd[0] == "f":
            horiz += x
            depth += aim * x
        elif cmd[0] == "d":
            aim += x
        elif cmd[0] == "u":
            aim -= x
    return horiz * depth


if __name__ == "__main__":
    import aocd

    print(f"part_1: {part_1(aocd.data)}")
    print(f"part_2: {part_2(aocd.data)}")

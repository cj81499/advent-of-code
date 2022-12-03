from collections.abc import Iterable


def parse(txt: str) -> Iterable[tuple[str, int]]:
    splits = (l.split() for l in txt.splitlines())
    yield from ((cmd, int(x)) for cmd, x in splits)


def parta(txt: str) -> int:
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


def partb(txt: str) -> int:
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
    from aocd import data

    print(f"parta: {parta(data)}")
    print(f"partb: {partb(data)}")

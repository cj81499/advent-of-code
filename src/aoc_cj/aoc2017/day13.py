import itertools


def scanner_pos(r, t):
    cycle_len = 2 * r - 2
    p = t % cycle_len
    return p if p < r else cycle_len - p


def caught_at(scanners, pos, delay=0):
    return scanner_pos(scanners[pos], delay + pos) == 0 if pos in scanners else False


def parse_scanners(txt: str):
    return dict(map(int, line.split(": ")) for line in txt.splitlines())


def part_1(txt: str):
    scanners = parse_scanners(txt)
    return sum(pos * rng for pos, rng in scanners.items() if caught_at(scanners, pos))


def part_2(txt: str):
    scanners = parse_scanners(txt)
    return next(d for d in itertools.count() if all(not caught_at(scanners, pos, delay=d) for pos in scanners))


if __name__ == "__main__":
    from aocd import data

    print(f"part_1: {part_1(data)}")
    print(f"part_2: {part_2(data)}")

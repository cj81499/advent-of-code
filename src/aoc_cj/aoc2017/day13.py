import itertools


def scanner_pos(r, t):
    cycle_len = 2 * r - 2
    p = t % cycle_len
    return p if p < r else cycle_len - p


def caught_at(scanners, pos, delay=0):
    return scanner_pos(scanners[pos], delay + pos) == 0 if pos in scanners else False


def parse_scanners(txt: str):
    return dict(map(int, line.split(": ")) for line in txt.splitlines())


def parta(txt: str):
    scanners = parse_scanners(txt)
    return sum(pos * rng for pos, rng in scanners.items() if caught_at(scanners, pos))


def partb(txt: str):
    scanners = parse_scanners(txt)
    return next(d for d in itertools.count() if all(not caught_at(scanners, pos, delay=d) for pos in scanners))


def main(txt: str):
    print(f"parta: {parta(txt)}")
    print(f"partb: {partb(txt)}")


if __name__ == "__main__":
    from aocd import data

    main(data)

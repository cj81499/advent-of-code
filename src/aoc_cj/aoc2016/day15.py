import itertools
import re

DIGITS_REGEX = re.compile(r"(\d+)")


def nums(txt: str):
    return tuple(int(x) for x in DIGITS_REGEX.findall(txt))


def position(disc, t):
    _, num_positions, _, start_pos = disc
    return (start_pos + t) % num_positions


def simulate(txt, additional_disc=False):
    discs = [nums(line) for line in txt.splitlines()]
    if additional_disc:
        discs.append((len(discs) + 1, 11, 0, 0))
    for push_time in itertools.count():
        if all(position(d, push_time + d[0]) == 0 for d in discs):
            return push_time


def part_1(txt: str):
    return simulate(txt)


def part_2(txt: str):
    return simulate(txt, additional_disc=True)


if __name__ == "__main__":
    import aocd

    print(f"part_1: {part_1(aocd.data)}")
    print(f"part_2: {part_2(aocd.data)}")

import re

import more_itertools as mi


def parta(txt: str) -> int:
    maxes = {"red": 12, "green": 13, "blue": 14}
    s = 0
    for line in txt.splitlines():
        _, game_id, *rest = re.findall(r"[a-zA-Z0-9]+", line)
        possible = True
        for count, color in mi.batched(rest, 2):
            if int(count) > maxes[color]:
                possible = False
        if possible:
            print(f"possible: {game_id}")
            s += int(game_id)
    return s


def partb(txt: str) -> int:
    s = 0
    for line in txt.splitlines():
        max_seen = {"red": 0, "green": 0, "blue": 0}
        _, game_id, *rest = re.findall(r"[a-zA-Z0-9]+", line)
        for count, color in mi.batched(rest, 2):
            max_seen[color] = max(max_seen[color], int(count))
        # TODO: util.product
        power = max_seen["red"] * max_seen["green"] * max_seen["blue"]
        s += power
    return s


if __name__ == "__main__":
    from aocd import data

    print(f"parta: {parta(data)}")
    print(f"partb: {partb(data)}")

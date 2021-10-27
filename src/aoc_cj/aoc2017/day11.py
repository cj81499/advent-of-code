from __future__ import annotations


def helper(txt):
    x, y, z = 0, 0, 0
    all_time_max = 0
    for move in txt.split(","):
        if move == "n":
            y += 1
            z -= 1
        elif move == "ne":
            x += 1
            z -= 1
        elif move == "se":
            x += 1
            y -= 1
        elif move == "s":
            y -= 1
            z += 1
        elif move == "sw":
            x -= 1
            z += 1
        elif move == "nw":
            x -= 1
            y += 1
        all_time_max = max(all_time_max, x, y, z)
    return max(x, y, z), all_time_max


def parta(txt: str):
    return helper(txt)[0]


def partb(txt: str):
    return helper(txt)[1]


def main(txt: str):
    print(f"parta: {parta(txt)}")
    print(f"partb: {partb(txt)}")


if __name__ == "__main__":
    from aocd import data

    main(data)

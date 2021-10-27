from collections import Counter


def parta(s: str):
    c = Counter(s)
    return c["("] - c[")"]


def partb(s: str):
    floor = 0
    for i, x in enumerate(s):
        floor += 1 if x == "(" else -1
        if floor == -1:
            return i + 1


def main(txt):
    print(f"parta: {parta(txt)}")
    print(f"partb: {partb(txt)}")


if __name__ == "__main__":
    from aocd import data

    main(data)

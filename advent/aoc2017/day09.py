from __future__ import annotations


def helper(txt):
    score = 0
    depth = 0
    ignore = False
    skip = False
    garbage_count = 0
    for c in txt:
        if skip:
            skip = False
            continue
        if c == "!":
            skip = True
        elif c == ">":
            ignore = False
        elif ignore:
            garbage_count += 1
        elif c == "<":
            ignore = True
        elif c == "{":
            depth += 1
        elif c == "}":
            score += depth
            depth -= 1
    return score, garbage_count


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

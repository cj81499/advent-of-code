TARGET_QUALITIES = {
    "children": 3,
    "cats": 7,
    "samoyeds": 2,
    "pomeranians": 3,
    "akitas": 0,
    "vizslas": 0,
    "goldfish": 5,
    "trees": 3,
    "cars": 2,
    "perfumes": 1,
}

GT_QUALITIES = set(("cats", "trees"))
LT_QUALITIES = set(("pomeranians", "goldfish"))


def parta(txt):
    return helper(txt)


def partb(txt):
    return helper(txt, True)


def helper(txt, partb=False):
    sues = parse_sues(txt)

    for qual in TARGET_QUALITIES:
        n = TARGET_QUALITIES[qual]
        sues = [s for s in sues if check_sue(s, qual, n, partb)]

    if len(sues) != 1:
        raise AssertionError("bad input")

    return sues[0]["SUE_ID"]


def parse_sues(txt):
    return [parse_sue(line) for line in txt.splitlines()]


def parse_sue(sue_str):
    sue = {}

    colon_i = sue_str.index(": ")
    num = int(sue_str[4:colon_i])
    attrs = sue_str[colon_i + 2 :].split(", ")

    sue["SUE_ID"] = num
    for attr in attrs:
        q, n = attr.split(": ")
        sue[q] = int(n)

    return sue


def check_sue(sue, qual, n, partb=False):
    if qual not in sue:
        return True

    comparison = int.__eq__

    if partb:
        if qual in GT_QUALITIES:
            comparison = int.__gt__
        elif qual in LT_QUALITIES:
            comparison = int.__lt__

    return comparison(sue[qual], n)


def main(txt):
    print(f"parta: {parta(txt)}")
    print(f"partb: {partb(txt)}")


if __name__ == "__main__":
    from aocd import data

    main(data)

from datetime import date

import helpers

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
    "perfumes": 1
}

GT_QUALITIES = set(("cats", "trees"))
LT_QUALITIES = set(("pomeranians", "goldfish"))


def part1(s, lines):
    return helper(lines)


def part2(s, lines):
    return helper(lines, True)


def helper(lines, part2=False):
    sues = parse_sues(lines)

    for qual in TARGET_QUALITIES:
        n = TARGET_QUALITIES[qual]
        sues = [s for s in sues if check_sue(s, qual, n, part2)]

    if len(sues) != 1:
        raise AssertionError("bad input")

    return sues[0]["SUE_ID"]


def parse_sues(lines):
    return [parse_sue(line) for line in lines]


def parse_sue(sue_str):
    sue = {}

    colon_i = sue_str.index(": ")
    num = int(sue_str[4:colon_i])
    attrs = sue_str[colon_i + 2:].split(", ")

    sue["SUE_ID"] = num
    for attr in attrs:
        q, n = attr.split(": ")
        sue[q] = int(n)

    return sue


def check_sue(sue, qual, n, part2=False):
    if qual not in sue:
        return True

    comparison = int.__eq__

    if part2:
        if qual in GT_QUALITIES:
            comparison = int.__gt__
        elif qual in LT_QUALITIES:
            comparison = int.__lt__

    return comparison(sue[qual], n)


def main():
    input_txt, input_lines = helpers.get_puzzle(date(2015, 12, 16), "Aunt Sue")  # noqa

    print(f"part1: {part1(input_txt, input_lines)}")
    print(f"part2: {part2(input_txt, input_lines)}")


if __name__ == "__main__":
    main()

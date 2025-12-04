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

GT_QUALITIES = {"cats", "trees"}
LT_QUALITIES = {"pomeranians", "goldfish"}


def part_1(txt: str) -> int:
    return helper(txt)


def part_2(txt: str) -> int:
    return helper(txt, True)


def helper(txt: str, part_2: bool = False) -> int:
    aunts = parse_aunts(txt)

    for qual in TARGET_QUALITIES:
        n = TARGET_QUALITIES[qual]
        aunts = [s for s in aunts if check_aunt(s, qual, n, part_2)]

    if len(aunts) != 1:
        raise AssertionError("bad input")

    return aunts[0]["SUE_ID"]


def parse_aunts(txt: str) -> list[dict[str, int]]:
    return [parse_aunt(line) for line in txt.splitlines()]


def parse_aunt(aunt_str: str) -> dict[str, int]:
    sue: dict[str, int] = {}

    colon_i = aunt_str.index(": ")
    num = int(aunt_str[4:colon_i])
    attrs = aunt_str[colon_i + 2 :].split(", ")

    sue["SUE_ID"] = num
    for attr in attrs:
        q, n = attr.split(": ")
        sue[q] = int(n)

    return sue


def check_aunt(aunt: dict[str, int], qual: str, n: int, part_2: bool = False) -> bool:
    if qual not in aunt:
        return True

    if part_2:
        if qual in GT_QUALITIES:
            return aunt[qual] > n
        if qual in LT_QUALITIES:
            return aunt[qual] < n

    return aunt[qual] == n


if __name__ == "__main__":
    import aocd

    print(f"part_1: {part_1(aocd.data)}")
    print(f"part_2: {part_2(aocd.data)}")

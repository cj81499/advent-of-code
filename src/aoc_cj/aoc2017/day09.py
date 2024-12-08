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


def part_1(txt: str):
    return helper(txt)[0]


def part_2(txt: str):
    return helper(txt)[1]


if __name__ == "__main__":
    import aocd

    print(f"part_1: {part_1(aocd.data)}")
    print(f"part_2: {part_2(aocd.data)}")

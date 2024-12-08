import more_itertools as mi


def step(data):
    a = data
    b = "".join("1" if c == "0" else "0" for c in reversed(a))
    return f"{a}0{b}"


def checksum(data):
    cs = "".join("1" if len(set(pair)) == 1 else "0" for pair in mi.ichunked(data, 2))
    return checksum(cs) if len(cs) % 2 == 0 else cs


def part_1(txt: str, length=272):
    data = txt
    while len(data) < length:
        data = step(data)
    return checksum(data[:length])


def part_2(txt: str):
    return part_1(txt, length=35651584)


if __name__ == "__main__":
    import aocd

    print(f"part_1: {part_1(aocd.data)}")
    print(f"part_2: {part_2(aocd.data)}")

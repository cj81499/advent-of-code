alphabet = "abcdefghijklmnopqrstuvwxyz"


def part_1(txt: str):
    prev_len = 0
    while prev_len != len(txt):
        prev_len = len(txt)
        for c in alphabet:
            txt = txt.replace(c + c.upper(), "").replace(c.upper() + c, "")
    return len(txt)


def part_2(txt):
    d = {}
    for c in alphabet:
        d[c] = part_1(txt.replace(c, "").replace(c.upper(), ""))
    shortest_length = d["a"]
    for c in alphabet:
        if d[c] < shortest_length:
            shortest_length = d[c]
    return shortest_length


def part_2_polished(txt):
    shortest_length = part_1(txt)
    for c in alphabet:
        length = part_1(txt.replace(c, "").replace(c.upper(), ""))
        if length < shortest_length:
            shortest_length = length
    return shortest_length


if __name__ == "__main__":
    import aocd

    print(f"part_1: {part_1(aocd.data)}")
    print(f"part_2: {part_2(aocd.data)}")

alphabet = "abcdefghijklmnopqrstuvwxyz"


def part1(txt: str):
    prev_len = 0
    while prev_len != len(txt):
        prev_len = len(txt)
        for c in alphabet:
            txt = txt.replace(c + c.upper(), "").replace(c.upper() + c, "")
    return len(txt)


def part2(txt):
    d = {}
    for c in alphabet:
        d[c] = part1(txt.replace(c, "").replace(c.upper(), ""))
    shortest_length = d["a"]
    for c in alphabet:
        if d[c] < shortest_length:
            shortest_length = d[c]
    return shortest_length


def part2_polished(txt):
    shortest_length = part1(txt)
    for c in alphabet:
        length = part1(txt.replace(c, "").replace(c.upper(), ""))
        if length < shortest_length:
            shortest_length = length
    return shortest_length


def main():
    input_txt, _ = helpers.load_input(5, "Alchemical Reduction")

    print(f"part1: {part1(input_txt)}")
    print(f"part2: {part2(input_txt)}")
    print(f"part2_polished: {part2_polished(input_txt)}")


if __name__ == "__main__":
    import helpers
    main()
